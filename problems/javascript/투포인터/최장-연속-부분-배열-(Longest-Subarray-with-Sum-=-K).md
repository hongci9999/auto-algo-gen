# 최장 연속 부분 배열 (Longest Subarray with Sum <= K)
*javascript · 투포인터 · 보통 · 투포인터, 슬라이딩 윈도우, 배열*

## 입출력 환경

Node.js 환경에서 표준 입력을 처리할 때, 전체 입력을 한 번에 읽어 배열로 처리하는 방식을 사용하세요.

## 문제

N개의 양수 정수로 이루어진 배열 $A$와 정수 $K$가 주어집니다. 

여러분은 배열 $A$의 부분 배열 중에서 원소들의 합이 $K$를 넘지 않으면서, 그 길이가 최대가 되는 부분 배열을 찾아야 합니다. 이 최대 길이를 반환하세요.

만약 합이 $K$를 넘지 않는 부분 배열이 하나도 없다면 0을 반환합니다.

## 입력

첫째 줄에 정수 N과 정수 K가 주어집니다. 
둘째 줄에 N개의 양수 정수 원소가 공백으로 구분되어 주어집니다.

## 출력

최대 길이를 나타내는 정수 하나를 출력합니다.

## 제약 조건

1. $1 	ext{ ≤ } N 	ext{ ≤ } 200,000$
2. $1 	ext{ ≤ } A_i 	ext{ ≤ } 10^9$
3. $0 	ext{ ≤ } K 	ext{ ≤ } 10^{14}$
(시간 복잡도: $O(N)$ 이하가 권장됩니다.)

## 예제 1

**입력**
```
5 10
1 2 3 4 5
```

**출력**
```
3
```

*부분 배열 [1, 2, 3]의 합이 6으로 최대 길이 3입니다. [1, 2, 3, 4]는 10을 초과합니다.*

## 예제 2

**입력**
```
4 5
5 1 1 1
```

**출력**
```
1
```

*가장 긴 부분 배열은 [5] 또는 [1]로, 최대 길이는 1입니다. [5, 1]은 6으로 K를 초과합니다.*

## 힌트

- 부분 배열의 합을 효율적으로 계산하는 방법을 생각해 보세요.
- 윈도우의 시작점과 끝점을 포인터로 관리하면 시간 복잡도를 줄일 수 있습니다.


## 알고리즘 요약

슬라이딩 윈도우 (Sliding Window) / 투 포인터 기법을 사용합니다. 두 포인터 (left, right)를 이용하여 현재 윈도우 [left, right]의 합을 유지하며, 합이 K를 초과하면 left 포인터를 이동시켜 합을 줄이고, 합이 K 이하일 때마다 최대 길이를 갱신합니다.

## 풀이 해설

풀이 해설: 아이디어 → 단계 → 시간복잡도

1. 아이디어 (Sliding Window):
이 문제는 '최대 길이'를 찾는 문제이며, '합이 K를 넘지 않아야 한다'는 제약 조건이 있습니다. 이 구조는 슬라이딩 윈도우 기법을 적용하기에 매우 적합합니다. 윈도우의 오른쪽 끝(right)을 한 칸씩 전진시키면서 합을 계산하고, 합이 K를 초과하면 윈도우의 왼쪽 끝(left)을 전진시켜 합을 다시 K 이하로 만들면서 윈도우를 유지합니다.

2. 단계:
   a. 변수 초기화: 현재까지의 합 `currentSum`을 0으로, 최대 길이 `maxLength`를 0으로, 왼쪽 포인터 `left`를 0으로 설정합니다.
   b. 윈도우 확장 (Right Pointer):
      오른쪽 포인터 `right`를 배열의 끝까지 순회시키며, `currentSum`에 $A[right]$ 값을 더합니다.
   c. 윈도우 축소 (Left Pointer):
      `currentSum`이 $K$를 초과하는 경우, 윈도우가 유효하지 않다는 의미이므로, 왼쪽 포인터 `left`를 이동시키고 `currentSum`에서 $A[left]$ 값을 <0xEB><0xBA><0x8D>니다. 이 과정을 `currentSum <= K`가 될 때까지 반복합니다.
   d. 최대 길이 갱신:
      현재 윈도우 $[left, right]$의 합이 $K$ 이하가 되었으므로, 이 윈도우의 길이 $(right - left + 1)$를 계산하여 `maxLength`와 비교하고 더 큰 값으로 갱신합니다.
   e. 반복: `right` 포인터가 끝날 때까지 2b~2d 과정을 반복합니다.

3. 시간 복잡도:
오른쪽 포인터(`right`)와 왼쪽 포인터(`left`)는 각각 $N$번씩 최대 이동합니다. 따라서 전체 시간 복잡도는 $O(N)$으로 매우 효율적입니다.

## 참고 코드 (javascript)

```javascript
/**
 * Node.js 환경에서 표준 입력을 처리하는 예제입니다.
 * 전체 입력을 받아 처리하기 위해 readline 모듈을 사용합니다.
 */

function solve() {
    const fs = require('fs');
    // 동기 방식으로 전체 입력을 읽어옵니다.
    const input = fs.readFileSync(0, 'utf8').trim().split('\n');

    // 첫 번째 줄: N과 K
    const [N_str, K_str] = input[0].split(' ');
    const N = parseInt(N_str);
    // K는 매우 클 수 있으므로 BigInt 사용
    const K = BigInt(K_str);

    // 두 번째 줄: 배열 A
    const A = input[1].split(' ').map(s => BigInt(s));

    let left = 0;
    let currentSum = 0n; // BigInt로 초기화
    let maxLength = 0;

    for (let right = 0; right < N; right++) {
        // 1. 윈도우 확장: 합에 A[right]를 더한다.
        currentSum += A[right];

        // 2. 윈도우 축소: 합이 K를 초과하면 left를 이동시키며 합을 줄인다.
        while (currentSum > K) {
            // A[left]를 빼고 left 포인터를 오른쪽으로 이동시킨다.
            currentSum -= A[left];
            left++;
        }

        // 3. 최대 길이 갱신: 현재 윈도우 [left, right]의 길이를 계산한다.
        // 길이 = right - left + 1
        const currentLength = right - left + 1;
        if (currentLength > maxLength) {
            maxLength = currentLength;
        }
    }

    console.log(maxLength);
}

solve();
```
