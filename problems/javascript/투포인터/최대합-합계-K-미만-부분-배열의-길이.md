# 최대합 합계 K 미만 부분 배열의 길이
*javascript · 투포인터 · 보통 · 배열, 투포인터, 슬라이딩 윈도우*

## 입출력 환경

Node.js 환경에서 입력을 받으려면 `readline` 모듈을 사용하거나 전체 입력 문자열을 한 번에 처리하는 방식을 권장합니다. (여기서는 전체 문자열을 받는다고 가정합니다.)

## 문제

정수 배열 `arr`과 기준 합계 `K`가 주어집니다. 이 배열에서 연속된 부분 배열(subarray) 중, 합계가 `K`를 초과하지 않는 부분 배열의 최대 길이를 구하는 문제입니다.

주어진 모든 원소는 0 이상의 정수입니다.

## 입력

첫 번째 줄에는 배열의 길이 N과 최대 허용 합계 K가 공백으로 구분되어 입력됩니다. (N: int, K: BigInt)
두 번째 줄에는 N개의 정수 원소들이 공백으로 구분되어 입력됩니다.

## 출력

최대 길이를 나타내는 정수 하나를 출력합니다.

## 제약 조건

1 <= N <= 10^5
0 <= arr[i] <= 10^9
0 <= K <= 10^{14}
시간 복잡도는 O(N)을 목표로 합니다.

## 예제 1

**입력**
```
4 8
3 1 2 7
```

**출력**
```
3
```

*부분 배열 [3, 1, 2]의 합은 6으로 K(8) 이하이며, 길이가 최대입니다.*

## 예제 2

**입력**
```
5 20
1 2 3 4 5
```

**출력**
```
5
```

*전체 배열 [1, 2, 3, 4, 5]의 합은 15로 K(20) 이하이므로 길이가 최대입니다.*

## 예제 3

**입력**
```
3 10
5 5 5
```

**출력**
```
2
```

*합계가 10을 넘지 않는 최대 길이는 [5, 5]로 2입니다.*

## 힌트

- 모든 원소가 음수가 아니라는 점을 활용하여 슬라이딩 윈도우 기법을 적용할 수 있습니다.
- 현재 합계를 효율적으로 관리하며 윈도우를 이동시키는 것이 핵심입니다.


## 알고리즘 요약

슬라이딩 윈도우 (Two Pointers) 기법을 사용합니다. 한쪽 포인터(Left)로 윈도우의 시작을, 다른 쪽 포인터(Right)로 윈도우의 끝을 이동시키면서 현재 윈도우의 합계를 유지합니다. 합계가 K를 초과하면 Left 포인터를 이동시켜 합계를 줄이고, 합계가 K 이하면 Right 포인터를 이동시켜 합계를 늘리며 최대 길이를 갱신합니다.

## 풀이 해설

풀이 해설:
1. 아이디어: 이 문제는 '슬라이딩 윈도우(Sliding Window)' 기법을 사용하기에 적합합니다. 모든 원소의 값이 0 이상이므로, 윈도우의 크기(길이)를 늘릴수록 합계는 단조 증가합니다. 따라서 합계가 K를 초과하면 반드시 윈도우의 왼쪽 끝을 좁혀야 합니다.
2. 단계:
   a. 변수 초기화: `left` 포인터(0), `right` 포인터(0), `currentSum` (0), `maxLength` (0)를 초기화합니다. 합계가 K의 범위까지 커질 수 있으므로, `currentSum`은 BigInt로 처리하는 것이 안전합니다.
   b. 윈도우 확장 (Right 포인터 이동): `right` 포인터를 배열의 끝까지 이동시키면서 `arr[right]` 값을 `currentSum`에 더합니다.
   c. 윈도우 축소 (Left 포인터 이동): 만약 `currentSum`이 `K`를 초과하게 되면, `left` 포인터를 이동시키면서 `arr[left]` 값을 `currentSum`에서 빼줍니다. 이 과정은 `currentSum <= K`가 될 때까지 반복됩니다.
   d. 최대 길이 갱신: 윈도우가 유효한 상태(`currentSum <= K`)가 될 때마다, 현재 윈도우의 길이 (`right - left + 1`)를 계산하여 `maxLength`와 비교하며 최댓값을 갱신합니다.
3. 시간 복잡도: `left` 포인터와 `right` 포인터 모두 배열의 원소를 최대 한 번씩만 순회합니다. 따라서 시간 복잡도는 O(N)입니다.

## 참고 코드 (javascript)

```javascript
/**
 * @param {number[]} arr 배열
 * @param {bigint} K 최대 허용 합계
 * @returns {number} 최대 길이
 */
function solve(arr, K) {
    let left = 0;
    let currentSum = 0n; // BigInt 사용
    let maxLength = 0;
    const N = arr.length;

    for (let right = 0; right < N; right++) {
        // 1. 윈도우 확장: 현재 원소를 합계에 더함
        currentSum += BigInt(arr[right]);

        // 2. 윈도우 축소: 합계가 K를 초과할 때까지 왼쪽 포인터를 이동시키며 합계를 줄임
        while (currentSum > K && left <= right) {
            // arr[left] 값을 합계에서 <0xEB><0xBA><0x8C>
            currentSum -= BigInt(arr[left]);
            // 왼쪽 포인터 이동
            left++;
        }

        // 3. 길이 갱신: 윈도우가 유효한 상태(currentSum <= K)일 때만 길이를 갱신함
        // (left가 right를 넘어가지 않았다는 전제 하에 길이가 유효함)
        if (left <= right) {
             // 현재 길이: right - left + 1
             maxLength = Math.max(maxLength, right - left + 1);
        }
    }
    return maxLength;
}

// Node.js 환경을 위한 입출력 처리 예시
// 실제 코딩테스트 환경에 맞게 입력 처리 부분을 수정해야 합니다.
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

let lines = [];
rl.on('line', (line) => {
    lines.push(line);
});

rl.on('close', () => {
    if (lines.length < 2) return;

    // 첫 번째 줄: N K
    const [N_str, K_str] = lines[0].trim().split(' ');
    const K = BigInt(K_str);

    // 두 번째 줄: 배열 원소
    const arr = lines[1].trim().split(' ').map(Number);

    const result = solve(arr, K);
    console.log(result);
});
```
