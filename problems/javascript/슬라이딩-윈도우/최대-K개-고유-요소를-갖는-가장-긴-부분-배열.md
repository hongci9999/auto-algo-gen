# 최대 K개 고유 요소를 갖는 가장 긴 부분 배열
*javascript · 슬라이딩 윈도우 · 보통 · 슬라이딩 윈도우, 자료구조, 배열*

## 입출력 환경

Node.js 환경에서 표준 입력을 사용합니다. 일반적으로 readline 모듈이나 fs.readFileSync를 사용하여 전체 입력을 받은 후 파싱합니다.

## 문제

주어진 정수 배열 `arr`과 정수 `K`가 있습니다. 배열 `arr`의 부분 배열 중, 고유한 요소(distinct elements)의 개수가 최대 `K`개 이하인 가장 긴 부분 배열의 길이를 구하는 문제입니다.

부분 배열의 길이는 1 이상이며, 배열의 전체 길이보다 클 수 없습니다.

예시: arr = [1, 2, 1, 3, 1], K = 2
부분 배열 [1, 2, 1]은 고유 요소가 {1, 2}로 2개입니다. 길이는 3입니다.
부분 배열 [2, 1, 3]은 고유 요소가 {1, 2, 3}로 3개입니다. (K=2이므로 조건 불만족)
가장 긴 부분 배열의 길이는 3입니다.

## 입력

첫 번째 줄에 정수 N과 정수 K가 공백으로 구분되어 주어집니다. 두 번째 줄부터 N개의 정수 원소가 공백으로 구분되어 주어집니다.

## 출력

가장 긴 부분 배열의 길이(정수)를 출력합니다.

## 제약 조건

1 <= N <= 100,000
1 <= K <= N
0 <= arr[i] <= 100,000
시간 복잡도는 O(N) 또는 O(N log N) 이하를 목표로 합니다.

## 예제 1

**입력**
```
5 2
1 2 1 3 1
```

**출력**
```
3
```

*부분 배열 [1, 2, 1] 또는 [1, 3, 1] 등이 가장 길며, 고유 요소는 2개입니다.*

## 예제 2

**입력**
```
4 1
5 5 5 5
```

**출력**
```
4
```

*모든 요소가 5로 고유 요소가 1개이므로, 전체 배열이 가장 깁니다.*

## 예제 3

**입력**
```
3 1
1 2 3
```

**출력**
```
1
```

*K=1이므로, 고유 요소가 1개인 가장 긴 부분 배열은 [1], [2], [3] 중 하나이며 길이는 1입니다.*

## 힌트

- 이 문제는 '슬라이딩 윈도우(Sliding Window)' 기법을 사용하여 O(N) 시간 복잡도로 해결할 수 있습니다.
- 현재 윈도우 내의 고유 요소의 개수를 효율적으로 추적하는 자료구조(예: Map 또는 빈도 배열)를 사용하세요.


## 알고리즘 요약

슬라이딩 윈도우 (Sliding Window) + 해시맵 (Hash Map)

## 풀이 해설

아이디어:
이 문제는 '최대 K개 고유 요소'라는 제약 조건을 만족하는 가장 긴 구간을 찾는 전형적인 슬라이딩 윈도우 문제입니다. 윈도우를 오른쪽으로 확장(right 포인터 이동)하면서 조건을 만족하는지 확인하고, 조건을 위반하면 왼쪽으로 축소(left 포인터 이동)하여 조건을 만족시킬 때까지 조정합니다.

단계:
1. 초기화: `left` 포인터와 `right` 포인터는 0에서 시작합니다. `max_length`를 0으로 초기화합니다. 윈도우 내의 요소 빈도수를 저장할 `frequencyMap`을 사용합니다.
2. 윈도우 확장 (Right 이동): `right` 포인터를 0부터 N-1까지 이동시키며 `arr[right]`를 `frequencyMap`에 추가하고 카운트를 증가시킵니다.
3. 조건 검사 및 축소 (Left 이동): 현재 `frequencyMap`에 저장된 고유 요소의 개수(즉, `Map.size`)가 `K`를 초과하는지 확인합니다. 만약 초과한다면, `left` 포인터를 증가시키면서 `arr[left]`를 `frequencyMap`에서 제거하고 카운트를 감소시킵니다. 이 과정을 고유 요소 개수가 다시 K 이하가 될 때까지 반복합니다.
4. 길이 갱신: 윈도우가 조건을 만족할 때마다, 현재 윈도우의 길이 (`right - left + 1`)를 계산하여 `max_length`와 비교해 더 큰 값을 갱신합니다.
5. 종료: `right` 포인터가 끝까지 이동하면 `max_length`가 답이 됩니다.

시간 복잡도: `left`와 `right` 포인터가 각각 배열을 한 번씩만 순회하므로, 시간 복잡도는 O(N)입니다. 공간 복잡도는 최악의 경우 모든 고유 요소가 존재할 때 O(min(N, V))입니다 (V는 값의 범위).

## 참고 코드 (javascript)

```javascript
/**
 * @param {number[]} arr - 입력 배열
 * @param {number} K - 최대 고유 요소 개수
 * @returns {number} - 가장 긴 부분 배열의 길이
 */
function longestSubarrayWithKDistinct(arr, K) {
    if (arr.length === 0) return 0;

    // Map을 사용하여 현재 윈도우 내 요소의 빈도수를 저장합니다.
    const frequencyMap = new Map();
    let left = 0;
    let maxLength = 0;

    for (let right = 0; right < arr.length; right++) {
        const element = arr[right];

        // 1. 윈도우 확장: 현재 요소를 맵에 추가하고 카운트를 증가시킵니다.
        if (!frequencyMap.has(element)) {
            frequencyMap.set(element, 0);
        }
        frequencyMap.set(element, frequencyMap.get(element) + 1);

        // 2. 조건 검사 및 윈도우 축소: 고유 요소 개수가 K를 초과하면 left를 이동시킵니다.
        while (frequencyMap.size > K) {
            const leftElement = arr[left];
            
            // left 요소를 맵에서 제거합니다.
            let count = frequencyMap.get(leftElement) - 1;
            frequencyMap.set(leftElement, count);
            
            // 카운트가 0이 되면 맵에서 완전히 제거하여 고유 요소 개수를 정확히 반영합니다.
            if (count === 0) {
                frequencyMap.delete(leftElement);
            }
            
            // left 포인터를 오른쪽으로 이동시킵니다.
            left++;
        }

        // 3. 길이 갱신: 현재 윈도우 [left, right]는 조건을 만족합니다.
        const currentLength = right - left + 1;
        maxLength = Math.max(maxLength, currentLength);
    }

    return maxLength;
}

// --- Node.js 환경을 위한 입출력 처리 예시 ---

/**
 * 실제 테스트 환경에서 이 함수를 사용합니다.
 * 입력 형식: N K\narr[0] arr[1] ... arr[N-1]
 */
function solve() {
    const fs = require('fs');
    // 표준 입력 전체를 읽어옵니다.
    const input = fs.readFileSync(0, 'utf8').trim().split('\n');
    
    if (input.length < 2) return;

    // 첫 줄: N K
    const [N_str, K_str] = input[0].trim().split(' ');
    const N = parseInt(N_str);
    const K = parseInt(K_str);

    // 두 번째 줄: 배열 원소들
    const arr = input[1].trim().split(' ').map(Number);

    const result = longestSubarrayWithKDistinct(arr, K);
    console.log(result);
}

// solve(); // 주석 처리: 테스트 환경에 맞게 사용자가 주석을 해제하도록 유도
```
