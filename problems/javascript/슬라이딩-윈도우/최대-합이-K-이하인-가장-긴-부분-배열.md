# 최대 합이 K 이하인 가장 긴 부분 배열
*javascript · 슬라이딩 윈도우 · 보통 · 배열, 투포인터, 자료구조*

## 입출력 환경

Node.js 환경에서 표준 입력 전체를 읽어 처리합니다. (예: readline 모듈 또는 process.stdin 사용)

## 문제

정수 배열 A와 정수 K가 주어집니다. 배열 A의 모든 부분 배열 중에서, 합이 K를 넘지 않으면서 길이가 가장 긴 부분 배열을 찾아 그 최대 길이를 반환하세요.

(예시: A = [1, 5, 2], K = 6인 경우. 부분 배열 [1, 5]는 합이 6으로 유효하며 길이는 2입니다. 부분 배열 [1, 5, 2]는 합이 8로 K를 초과하므로 유효하지 않습니다. 따라서 최대 길이는 2입니다.)

## 입력

첫째 줄에 정수 N (배열의 길이)이 주어집니다.
둘째 줄에 공백으로 구분된 N개의 정수 A[0], A[1], ..., A[N-1]가 주어집니다.
셋째 줄에 목표 합 K가 주어집니다.

## 출력

최대 길이인 하나의 정수를 출력합니다.

## 제약 조건

1.  $1 	ext{ } floor 	ext{ } N 	ext{ } floor 10^5$
2.  $-10^9 	ext{ } floor 	ext{ } A[i] 	ext{ } floor 10^9$
3.  $-10^{18} 	ext{ } floor 	ext{ } K 	ext{ } floor 10^{18}$
(주의: 합을 계산할 때 JavaScript의 기본 Number 타입이 아닌 BigInt를 사용하여 오버플로우를 방지해야 합니다.)

## 예제 1

**입력**
```
3
1 5 2
6
```

**출력**
```
2
```

*부분 배열 [1, 5]의 합은 6이며 길이는 2입니다. 최대 길이입니다.*

## 예제 2

**입력**
```
5
3 1 2 7 4
10
```

**출력**
```
3
```

*부분 배열 [3, 1, 2]는 합이 6이고 길이가 3입니다. [1, 2, 7]은 합이 10이며 길이 3입니다. 최대 길이는 3입니다.*

## 힌트

- 현재 부분 배열의 합을 누적하여 관리하세요.
- 합이 K를 초과할 경우, 윈도우의 시작점(Left)을 이동시켜야 합니다.


## 알고리즘 요약

슬라이딩 윈도우 (Sliding Window). 두 개의 포인터 'left'와 'right'를 사용하여 현재 부분 배열 [A[left]...A[right]]를 유지하며, 이 구간의 합이 K를 초과하는지 지속적으로 확인합니다. 합이 초과하면 left 포인터를 이동시키고, 그렇지 않으면 right 포인터를 전진시키면서 최대 길이를 갱신합니다.

## 풀이 해설

아이디어: 문제에서 요구하는 '합이 K 이하'라는 조건은 부분 배열의 크기를 결정하는 제약 조건입니다. 이 조건을 활용하여 슬라이딩 윈도우 기법을 사용하면 O(N) 시간에 해결할 수 있습니다.

단계:
1. 초기화: `left` 포인터와 `currentSum` (현재 합) 및 `maxLength`를 0으로 설정합니다. 이때, 입력 값의 범위가 매우 크므로 JavaScript에서는 BigInt 타입을 사용하여 합을 관리해야 합니다.
2. Right 전진: `right` 포인터를 배열 끝까지 한 칸씩 이동시키며 `A[right]` 값을 `currentSum`에 더하여 윈도우를 확장합니다.
3. 조건 확인 (Shrink): 만약 `currentSum`이 K보다 커지면, 현재 윈도우는 유효하지 않다는 뜻입니다. 따라서 `left` 포인터를 오른쪽으로 한 칸 이동시키면서 `A[left]` 값을 `currentSum`에서 빼주고, 이 과정을 반복하여 `currentSum`이 다시 K 이하가 될 때까지 윈도우를 축소합니다.
4. 최대 길이 갱신: 매 단계마다 (shrink 과정이 끝난 후), 현재 윈도우의 크기 (`right - left + 1`)는 합 조건(<= K)을 만족하는 가장 긴 유효한 부분 배열 중 하나입니다. 따라서 `maxLength = max(maxLength, right - left + 1)`로 최대 길이를 갱신합니다.
5. 반복: 이 과정을 `right` 포인터가 끝날 때까지 반복하고, 최종 `maxLength`를 반환합니다.

시간 복잡도: Time Complexity는 O(N)입니다. 'left'와 'right' 포인터 모두 배열을 최대 한 번씩만 순회하므로 선형 시간 복잡도를 가집니다.

## 참고 코드 (javascript)

```javascript
/**
 * @param {bigint[]} A - 정수 배열 (BigInt 타입)
 * @param {bigint} K - 목표 합계 (BigInt 타입)
 * @returns {number} 최대 길이
 */
function solve(A, K) {
    let left = 0;
    let currentSum = BigInt(0);
    let maxLength = 0;
    const N = A.length;

    for (let right = 0; right < N; right++) {
        // 1. Window 확장: A[right]를 합에 추가합니다.
        currentSum += A[right];

        // 2. 조건 확인 및 Shrink: 합이 K를 초과하면 left 포인터를 이동시켜 축소합니다.
        while (currentSum > K) {
            // 현재 A[left] 값을 합에서 제거하고 left를 전진시킵니다.
            currentSum -= A[left];
            left++;
        }

        // 3. 최대 길이 갱신: 현재 유효한 윈도우의 길이를 계산하여 최대값과 비교합니다.
        const currentLength = right - left + 1;
        if (currentLength > maxLength) {
            maxLength = currentLength;
        }
    }
    return maxLength;
}

/**
 * Node.js 환경에서 표준 입력을 처리하는 함수 예시입니다.
 * 실제 제출 시에는 이 부분의 입력 파싱 로직이 중요합니다.
 */
function runSolution() {
    const fs = require('fs');
    // 모든 인풋을 동기적으로 읽어옵니다. (테스트 환경에 맞게 수정 필요)
    const input = fs.readFileSync(0, 'utf8').trim().split('\n');

    if (input.length < 3) return;

    // 1. N 처리 (사용되지 않지만 순서 유지를 위해 읽음)
    let N = parseInt(input[0].trim());

    // 2. 배열 A 파싱 및 BigInt 변환
    const A_str = input[1].trim().split(' ').filter(s => s).map(s => s);
    if (A_str.length === 0) return;
    
    let A = [];
    for (const str of A_str) {
        // 큰 숫자를 처리하기 위해 BigInt로 변환합니다.
        A.push(BigInt(str));
    }

    // 3. K 파싱 및 BigInt 변환
    let K = BigInt(input[2].trim());

    // 문제 해결 함수 호출
    const result = solve(A, K);
    console.log(result);
}
```
