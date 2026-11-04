# 문자열에서 K개 문자로 이루어진 가장 긴 부분 문자열
*javascript · 슬라이딩 윈도우 · 보통 · 문자열, 슬라이딩 윈도우, 자료구조*

## 입출력 환경

Node.js 환경에서 표준 입력을 통해 'S K' 형태의 문자열을 받습니다. 예시: process.stdin.on('data', (data) => { ... });

## 문제

당신에게 알파벳으로만 이루어진 문자열 $S$와 정수 $K$가 주어집니다. 

$S$의 부분 문자열 중, 포함된 서로 다른 문자의 종류가 $K$개 이하인 가장 긴 부분 문자열의 길이를 구하는 문제입니다.

예시: 문자열 "araac", $K=2$일 때, "araa"는 'a'와 'r' 두 종류의 문자로 이루어져 있으며, 길이가 4입니다. 가장 긴 부분 문자열의 길이는 4입니다.

## 입력

첫째 줄에 문자열 $S$와 정수 $K$가 공백으로 구분되어 주어집니다. (예: "araac" 2)

## 출력

가장 긴 부분 문자열의 길이를 하나의 정수로 출력합니다.

## 제약 조건

문자열 $S$의 길이는 1부터 100,000까지입니다. $K$는 1부터 26까지의 정수입니다. 시간 복잡도는 $O(N)$을 목표로 합니다.

## 예제 1

**입력**
```
"araac" 2
```

**출력**
```
4
```

*슬라이딩 윈도우를 사용하여 'a'와 'r'만 포함하는 가장 긴 부분 문자열 'araa'의 길이를 찾습니다.*

## 예제 2

**입력**
```
"abcabcabc" 3
```

**출력**
```
9
```

*문자열 전체가 3개 문자로 이루어져 있으므로 길이가 9입니다.*

## 예제 3

**입력**
```
"bbbbbb" 1
```

**출력**
```
6
```

*모든 문자가 동일하므로 전체 길이가 가장 깁니다.*

## 힌트

- 슬라이딩 윈도우(Sliding Window) 기법을 사용하면 시간 복잡도를 최적화할 수 있습니다.
- 현재 윈도우(부분 문자열) 내에 포함된 문자의 종류를 효율적으로 세는 자료구조가 필요합니다.


## 알고리즘 요약

슬라이딩 윈도우 + 빈도 맵 (Frequency Map)

## 풀이 해설

이 문제는 슬라이딩 윈도우 기법을 사용하여 $O(N)$ 시간 복잡도로 해결할 수 있습니다.

**아이디어:**
두 개의 포인터, `left` (윈도우 시작)와 `right` (윈도우 끝)를 사용하며, 윈도우가 항상 유효한 상태(즉, 포함된 고유 문자의 개수가 $K$개 이하)를 유지하도록 만듭니다.

**단계:**
1. **초기화:** `left = 0`, `maxLength = 0`, 그리고 문자의 빈도를 저장할 `charCount` 맵(Map)을 초기화합니다.
2. **윈도우 확장 (Right 포인터 이동):** `right` 포인터를 문자열 끝까지 한 칸씩 이동시키면서, `S[right]` 문자를 `charCount`에 추가하고 해당 문자의 빈도를 증가시킵니다.
3. **조건 검사 및 윈도우 축소 (Left 포인터 이동):** 현재 윈도우 `[left, right]`에 포함된 고유 문자의 개수(즉, `charCount` 맵의 크기)가 $K$를 초과하는지 확인합니다. 만약 초과한다면, 윈도우가 유효하지 않다는 뜻이므로, `left` 포인터를 오른쪽으로 이동시키고, `S[left]` 문자의 빈도를 `charCount`에서 감소시킵니다. 만약 이 감소로 인해 해당 문자의 빈도가 0이 되면, `charCount`에서 해당 문자를 완전히 제거합니다.
4. **최대 길이 갱신:** 윈도우가 유효한 상태가 될 때마다 (즉, 고유 문자의 개수가 $K$ 이하일 때마다), 현재 윈도우의 길이 (`right - left + 1`)를 계산하여 `maxLength`와 비교하고 최댓값으로 갱신합니다.
5. **종료:** `right` 포인터가 끝에 도달하면, `maxLength`가 최종 답이 됩니다.

**시간 복잡도:** `left`와 `right` 포인터는 각각 문자열의 길이를 넘지 않으며, 각 문자는 최대 한 번만 맵에 추가되고 제거됩니다. 따라서 시간 복잡도는 $O(N)$입니다. 공간 복잡도는 $O(|	ext{Alphabet}|)$로, 알파벳 크기(26)에 비례합니다.

## 참고 코드 (javascript)

```javascript
/**
 * @param {string} S - 입력 문자열
 * @param {number} K - 허용되는 고유 문자의 종류
 * @returns {number} 가장 긴 부분 문자열의 길이
 */
function solve(S, K) {
    let left = 0;
    let maxLength = 0;
    // charCount: {문자: 빈도수} 형태의 맵 사용
    const charCount = new Map();

    for (let right = 0; right < S.length; right++) {
        const charR = S[right];
        
        // 1. 윈도우 확장: right 포인터 이동
        charCount.set(charR, (charCount.get(charR) || 0) + 1);

        // 2. 조건 검사 및 윈도우 축소: 고유 문자가 K를 초과하면 left 이동
        while (charCount.size > K) {
            const charL = S[left];
            
            // 윈도우에서 charL 제거
            let count = charCount.get(charL) - 1;
            charCount.set(charL, count);

            if (count === 0) {
                charCount.delete(charL);
            }
            
            left++;
        }

        // 3. 최대 길이 갱신: 현재 윈도우는 항상 유효함
        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
}

// Node.js 표준 입력 처리 예시
function main() {
    // Node.js 환경에서 모든 입력 라인을 처리하기 위한 구조
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
        terminal: false
    });

    rl.on('line', (line) => {
        if (!line.trim()) return;
        
        // 입력 형식: "S" K
        // 문자열 S가 따옴표로 감싸져 있을 수 있으므로 이를 처리
        const parts = line.trim().split(/\s+/); 
        // 첫 번째 요소에서 따옴표 제거
        const S = parts[0].replace(/"/g, ''); 
        const K = parseInt(parts[1]);
        
        const result = solve(S, K);
        console.log(result);
        rl.close();
    });
}

main();
```
