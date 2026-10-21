# 최대 합 K 이하의 부분 배열 길이
*javascript · 슬라이딩 윈도우 · 보통 · 배열, 슬라이딩 윈도우*

## 입출력 환경

Node.js 환경에서 표준 입력을 사용합니다. 모든 입력은 한 번에 받아서 처리한다고 가정합니다.

## 문제

정수 배열 `arr`과 정수 `K`가 주어집니다. 배열 `arr`에서 연속하는 부분 배열 중, 합이 `K`를 넘지 않는 가장 긴 길이(최대 길이)를 구하세요. 부분 배열의 길이가 1부터 N까지 가능하며, 합이 K를 초과하는 부분 배열은 최대 길이 계산에서 제외합니다.

예시: arr = [1, 2, 3], K = 5
부분 배열 [1, 2]의 합은 3, 길이 2. (<= 5)
부분 배열 [1, 2, 3]의 합은 6. (> 5)
따라서 최대 길이는 2입니다.

## 입력

첫 번째 줄에 정수 N과 정수 K가 공백으로 구분되어 입력됩니다. 두 번째 줄에 N개의 정수 원소가 공백으로 구분되어 입력됩니다.

## 출력

최대 길이(정수)를 출력합니다.

## 제약 조건

1. 1 <= N <= 100,000
2. -10^4 <= arr[i] <= 10^4
3. -10^9 <= K <= 10^9
4. 시간 복잡도는 O(N) 또는 O(N log N) 이내여야 합니다.

## 예제 1

**입력**
```
3 5
1 2 3
```

**출력**
```
2
```

*부분 배열 [1, 2]의 합은 3으로, 5 이하이며 길이가 최대입니다.*

## 예제 2

**입력**
```
5 10
2 3 1 4 1
```

**출력**
```
4
```

*부분 배열 [2, 3, 1, 4]의 합은 10으로, K를 초과하지 않으며 최대 길이입니다.*

## 예제 3

**입력**
```
4 1
10 20 30 40
```

**출력**
```
0
```

*모든 원소의 값이 K보다 크므로, 길이가 0입니다.*

## 힌트

- 부분 배열의 합을 계산할 때, 모든 가능한 부분 배열을 확인하는 것은 시간 초과를 유발할 수 있습니다.
- 현재 합이 K를 초과하게 되면, 윈도우의 시작 지점을 이동시키면서 합을 줄여나가는 기법을 사용해 보세요.


## 알고리즘 요약

슬라이딩 윈도우 (Sliding Window) 기법을 사용합니다. 두 포인터(left, right)를 설정하여 현재 윈도우의 합을 유지하고, 합이 K를 초과할 때만 left 포인터를 이동시켜 윈도우를 축소합니다. 이때, 현재 윈도우의 길이를 최대값과 비교하며 갱신합니다.

## 풀이 해설

아이디어: 이 문제는 '가장 긴 연속 부분 배열'을 찾는 전형적인 슬라이딩 윈도우(Sliding Window) 문제입니다. 배열의 모든 부분 배열을 탐색하는 것은 시간 복잡도가 O(N^2)이 되어 시간 제한을 초과할 수 있습니다. 따라서, 현재 윈도우의 합(Sum)을 효율적으로 관리하며 포인터를 이동시키는 방식을 사용해야 합니다.

단계:
1. 초기화: `left` 포인터(윈도우 시작)를 0으로, `currentSum`을 0으로, `maxLength`를 0으로 설정합니다.
2. 확장 (Right 포인터 이동): `right` 포인터를 0부터 N-1까지 순회하며 배열의 원소 `arr[right]`를 `currentSum`에 더합니다. (윈도우를 확장)
3. 수축 (Left 포인터 조정): 만약 `currentSum`이 `K`보다 커지면, 윈도우가 너무 커진 것입니다. 이 경우, `left` 포인터에 해당하는 원소 `arr[left]`를 `currentSum`에서 빼고, `left` 포인터를 1 증가시킵니다. 이 과정을 `currentSum <= K`가 될 때까지 반복합니다. (윈도우를 축소)
4. 최대 길이 갱신: `currentSum <= K`인 상태가 되면, 현재 윈도우의 길이(`right - left + 1`)를 계산하고, 이를 `maxLength`와 비교하여 더 큰 값으로 갱신합니다.
5. 반복: 모든 `right` 포인터가 끝날 때까지 2~4단계를 반복한 후, `maxLength`를 반환합니다.

시간 복잡도: 각 원소는 `right` 포인터에 의해 한 번, 그리고 `left` 포인터에 의해 최대 한 번만 합산/제거됩니다. 따라서 시간 복잡도는 O(N)입니다.

## 참고 코드 (javascript)

```javascript
/**
 * @param {number[]} arr - 정수 배열
 * @param {number} K - 최대 합치
 * @returns {number} - 최대 길이
 */
function maxLenSubarray(arr, K) {
    let left = 0; // 윈도우 시작 포인터
    let currentSum = 0;
    let maxLength = 0;
    const N = arr.length;

    for (let right = 0; right < N; right++) {
        // 1. 윈도우 확장: right 포인터 이동
        currentSum += arr[right];

        // 2. 윈도우 수축: 합이 K를 초과하면 left 포인터 이동
        while (currentSum > K && left <= right) {
            currentSum -= arr[left];
            left++;
        }

        // 3. 최대 길이 갱신: 현재 윈도우의 합이 K 이하일 때만 길이를 갱신
        // left가 right보다 커진 경우는 (모든 원소를 제거한 경우) 길이 0이 되므로, 
        // length는 right - left + 1 입니다.
        if (left <= right) {
             maxLength = Math.max(maxLength, right - left + 1);
        }
    }
    return maxLength;
}

// Node.js 환경을 위한 입력 처리 예시
function solve() {
    const fs = require('fs');
    // 표준 입력 전체를 동기적으로 읽어옵니다.
    const input = fs.readFileSync(0, 'utf8').trim().split('\n');

    if (input.length < 2) return;
    
    // 첫 줄: N과 K
    const nkLine = input[0].trim().split(' ').map(Number);
    const N = nkLine[0];
    const K = nkLine[1];

    // 두 번째 줄: 배열 arr
    const arr = input[1].trim().split(' ').map(Number);

    const result = maxLenSubarray(arr, K);
    console.log(result);
}

// solve(); // 실제 제출 시 주석 해제
```
