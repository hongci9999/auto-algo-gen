# 로그온(또는 예약 작업)에서 실행: 문제 생성 후 --git-push
# 위치: algo_problem_gen.py 와 같은 폴더에 두세요.
#
# Ollama가 시작 프로그램에서 늦게 뜨는 경우: 아래 대기 후 실행.
#   $env:OLLAMA_WAIT_URL = "http://127.0.0.1:11434/api/tags"
#   $env:OLLAMA_WAIT_MAX_SEC = "600"
#   $env:OLLAMA_WAIT_INTERVAL_SEC = "5"

$ErrorActionPreference = "Continue"
$Root = $PSScriptRoot
Set-Location -LiteralPath $Root

$ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$history = Join-Path $Root "auto_gen_history.log"
$lastLog = Join-Path $Root "auto_gen_last.log"

function Write-HistoryLine([string]$line) {
    Add-Content -LiteralPath $history -Value $line -Encoding UTF8
}

function Wait-OllamaHttp {
    $url = $env:OLLAMA_WAIT_URL
    if (-not $url) { $url = "http://127.0.0.1:11434/api/tags" }
    $max = 600
    if ($env:OLLAMA_WAIT_MAX_SEC -match '^\d+$') { $max = [int]$env:OLLAMA_WAIT_MAX_SEC }
    if ($max -lt 30) { $max = 600 }
    $step = 5
    if ($env:OLLAMA_WAIT_INTERVAL_SEC -match '^\d+$') { $step = [int]$env:OLLAMA_WAIT_INTERVAL_SEC }
    if ($step -lt 2) { $step = 5 }
    $deadline = (Get-Date).AddSeconds($max)
    Write-HistoryLine "[$((Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))] Ollama 대기: $url (최대 ${max}s, 간격 ${step}s)"
    while ((Get-Date) -lt $deadline) {
        try {
            $r = Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 8 -ErrorAction Stop
            if ($r.StatusCode -eq 200) {
                Write-HistoryLine "[$((Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))] Ollama 준비됨"
                return $true
            }
        } catch { }
        Start-Sleep -Seconds $step
    }
    Write-HistoryLine "[$((Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))] Ollama 대기 시간 초과"
    return $false
}

Write-HistoryLine "[$ts] 시작 (cwd=$Root)"

if (-not (Wait-OllamaHttp)) {
    exit 1
}

$script = Join-Path $Root "algo_problem_gen.py"
if (-not (Test-Path -LiteralPath $script)) {
    Write-HistoryLine "[$ts] 오류: algo_problem_gen.py 없음"
    exit 1
}

$run = $null
if (Get-Command python -ErrorAction SilentlyContinue) {
    $run = { & python $script --git-push }
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $run = { & py -3 $script --git-push }
}
if (-not $run) {
    Write-HistoryLine "[$ts] 오류: PATH에 python 또는 py 없음"
    exit 1
}

& $run 2>&1 | Set-Content -LiteralPath $lastLog -Encoding UTF8

$code = $LASTEXITCODE
$ts2 = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Write-HistoryLine "[$ts2] 종료 exit=$code (상세: auto_gen_last.log)"

# python 출력은 파일로만 갔을 수 있어, 푸시 여부 확인용으로 끝부분을 콘솔에도 표시
Write-Host ""
Write-Host "=== run_daily_problem_gen (exit=$code) ===" -ForegroundColor Cyan
Write-Host "전체 로그: $lastLog"
if (Test-Path -LiteralPath $lastLog) {
    Write-Host "--- 마지막 25줄 ---" -ForegroundColor DarkGray
    Get-Content -LiteralPath $lastLog -Tail 25 -Encoding UTF8
}
Write-Host "히스토리: $history" -ForegroundColor DarkGray

exit $code
