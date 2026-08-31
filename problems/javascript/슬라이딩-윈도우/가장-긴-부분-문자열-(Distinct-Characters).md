# 가장 긴 부분 문자열 (Distinct Characters)
*javascript · 슬라이딩 윈도우 · 보통 · 문자열, 슬라이딩 윈도우, 해시맵*

## 입출력 환경

Node.js 환경에서 표준 입력을 통해 'S K' 형태의 문자열을 받습니다. (예: process.stdin.on('data', ...))

## 문제

주어진 문자열 `S`와 정수 `K`가 있습니다. 문자열 `S`에서 포함된 서로 다른 문자의 종류가 K 이하인 가장 긴 부분 문자열의 길이를 구하는 문제입니다.

부분 문자열은 연속된 문자의 집합입니다.

## 입력

첫 번째 줄에 문자열 S와 정수 K가 공백으로 구분되어 한 줄에 입력됩니다. (예: "araac 2")

## 출력

찾은 가장 긴 부분 문자열의 길이(정수)를 출력합니다.

## 제약 조건

S의 길이 N은 1부터 10^5까지입니다. K는 1부터 26까지의 정수입니다. 시간 복잡도는 O(N)에 가까워야 합니다.

## 예제 1

**입력**
```
araac 2
```

**출력**
```
4
```

*부분 문자열 'araa'는 'a'와 'r' 두 종류의 문자를 가지며, 길이가 4입니다.*

## 예제 2

**입력**
```
abcabc 3
```

**출력**
```
6
```

*문자열 전체 'abcabc'는 'a', 'b', 'c' 세 종류의 문자를 가지며, 최대 길이 6입니다.*

## 예제 3

**입력**
```
bbbbbbbbbb 1
```

**출력**
```
11
```

*모두 같은 문자이므로, 전체 문자열이 최대 부분 문자열입니다.*

## 힌트

- 슬라이딩 윈도우 기법을 사용합니다. (Window = [left, right])
- 현재 윈도우 내에 몇 종류의 문자가 있는지 카운트할 수 있는 자료구조(예: Map)를 유지하세요.


## 알고리즘 요약

슬라이딩 윈도우 (Sliding Window) 기법을 활용합니다. 윈도우의 오른쪽 경계(right)를 확장하면서 현재 윈도우 내의 고유 문자 개수를 체크하고, 이 개수가 K를 초과하면 왼쪽 경계(left)를 이동시켜 고유 문자 개수를 다시 K 이하로 맞춥니다. 매 단계마다 현재 윈도우의 길이를 최대 길이와 비교하여 갱신합니다.

## 풀이 해설

풀이 아이디어:
이 문제는 '가장 긴 연속 부분'을 찾는 전형적인 슬라이딩 윈도우 문제입니다. 윈도우의 오른쪽 끝(right)을 한 칸씩 전진시키며 윈도우를 확장합니다. 이때, 윈도우 내의 고유 문자 개수를 카운트하는 맵(Map)을 사용합니다. 

단계별 풀이:
1. 초기화: `left` 포인터와 `max_length`를 0으로 설정하고, 빈 빈도 맵(charCount)을 준비합니다.
2. 윈도우 확장 (right 포인터 이동): `right`를 0부터 N-1까지 증가시키면서 `S[right]` 문자를 `charCount`에 추가하고 빈도를 1 증가시킵니다.
3. 윈도우 축소 (left 포인터 이동): `charCount`의 키(key) 개수(즉, 고유 문자 개수)가 K보다 커지는 순간이 발생하면, 이 조건을 만족할 때까지 `left` 포인터를 이동시켜야 합니다. `S[left]` 문자를 `charCount`에서 제거하고 빈도를 1 감소시킵니다. 만약 빈도가 0이 되면, 해당 문자는 맵에서 완전히 삭제합니다.
4. 길이 갱신: 윈도우가 유효(고유 문자 <= K)한 상태가 될 때마다, 현재 윈도우의 길이(`right - left + 1`)를 `max_length`와 비교하여 최대값을 갱신합니다.
5. 반복: 모든 `right` 포인터 이동이 끝날 때까지 2~4단계를 반복합니다.

시간 복잡도: 각 포인터(left와 right)는 문자열의 길이에 비례하여 최대 한 번만 이동하므로, 시간 복잡도는 O(N)입니다.

## 참고 코드 (javascript)

```javascript
/**
 * @param {string} S - 입력 문자열
 * @param {number} K - 허용되는 고유 문자 개수
 * @returns {number} - 최대 부분 문자열 길이
 */
function solve(S, K) {
    let left = 0;
    let maxLength = 0;
    // 각 문자의 빈도를 저장하는 맵
    const charCount = new Map();

    for (let right = 0; right < S.length; right++) {
        const charR = S[right];
        
        // 1. 윈도우 확장: 오른쪽 포인터 이동
        // 빈도수를 증가시키고 맵에 추가합니다.
        charCount.set(charR, (charCount.get(charR) || 0) + 1);

        // 2. 윈도우 축소: 고유 문자 개수가 K를 초과하면 왼쪽 포인터 이동
        // Map.size는 현재 윈도우의 고유 문자 개수입니다.
        while (charCount.size > K) {
            const charL = S[left];
            
            // 왼쪽 문자의 빈도수 감소
            let count = charCount.get(charL) - 1;
            charCount.set(charL, count);

            // 빈도가 0이 되면 맵에서 완전히 제거하여 고유 문자 개수를 정확히 관리
            if (count === 0) {
                charCount.delete(charL);
            }
            
            // 왼쪽 포인터 이동
            left++;
        }

        // 3. 최대 길이 갱신: 현재 윈도우는 항상 유효함 (고유 문자 <= K)
        // 현재 길이 = right - left + 1
        maxLength = Math.max(maxLength, right - left + 1);
    }
    
    return maxLength;
}

// Node.js 환경에서 표준 입력을 처리하는 로직
function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
        terminal: false
    });

    rl.on('line', (line) => {
        if (!line.trim()) return;
        
        // 입력 형식: "S K"
        const parts = line.trim().split(' ');
        if (parts.length !== 2) return;

        const S = parts[0];
        const K = parseInt(parts[1], 10);
        
        const result = solve(S, K);
        console.log(result);
        
        rl.close();
    });
}

main();
```
