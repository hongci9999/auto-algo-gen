# K를 넘지 않는 가장 긴 부분 배열
*javascript · 슬라이딩 윈도우 · 보통 · 슬라이딩 윈도우, 배열*

## 입출력 환경

Node.js 환경에서 입력을 처리할 때는 전체 입력을 읽어 배열과 K 값을 분리하여 사용하는 것이 효율적입니다.

## 문제

정수 배열 `arr`과 양의 정수 `K`가 주어집니다. 당신의 목표는 배열 `arr` 내에서 합이 `K`를 초과하지 않는 가장 긴 연속 부분 배열의 길이를 찾는 것입니다. 배열의 모든 원소는 양수입니다.

예를 들어, arr = [1, 2, 3], K = 3인 경우, 부분 배열 [1, 2]의 합은 3으로 K를 초과하지 않으며, 길이는 2입니다. 이 문제는 이와 같은 최대 길이를 반환해야 합니다.

## 입력

첫 번째 줄에 정수 K가 주어집니다. 두 번째 줄에 공백으로 구분된 정수 배열 arr의 원소들이 주어집니다.

## 출력

가장 긴 부분 배열의 길이(정수)를 한 줄로 출력합니다.

## 제약 조건

1 <= K <= 10^9
1 <= N <= 10^5 (N은 배열의 원소 개수)
1 <= arr[i] <= 10^9
시간 복잡도는 O(N)을 목표로 합니다.

## 예제 1

**입력**
```
15
10 5 2 7 1 9
```

**출력**
```
4
```

*부분 배열 [5, 2, 7, 1]의 합은 15로, K를 초과하지 않으며 가장 긴 길이입니다.*

## 예제 2

**입력**
```
3
1 2 3
```

**출력**
```
2
```

*부분 배열 [1, 2]의 합은 3입니다. 길이가 3인 [1, 2, 3]은 합이 6이므로 제외됩니다.*

## 예제 3

**입력**
```
100
1 1 1 1 1
```

**출력**
```
5
```

*모든 원소를 포함하는 부분 배열의 합이 5로, K(100)보다 작으므로 길이가 5입니다.*

## 힌트

- 문제를 '슬라이딩 윈도우(Sliding Window)' 기법으로 접근하는 것이 효율적입니다.
- 두 개의 포인터(시작점과 끝점)를 사용하여 현재 부분 배열의 합을 관리해야 합니다.


## 알고리즘 요약

슬라이딩 윈도우 (Two Pointers)

## 풀이 해설

아이디어: 이 문제는 '합이 K를 넘지 않는 가장 긴 구간'을 찾는 문제입니다. 모든 원소가 양수이기 때문에, 구간의 길이가 길어질수록 합은 무조건 증가한다는 성질을 이용할 수 있습니다. 따라서 슬라이딩 윈도우 기법을 사용합니다.

단계:
1. 두 포인터 `start` (윈도우 시작)와 `end` (윈도우 끝)를 0으로 초기화하고, 현재 합 `currentSum`을 0으로 초기화합니다.
2. `end` 포인터를 배열의 끝까지 이동시키면서 `currentSum`에 `arr[end]`를 계속 더합니다. (윈도우 확장)
3. 만약 `currentSum`이 `K`를 초과하게 되면, 윈도우가 너무 커진 것입니다. 이 경우, `start` 포인터를 전진시키면서 `currentSum`에서 `arr[start]`를 빼줍니다. 이 과정을 `currentSum`이 다시 `K` 이하가 될 때까지 반복합니다. (윈도우 축소)
4. `currentSum`이 항상 `K` 이하를 유지하는 상태이므로, 매 단계마다 현재 윈도우의 길이(`end - start + 1`)를 계산하여 이전에 기록된 최대 길이(`maxLength`)와 비교하고 갱신합니다.
5. `end` 포인터가 배열 끝까지 도달하면 `maxLength`를 반환합니다.

시간 복잡도: O(N). `end` 포인터는 N번 이동하고, `start` 포인터 역시 최대 N번 이동합니다. 따라서 전체 시간 복잡도는 선형 시간인 O(N)입니다.

## 참고 코드 (javascript)

```javascript
/**
 * Node.js 환경에서 표준 입력을 처리하여 문제를 해결하는 함수
 * @param {number[]} arr - 입력 배열
 * @param {number} K - 최대 허용 합
 * @returns {number} - 최대 길이
 */
function solveSlidingWindow(arr, K) {
    let start = 0;       // 윈도우 시작 포인터
    let currentSum = 0;  // 현재 윈도우의 합
    let maxLength = 0;   // 찾은 최대 길이

    // end 포인터를 배열의 끝까지 이동시키면서 윈도우를 확장
    for (let end = 0; end < arr.length; end++) {
        currentSum += arr[end];

        // 1. 윈도우가 너무 커져서 합이 K를 초과하면, start 포인터를 이동시키며 윈도우 축소
        while (currentSum > K) {
            // start 위치의 원소를 합에서 <0xEB><0xBA><0x8C>
            currentSum -= arr[start];
            // start 포인터 전진
            start++;
        }

        // 2. 현재 윈도우의 길이가 최대 길이보다 길면 갱신
        // 현재 길이 = end - start + 1
        maxLength = Math.max(maxLength, end - start + 1);
    }

    return maxLength;
}

// =========================================================================
// I/O 처리 부분 (실제 환경에 맞게 수정 필요)
// =========================================================================

// Node.js 환경에서 모든 입력을 읽는 표준 방식 예시 (전체 입력이 한 번에 들어올 경우)

/*
const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\n');

if (input.length >= 2) {
    const K = parseInt(input[0].trim(), 10);
    const arr = input[1].trim().split(' ').map(Number);
    console.log(solveSlidingWindow(arr, K));
}
*/

// 예제 테스트를 위한 실행 코드 (실제 제출 시 주석 처리하거나 제거)
const exampleInput = "15\n10 5 2 7 1 9";
const lines = exampleInput.trim().split('\n');

if (lines.length >= 2) {
    const K = parseInt(lines[0].trim(), 10);
    const arr = lines[1].trim().split(' ').map(Number);
    const result = solveSlidingWindow(arr, K);
    console.log(result);
}
```
