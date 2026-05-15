# 최대 연속 부분 수열 합 (Maximum Subarray Sum)
*javascript · DP · 보통 · DP, 배열, 누적합*

## 입출력 환경

JavaScript 환경에서 입력은 일반적으로 표준 입력(stdin)을 통해 처리됩니다. 모든 입력은 문자열 형태로 받고, 적절히 파싱해야 합니다.

## 문제

정수 배열 `A`가 주어집니다. 이 배열에서 연속된 부분 수열을 선택했을 때, 그 합이 최대가 되는 값을 구하는 문제입니다. 부분 수열은 반드시 적어도 하나의 원소를 포함해야 합니다.

예시:
A = [1, -2, 3, -1]
부분 수열 [3]의 합은 3
부분 수열 [1, -2, 3]의 합은 2
부분 수열 [3, -1]의 합은 2
최대 합은 [3]의 합인 3입니다.

## 입력

첫 번째 줄에 정수 N이 주어집니다. N은 배열의 크기입니다.
두 번째 줄에 공백으로 구분된 N개의 정수 A[0], A[1], ..., A[N-1]이 주어집니다.

## 출력

최대 연속 부분 수열의 합을 정수로 출력합니다.

## 제약 조건

1 <= N <= 1000
A[i]은 -1000 <= A[i] <= 1000

## 예제 1

**입력**
```
4
1 -2 3 -1
```

**출력**
```
3
```

*배열 [1, -2, 3, -1]에서 최대 합을 가지는 부분 수열은 [3]이며, 합은 3입니다.*

## 예제 2

**입력**
```
5
-2 -3 -1 -5 -6
```

**출력**
```
-1
```

*모든 원소가 음수일 때, 가장 큰 값(최소한의 손해)인 -1이 최대 합입니다.*

## 힌트

- 1. 누적 합(Prefix Sum)의 개념을 활용할 수 있습니다.
- 2. 현재 위치까지의 최대 합을 점화식으로 정의해 보세요. (Kadane's Algorithm)
- 3. 배열의 모든 부분 수열을 확인하는 것은 시간 복잡도가 너무 높습니다.


## 알고리즘 요약

이 문제는 '카데니 알고리즘(Kadane's Algorithm)'이라는 동적 계획법(DP) 기법을 사용하여 해결할 수 있습니다. 핵심 아이디어는 배열을 순차적으로 탐색하면서, 현재 원소까지 포함하여 만들 수 있는 최대 합을 누적 계산하는 것입니다. 만약 현재까지의 누적 합이 음수라면, 그 합은 다음 원소에 더해져도 전체 합을 키우는 데 도움이 되지 않으므로, 그 합을 0으로 리셋하고 현재 원소부터 다시 시작하는 방식으로 처리합니다.

## 풀이 해설

### 아이디어: 카데니 알고리즘 (Kadane's Algorithm)
이 문제는 DP(동적 계획법)의 대표적인 예시입니다. 우리는 배열을 왼쪽에서 오른쪽으로 한 번만 순회하면서 최대 합을 찾을 수 있습니다.

1. **변수 정의:**
   - `current_max`: 현재 원소까지 포함하여 만들 수 있는 최대 연속 부분 수열의 합. 이 값은 매 단계에서 갱신됩니다.
   - `global_max`: 지금까지 발견된 모든 부분 수열 중 가장 큰 합. 이 값을 최종 결과로 반환합니다.

2. **단계별 계산:**
   - 배열의 첫 번째 원소로 `current_max`와 `global_max`를 초기화합니다.
   - 배열의 다음 원소 `A[i]`에 대해 반복합니다:
     a. **`current_max` 갱신:** `current_max`는 이전의 `current_max`와 현재 원소 `A[i]` 중 더 큰 값으로 시작해야 합니다. 즉, `current_max = max(A[i], current_max + A[i])`입니다. (만약 이전까지의 합이 음수라면, 그 합을 버리고 A[i]부터 새롭게 시작하는 것이 유리하기 때문입니다.)
     b. **`global_max` 갱신:** `global_max`는 현재의 `current_max`와 기존의 `global_max` 중 더 큰 값으로 갱신됩니다. `global_max = max(global_max, current_max)`.

3. **시간 복잡도:** 배열을 한 번만 순회하므로 시간 복잡도는 $O(N)$입니다. 공간 복잡도는 $O(1)$입니다.

## 참고 코드 (javascript)

```javascript
/**
 * @param {number[]} A - 정수 배열
 * @returns {number} - 최대 연속 부분 수열의 합
 */
function maxSubarraySum(A) {
    if (!A || A.length === 0) {
        return 0;
    }

    // global_max: 지금까지 발견된 최대 합
    // current_max: 현재 원소까지 포함하여 만들 수 있는 최대 연속 합
    let global_max = A[0];
    let current_max = A[0];

    for (let i = 1; i < A.length; i++) {
        const num = A[i];
        
        // 1. current_max 갱신: 이전까지의 합에 현재 원소를 더하거나, 아니면 현재 원소부터 새로 시작하는 것 중 큰 값을 선택
        current_max = Math.max(num, current_max + num);
        
        // 2. global_max 갱신: 지금까지의 최대 합을 갱신
        global_max = Math.max(global_max, current_max);
    }

    return global_max;
}

// --- 입출력 처리 예시 (Node.js 기준) ---

function solve() {
    const fs = require('fs');
    // 동기 방식으로 전체 입력을 읽어옵니다. 실제 코딩테스트 환경에 맞게 수정 필요
    const input = fs.readFileSync(0, 'utf8').trim().split('\n');

    if (input.length < 2) {
        console.log(0);
        return;
    }

    // 첫 줄: N (배열 크기)
    const N = parseInt(input[0].trim());
    // 두 번째 줄: 배열 원소들
    const A = input[1].trim().split(' ').map(Number);

    if (A.length !== N) {
        // 입력 형식이 잘못되었을 경우 처리
        return;
    }

    const result = maxSubarraySum(A);
    console.log(result);
}

// solve(); // 실제 실행 시 주석 해제
```
