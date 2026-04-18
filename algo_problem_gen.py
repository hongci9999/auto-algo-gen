"""
Ollama 로컬 API로 알고리즘(코딩테스트) 문제를 생성하고,
언어(javascript / java / python) · 유형별 폴더에 마크다운으로 저장합니다.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import ollama
except ImportError:
    print("ollama 패키지가 필요합니다: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

# `python 다른경로\algo_problem_gen.py` 처럼 실행해도, 상대 --out 은 항상 이 스크립트가 있는 폴더 기준
_SCRIPT_DIR = Path(__file__).resolve().parent


def resolve_output_root(out: str) -> Path:
    p = Path(out.strip() or "problems")
    if p.is_absolute():
        return p
    return (_SCRIPT_DIR / p).resolve()


# CLI 별칭 → 저장 디렉터리명
LANG_ALIASES: dict[str, str] = {
    "js": "javascript",
    "javascript": "javascript",
    "node": "javascript",
    "nodejs": "javascript",
    "java": "java",
    "py": "python",
    "python": "python",
    "python3": "python",
}

SYSTEM_PROMPT = """당신은 한국어로 출제하는 알고리즘·자료구조 코딩테스트 출제자입니다.
반드시 아래 JSON 스키마에 맞는 **유효한 JSON 하나만** 출력하세요.
JSON 앞뒤에 설명 문장, 마크다운 코드펜스, 주석을 넣지 마세요.

스키마:
{
  "title": "문제 제목 (한 줄)",
  "language": "javascript, java, python 중 하나 (소문자)",
  "type": "유형 한 줄 (예: 그래프, DP, 투포인터, 구현, 시뮬레이션, 자료구조)",
  "difficulty": "쉬움|보통|어려움 중 하나",
  "tags": ["태그1", "태그2"],
  "statement": "문제 본문 (입력/출력 설명 포함, 마크다운 가능)",
  "input_format": "입력 형식 설명",
  "output_format": "출력 형식 설명",
  "constraints": "제약 조건 (시간/메모리, N 범위 등)",
  "io_notes": "해당 언어에서의 입출력 안내 (예: Node readline, Java BufferedReader+StringTokenizer, Python sys.stdin.readline 등)",
  "samples": [
    {"input": "예제 입력 문자열", "output": "예제 출력 문자열", "explanation": "선택, 짧은 설명"}
  ],
  "hints": ["힌트1", "힌트2"],
  "reference_approach": "알고리즘 개요 (개념 위주, 짧게)",
  "solution_explanation": "풀이 해설: 아이디어 → 단계 → 시간복잡도까지 서술형으로 자세히 (한국어)",
  "reference_solution": "위 해설과 일치하는 참고 정답 코드 전체 (language 필드에 맞는 문법만 사용, 주석 포함 가능)"
}

요구사항:
- language가 javascript이면 Node.js 기준으로 풀이·참고 코드를 작성 (브라우저 전용 API 금지).
- language가 java이면 Java 17 이하에서도 돌아가게 작성.
- language가 python이면 Python 3.10+ 기준, 표준 라이브러리만 사용 (numpy/pandas 등 외부 패키지 금지).
- 실제 코딩테스트 수준의 명확한 입출력.
- 예제는 최소 2개.
- solution_explanation은 초보자도 따라갈 수 있게 단계적으로.
- reference_solution은 컴파일·실행 가능한 형태로.
"""


def normalize_language(name: str) -> str:
    key = name.strip().lower()
    if key not in LANG_ALIASES:
        allowed = ", ".join(sorted(set(LANG_ALIASES.values())))
        raise ValueError(f"지원하지 않는 언어: {name!r} (허용: {allowed})")
    return LANG_ALIASES[key]


def unique_languages(names: list[str]) -> list[str]:
    out: list[str] = []
    for n in names:
        u = normalize_language(n)
        if u not in out:
            out.append(u)
    return out


def slugify_segment(s: str, max_len: int = 48) -> str:
    s = (s or "").strip()
    s = re.sub(r'[<>:"/\\|?*\n\r\t#]', "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-._")
    if not s:
        s = "misc"
    return s[:max_len]


def _first_balanced_object(text: str) -> str | None:
    start = text.find("{")
    if start == -1:
        return None
    depth = 0
    in_string = False
    escape = False
    for i in range(start, len(text)):
        c = text[i]
        if escape:
            escape = False
            continue
        if in_string:
            if c == "\\":
                escape = True
            elif c == '"':
                in_string = False
            continue
        if c == '"':
            in_string = True
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    return None


def _extract_json_object(text: str) -> dict[str, Any]:
    text = text.strip()
    errors: list[str] = []

    def _try_load(raw: str, label: str) -> dict[str, Any] | None:
        raw = raw.strip()
        if not raw:
            return None
        try:
            out = json.loads(raw)
        except json.JSONDecodeError as e:
            errors.append(f"{label}: {e}")
            return None
        if isinstance(out, dict):
            return out
        errors.append(f"{label}: 루트가 객체가 아님 ({type(out).__name__})")
        return None

    if r := _try_load(text, "전체"):
        return r

    fence = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text, re.IGNORECASE)
    if fence and (r := _try_load(fence.group(1), "코드펜스")):
        return r

    balanced = _first_balanced_object(text)
    if balanced and (r := _try_load(balanced, "균형구간")):
        return r

    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        if r := _try_load(text[start : end + 1], "첫{~마지}"):
            return r

    detail = "; ".join(errors[:3]) if errors else "파싱 시도 없음"
    snippet = text[:1200] + ("…" if len(text) > 1200 else "")
    raise ValueError(
        "모델 응답에서 JSON 객체를 파싱할 수 없습니다.\n"
        f"원인 요약: {detail}\n"
        f"응답 앞부분:\n{snippet}"
    )


def _validate_problem(data: dict[str, Any]) -> None:
    required = (
        "title",
        "language",
        "type",
        "statement",
        "input_format",
        "output_format",
        "constraints",
        "samples",
        "solution_explanation",
        "reference_solution",
    )
    for key in required:
        if key not in data or data[key] in (None, ""):
            raise ValueError(f"필수 필드 누락 또는 비어 있음: {key}")
    if not isinstance(data["samples"], list) or len(data["samples"]) < 2:
        raise ValueError("samples는 예제 2개 이상의 배열이어야 합니다.")


def _code_fence_lang(language: str) -> str:
    if language == "java":
        return "java"
    if language == "python":
        return "python"
    return "javascript"


def format_problem_markdown(data: dict[str, Any]) -> str:
    lines: list[str] = []
    title = str(data.get("title", "제목 없음"))
    diff = str(data.get("difficulty", ""))
    lang = str(data.get("language", ""))
    prob_type = str(data.get("type", ""))
    tags = data.get("tags") or []
    tag_str = ", ".join(str(t) for t in tags) if isinstance(tags, list) else ""

    lines.append(f"# {title}\n")
    meta_bits = [b for b in (lang, prob_type, diff, tag_str) if b]
    if meta_bits:
        lines.append(f"*{' · '.join(meta_bits)}*\n")

    io_notes = data.get("io_notes")
    if io_notes:
        lines.append(f"\n## 입출력 환경\n\n{str(io_notes).strip()}\n")

    lines.append("\n## 문제\n\n")
    lines.append(str(data.get("statement", "")).strip())
    lines.append("\n\n## 입력\n\n")
    lines.append(str(data.get("input_format", "")).strip())
    lines.append("\n\n## 출력\n\n")
    lines.append(str(data.get("output_format", "")).strip())
    lines.append("\n\n## 제약 조건\n\n")
    lines.append(str(data.get("constraints", "")).strip())

    samples = data.get("samples") or []
    if isinstance(samples, list):
        for i, s in enumerate(samples, 1):
            if not isinstance(s, dict):
                continue
            lines.append(
                f"\n\n## 예제 {i}\n\n**입력**\n```\n{s.get('input', '')}\n```\n\n**출력**\n```\n{s.get('output', '')}\n```"
            )
            exp = s.get("explanation")
            if exp:
                lines.append(f"\n\n*{exp}*")

    hints = data.get("hints")
    if isinstance(hints, list) and hints:
        lines.append("\n\n## 힌트\n\n")
        lines.extend(f"- {h}\n" for h in hints if h)

    ref = data.get("reference_approach")
    if ref:
        lines.append("\n\n## 알고리즘 요약\n\n")
        lines.append(str(ref).strip())

    sol = data.get("solution_explanation")
    if sol:
        lines.append("\n\n## 풀이 해설\n\n")
        lines.append(str(sol).strip())

    code = data.get("reference_solution")
    if code:
        fence = _code_fence_lang(lang)
        lines.append(f"\n\n## 참고 코드 ({lang})\n\n```{fence}\n")
        lines.append(str(code).strip("\n"))
        lines.append("\n```\n")

    return "".join(lines).strip() + "\n"


def generate_problem(
    client: ollama.Client,
    model: str,
    difficulty: str,
    topic: str | None,
    extra: str | None,
    language: str,
    problem_type: str | None,
) -> dict[str, Any]:
    lang = normalize_language(language)
    user_parts = [
        f"난이도: {difficulty}.",
        f"풀이·참고 코드 작성 언어: {lang} (JSON의 language 필드도 반드시 이 값과 동일하게).",
    ]
    if problem_type:
        user_parts.append(f"문제 유형(type 필드): 반드시 '{problem_type}' 로 태깅할 것.")
    if topic:
        user_parts.append(f"주제/태그 방향: {topic}.")
    if extra:
        user_parts.append(f"추가 요청: {extra}.")
    user_parts.append("위 조건에 맞는 새 문제 하나를 JSON으로만 출력하세요.")

    response = client.chat(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": " ".join(user_parts)},
        ],
        format="json",
        options={"temperature": 0.72},
    )
    content = response.get("message", {}).get("content", "")
    if not content:
        raise RuntimeError("모델이 빈 응답을 반환했습니다.")

    data = _extract_json_object(content)
    data["language"] = lang
    if problem_type:
        data["type"] = problem_type
    _validate_problem(data)

    out_lang = normalize_language(str(data.get("language", lang)))
    if out_lang != lang:
        data["language"] = lang
    return data


def unique_md_path(directory: Path, base_slug: str) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    p = directory / f"{base_slug}.md"
    if not p.exists():
        return p
    for n in range(2, 1000):
        cand = directory / f"{base_slug}_{n}.md"
        if not cand.exists():
            return cand
    return directory / f"{base_slug}_{uuid.uuid4().hex[:8]}.md"


def write_problem_bundle(
    root: Path,
    data: dict[str, Any],
    *,
    save_json: bool,
) -> tuple[Path, Path | None]:
    lang = normalize_language(str(data["language"]))
    type_slug = slugify_segment(str(data.get("type", "misc")))
    title_slug = slugify_segment(str(data.get("title", "problem")), max_len=64)
    dir_path = root / lang / type_slug
    md_path = unique_md_path(dir_path, title_slug)
    md_path.write_text(format_problem_markdown(data), encoding="utf-8")
    json_path: Path | None = None
    if save_json:
        json_path = md_path.with_suffix(".json")
        json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return md_path, json_path


def parse_comma_list(s: str) -> list[str]:
    return [p.strip() for p in s.split(",") if p.strip()]


def _get_git_root(start: Path) -> Path | None:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=start,
            capture_output=True,
            text=True,
            check=True,
        )
        line = (out.stdout or "").strip()
        return Path(line) if line else None
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None


def _git_current_branch(repo: Path) -> str:
    out = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=repo,
        capture_output=True,
        text=True,
        check=True,
    )
    return (out.stdout or "").strip() or "HEAD"


def _paths_for_git_add(repo: Path, written: list[tuple[Path, Path | None]]) -> list[str]:
    repo = repo.resolve()
    rels: list[str] = []
    for md_path, json_path in written:
        for p in (md_path, json_path):
            if p is None:
                continue
            try:
                rels.append(p.resolve().relative_to(repo).as_posix())
            except ValueError:
                pass
    return rels


def git_add_commit_push(
    repo: Path,
    paths: list[str],
    *,
    remote: str,
    branch: str | None,
    message: str,
) -> str:
    if not paths:
        raise ValueError("git에 추가할 상대 경로가 없습니다. 저장 위치가 저장소 루트 밖인지 확인하세요.")

    subprocess.run(["git", "add", "--"] + paths, cwd=repo, check=True)

    st = subprocess.run(["git", "diff", "--staged", "--quiet"], cwd=repo)
    if st.returncode == 0:
        return "스테이징된 변경 없음(이미 동일). 커밋·푸시 생략."

    br = branch.strip() if branch else _git_current_branch(repo)
    subprocess.run(["git", "commit", "-m", message], cwd=repo, check=True)
    subprocess.run(["git", "push", remote.strip() or "origin", br], cwd=repo, check=True)
    return f"커밋 후 {remote!r} → {br!r} 푸시 완료."


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ollama로 JS/Java/Python 알고리즘 문제를 만들고 언어·유형별 폴더에 MD로 저장합니다.",
    )
    parser.add_argument("--model", default="gemma4", help="Ollama 모델 이름")
    parser.add_argument(
        "--difficulty",
        choices=("쉬움", "보통", "어려움"),
        default="보통",
    )
    parser.add_argument("--topic", default="", help="주제 힌트 (예: 그래프, 누적합)")
    parser.add_argument("--extra", default="", help="출제에 반영할 추가 요청")
    parser.add_argument(
        "--langs",
        default="javascript,java,python",
        help="쉼표 구분 (기본: javascript,java,python). 별칭: js,node→javascript / py→python",
    )
    parser.add_argument(
        "--types",
        default="",
        help="유형 고정 시 쉼표 구분 (예: DP,그래프,BFS). 비우면 모델이 type을 정함(각 언어마다 생성).",
    )
    parser.add_argument(
        "--per",
        type=int,
        default=1,
        metavar="N",
        help="(언어×유형) 조합당 생성할 문제 수 (기본 1)",
    )
    parser.add_argument(
        "--out",
        default="problems",
        help="저장 루트. 상대 경로면 algo_problem_gen.py 가 있는 폴더 기준 (기본 problems)",
    )
    parser.add_argument(
        "--save-json",
        action="store_true",
        help="같은 이름의 .json도 함께 저장",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="생성된 마크다운 전체를 표준 출력에도 인쇄",
    )
    parser.add_argument("--host", default="", help="Ollama 호스트 URL (선택)")
    parser.add_argument(
        "--git-push",
        action="store_true",
        help="생성·저장 후 해당 파일만 git add → commit → push (스크립트 폴더 기준 git 저장소)",
    )
    parser.add_argument(
        "--git-remote",
        default="origin",
        help="git push 대상 리모트 (기본 origin)",
    )
    parser.add_argument(
        "--git-branch",
        default="",
        metavar="NAME",
        help="푸시할 브랜치. 비우면 현재 체크아웃 브랜치",
    )
    parser.add_argument(
        "--git-message",
        default="",
        metavar="TEXT",
        help="커밋 메시지. 비우면 자동 생성",
    )
    args = parser.parse_args()

    try:
        lang_list = unique_languages(parse_comma_list(args.langs))
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 1

    if not lang_list:
        print("--langs 에 최소 한 언어를 지정하세요.", file=sys.stderr)
        return 1

    types_list = parse_comma_list(args.types)
    topic = args.topic.strip() or None
    extra = args.extra.strip() or None
    root = resolve_output_root(args.out)

    host = args.host.strip()
    client = ollama.Client(host=host) if host else ollama.Client()

    per = max(1, args.per)
    jobs: list[tuple[str, str]] = []
    if types_list:
        for lang in lang_list:
            for t in types_list:
                for _ in range(per):
                    jobs.append((lang, t))
    else:
        for lang in lang_list:
            for _ in range(per):
                jobs.append((lang, ""))

    written: list[tuple[Path, Path | None]] = []
    try:
        for lang, typ in jobs:
            data = generate_problem(
                client,
                model=args.model,
                difficulty=args.difficulty,
                topic=topic,
                extra=extra,
                language=lang,
                problem_type=typ or None,
            )
            paths = write_problem_bundle(root, data, save_json=args.save_json)
            written.append(paths)
            if args.show:
                print(format_problem_markdown(data))
    except ollama.ResponseError as e:
        print(f"Ollama API 오류: {e}", file=sys.stderr)
        return 2
    except (ValueError, RuntimeError, json.JSONDecodeError) as e:
        print(str(e), file=sys.stderr)
        return 3

    # 본문은 파일에만 두고, 저장 결과는 stdout에 표시 (stderr만 보면 저장 여부가 안 보이는 경우 방지)
    print(f"\n저장 완료: 마크다운 {len(written)}개 → 루트 {root.resolve()}")
    for md_path, json_path in written:
        line = f"  - {md_path}"
        if json_path:
            line += f"  (+ {json_path.name})"
        print(line)

    if args.git_push:
        repo = _get_git_root(_SCRIPT_DIR)
        if not repo:
            print("\n[git] 스크립트 위치가 git 저장소 안이 아니어서 푸시를 건너뜁니다.", file=sys.stderr)
            return 4
        rel_paths = _paths_for_git_add(repo, written)
        msg = args.git_message.strip()
        if not msg:
            ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%MZ")
            msg = f"문제 자동 생성 {len(written)}개 ({ts})"
        try:
            git_note = git_add_commit_push(
                repo,
                rel_paths,
                remote=args.git_remote,
                branch=args.git_branch or None,
                message=msg,
            )
            print(f"\n[git] {git_note}")
        except ValueError as e:
            print(f"\n[git] {e}", file=sys.stderr)
            return 4
        except subprocess.CalledProcessError as e:
            print(f"\n[git] 실패 (exit {e.returncode}): {e}", file=sys.stderr)
            return 5

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
