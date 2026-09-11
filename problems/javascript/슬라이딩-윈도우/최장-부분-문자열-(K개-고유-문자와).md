# 최장 부분 문자열 (K개 고유 문자와)
*javascript · 슬라이딩 윈도우 · 보통 · 문자열, 슬라이딩 윈도우, 자료구조*

## 입출력 환경

Node.js 환경에서 표준 입력을 받으며, 모든 입력은 공백으로 구분된 문자열 형태로 처리됩니다.

## 문제

문자열 $S$와 정수 $K$가 주어집니다. 문자열 $S$에서 고유한 문자의 개수가 $K$개 이하인 가장 긴 부분 문자열의 길이를 구하는 문제입니다. 부분 문자열은 연속된 문자의 집합이어야 합니다. 모든 문자는 영문 소문자('a'-'z')라고 가정합니다.

예시: S = "araawn", K = 2
"araawn"에는 고유 문자가 'a', 'r', 'w', 'n' 4개가 포함되어 있습니다.
K=2인 부분 문자열로는 "araa" (고유 문자: a, r)가 있습니다. 길이는 4입니다.

## 입력

첫 번째 줄에 문자열 S와 정수 K가 공백으로 구분되어 입력됩니다. (예: "araawn" 2)

## 출력

가장 긴 부분 문자열의 길이를 정수로 출력합니다.

## 제약 조건

문자열 S의 길이 $N$은 1부터 100,000까지입니다. $K$는 1 이상 $N$ 이하의 정수입니다.

## 예제 1

**입력**
```
"araawn" 2
```

**출력**
```
4
```

*슬라이딩 윈도우를 사용하여 'a', 'r'이 포함된 최대 길이 4인 "araa"를 찾습니다.*

## 예제 2

**입력**
```
"abcabcabc" 1
```

**출력**
```
1
```

*고유 문자가 1개인 가장 긴 부분 문자열은 'a', 'b', 'c' 중 하나이므로 길이가 1입니다.*

## 힌트

- 슬라이딩 윈도우(Sliding Window) 기법을 사용하면 효율적으로 문제를 해결할 수 있습니다.
- 현재 윈도우 내의 문자를 추적할 수 있는 빈도 맵(Frequency Map)을 활용하세요.


## 알고리즘 요약

슬라이딩 윈도우 + 맵(Map): 윈도우의 오른쪽 경계(right)를 확장하며 문자를 추가합니다. 윈도우 내 고유 문자의 개수가 $K$를 초과하면, 왼쪽 경계(left)를 이동시키며 문자를 제거하고 고유 문자의 개수를 줄여나갑니다. 매 단계마다 현재 윈도우의 길이를 최대 길이와 비교합니다.

## 풀이 해설

풀이 과정은 슬라이딩 윈도우 기법을 활용하여 $O(N)$ 시간 복잡도로 해결할 수 있습니다.

1. **초기화**: 왼쪽 포인터 `left`와 오른쪽 포인터 `right`를 0으로 설정하고, 현재 윈도우 내 문자의 빈도를 저장할 `charMap`을 초기화합니다. 최대 길이를 저장할 `maxLength`를 0으로 설정합니다.
2. **윈도우 확장 (Right Pointer)**: `right` 포인터를 문자열의 끝까지 이동시키며 문자를 윈도우에 추가합니다. `charMap`에 해당 문자를 기록하고, 고유 문자의 개수(`Map.size`)가 증가합니다.
3. **윈도우 축소 (Left Pointer)**: 만약 `charMap.size`가 주어진 제한 $K$를 초과하게 되면, 윈도우가 조건을 만족하지 못한다는 의미입니다. 이때 `left` 포인터를 이동시키며 윈도우를 축소해야 합니다. 제거되는 문자를 `charMap`에서 제거하고, 해당 문자의 빈도가 0이 되면 `charMap`에서 해당 문자를 완전히 삭제하여 고유 문자의 개수를 정확히 줄입니다.
4. **최대 길이 갱신**: 윈도우가 항상 조건을 만족하는 상태(고유 문자 개수 $\le K$)가 되므로, 현재 윈도우의 길이 (`right - left + 1`)를 계산하여 `maxLength`를 갱신합니다.
5. **종료**: `right` 포인터가 끝까지 도달하면 `maxLength`가 정답입니다.

*시간 복잡도: $O(N)$ (각 포인터는 문자열을 한 번만 순회합니다.)

## 참고 코드 (javascript)

```javascript
/**
 * Node.js 환경에서 표준 입력을 처리하기 위한 구조입니다.
 */

function solve(S, K) {
    let left = 0;
    let maxLength = 0;
    // 문자의 빈도를 저장하는 Map을 사용합니다. {문자: 횟수}
    const charMap = new Map();

    for (let right = 0; right < S.length; right++) {
        const charR = S[right];

        // 1. 윈도우 확장: 문자를 추가하고 맵에 기록
        charMap.set(charR, (charMap.get(charR) || 0) + 1);

        // 2. 윈도우 축소: 고유 문자의 개수가 K를 초과하면 왼쪽 포인터를 이동
        while (charMap.size > K) {
            const charL = S[left];
            
            // 맵에서 해당 문자의 횟수 감소
            let count = charMap.get(charL) - 1;
            charMap.set(charL, count);
            
            // 횟수가 0이 되면, 고유 문자가 아니므로 맵에서 완전히 제거
            if (count === 0) {
                charMap.delete(charL);
            }
            
            // 왼쪽 포인터 이동
            left++;
        }

        // 3. 최대 길이 갱신: 현재 윈도우의 길이는 (right - left + 1)
        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
}

// 표준 입력 처리 예시 (실제 코딩테스트 환경에 맞춰 구현)
function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
        terminal: false
    });

    rl.on('line', (line) => {
        if (!line) return;
        
        // 입력 형식: "문자열" K
        const parts = line.trim().split(/\s+/);
        if (parts.length < 2) return;

        // 문자열 S는 따옴표로 감싸져 올 수 있으므로, 첫 번째 요소를 정리합니다.
        let S = parts[0].startsWith(""') ? parts[0].slice(1, -1) : parts[0];
        const K = parseInt(parts[1]);

        const result = solve(S, K);
        console.log(result);
        rl.close();
    });
}

main();
```
