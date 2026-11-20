# 최대 K개 고유 문자를 가진 가장 긴 부분 문자열
*javascript · 슬라이딩 윈도우 · 보통 · 슬라이딩 윈도우, 해시맵, 문자열*

## 입출력 환경

Node.js 환경에서 표준 입력(stdin)을 사용하며, 전체 입력을 한 번에 읽어 처리하는 것이 효율적입니다.

## 문제

문자열 S와 정수 K가 주어집니다. 문자열 S의 부분 문자열 중에서 고유한(distinct) 문자의 개수가 K개 이하인 가장 긴 부분 문자열의 길이를 구하세요. 

부분 문자열은 연속된 문자들로 이루어져야 하며, 전체 문자열 S의 부분 문자열만 고려합니다.

예시: S = "araac", K = 2
부분 문자열 "araa"는 고유 문자가 'a'와 'r' 두 개이므로 조건을 만족합니다. 길이는 4입니다. 이보다 더 긴 부분 문자열은 고유 문자가 3개 이상일 수 있습니다.
따라서 정답은 4입니다.

## 입력

첫 번째 줄에 문자열 S와 정수 K가 공백으로 구분되어 한 줄에 입력됩니다. (예: "araac" 2)

## 출력

정수 하나를 출력합니다. (가장 긴 부분 문자열의 길이)

## 제약 조건

문자열 S의 길이는 1부터 10^5까지입니다. K는 1부터 26까지의 정수입니다. 시간 복잡도는 O(N) 또는 O(N log N) 이내여야 합니다.

## 예제 1

**입력**
```
"araac" 2
```

**출력**
```
4
```

*부분 문자열 "araa"는 고유 문자가 'a', 'r'로 2개이므로 조건을 만족하며, 길이가 4로 가장 깁니다.*

## 예제 2

**입력**
```
"aabbcc" 1
```

**출력**
```
2
```

*고유 문자가 1개인 가장 긴 부분 문자열은 "aa", "bb", "cc" 등이며, 길이는 2입니다.*

## 예제 3

**입력**
```
"abcde" 5
```

**출력**
```
5
```

*전체 문자열 자체가 5개의 고유 문자를 가지므로, 최대 길이가 5입니다.*

## 힌트

- 슬라이딩 윈도우 기법을 사용하세요. 두 개의 포인터(left, right)를 활용하는 것이 핵심입니다.
- 현재 윈도우 내의 문자의 고유 개수를 효율적으로 추적할 자료구조(예: HashMap 또는 빈도 배열)를 사용하세요.


## 알고리즘 요약

슬라이딩 윈도우 (Sliding Window) + 해시맵 (HashMap).

## 풀이 해설

### 💡 아이디어: 슬라이딩 윈도우
이 문제는 '최대 K개 고유 문자를 가진 가장 긴 부분 문자열'을 찾는 전형적인 슬라이딩 윈도우 문제입니다. 윈도우의 오른쪽 끝(right 포인터)을 한 칸씩 전진시키면서 윈도우를 확장합니다. 윈도우가 조건을 위반할 경우(고유 문자가 K를 초과하는 경우), 윈도우의 왼쪽 끝(left 포인터)을 전진시켜 조건을 만족시킬 때까지 윈도우를 축소합니다.

### ⚙️ 단계별 풀이
1. **초기화:** `left` 포인터와 `right` 포인터, 그리고 현재 윈도우 내 문자의 빈도를 저장할 `Map`을 초기화합니다. 최대 길이(`maxLength`)를 0으로 설정합니다.
2. **윈도우 확장 (Right 포인터 이동):** `right` 포인터를 문자열의 끝까지 이동시키며 현재 문자를 윈도우에 추가하고, `Map`에 해당 문자의 빈도를 증가시킵니다.
3. **조건 확인 및 윈도우 축소 (Left 포인터 이동):** 현재 윈도우 내의 고유 문자 개수(`Map.size`)가 K를 초과하는지 확인합니다. 만약 초과한다면, `left` 포인터를 이동시키면서 윈도우를 축소합니다. 축소할 때마다, `Map`에서 `left`가 가리키는 문자의 빈도를 감소시키고, 빈도가 0이 되면 `Map`에서 해당 문자를 제거합니다.
4. **최대 길이 갱신:** 윈도우가 항상 조건을 만족하는 상태일 때마다, 현재 윈도우의 길이(`right - left + 1`)를 계산하여 `maxLength`를 갱신합니다.
5. **반복:** `right` 포인터가 끝에 도달할 때까지 2~4단계를 반복하고, 최종 `maxLength`를 반환합니다.

### ⏱️ 시간 복잡도
`left` 포인터와 `right` 포인터는 각각 문자열의 시작부터 끝까지 최대 한 번만 이동합니다. 따라서 시간 복잡도는 O(N)입니다. (N은 문자열의 길이)

## 참고 코드 (javascript)

```javascript
/**
 * Node.js 환경에서 표준 입력을 읽어 처리하는 함수입니다.
 * @param {string} S - 입력 문자열
 * @param {number} K - 최대 고유 문자 개수
 * @returns {number} - 가장 긴 부분 문자열의 길이
 */
function solve(S, K) {
    // Map을 사용하여 현재 윈도우 내 문자의 빈도를 저장합니다.
    const charFrequency = new Map();
    let left = 0;
    let maxLength = 0;

    for (let right = 0; right < S.length; right++) {
        const charRight = S[right];
        
        // 1. 윈도우 확장: 오른쪽 문자를 추가하고 빈도를 증가시킵니다.
        charFrequency.set(charRight, (charFrequency.get(charRight) || 0) + 1);

        // 2. 조건 확인 및 윈도우 축소: 고유 문자가 K를 초과하면 left를 이동시킵니다.
        while (charFrequency.size > K) {
            const charLeft = S[left];
            
            // 왼쪽 문자의 빈도를 감소시킵니다.
            let count = charFrequency.get(charLeft) - 1;
            charFrequency.set(charLeft, count);
            
            // 빈도가 0이 되면 Map에서 제거하여 고유 문자 개수를 줄입니다.
            if (count === 0) {
                charFrequency.delete(charLeft);
            }
            
            // left 포인터를 오른쪽으로 이동시킵니다.
            left++;
        }

        // 3. 최대 길이 갱신: 현재 윈도우 [left, right]의 길이를 계산하여 갱신합니다.
        // 이 시점에서는 윈도우가 항상 조건을 만족합니다.
        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
}

// --- 입출력 처리 (Node.js 표준 입력) ---

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

rl.on('line', (line) => {
    if (!line) return;
    
    // 입력 형식: "문자열" K (예: "araac" 2)
    const parts = line.trim().split(' ');
    
    // 첫 번째 요소가 문자열 S, 두 번째 요소가 숫자 K입니다.
    const S = parts[0].replace(/"/g, ''); // 따옴표 제거
    const K = parseInt(parts[1]);
    
    if (!isNaN(K)) {
        const result = solve(S, K);
        console.log(result);
    }
});
```
