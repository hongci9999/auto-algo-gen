# 최대 합 부분 배열 찾기 (Maximum Subarray Sum)
*javascript · 자료구조 · 보통 · 배열, 탐색, Kadane*

## 입출력 환경

Node.js 환경에서 표준 입력(stdin)으로 배열의 원소들을 받습니다. 입력된 문자열을 파싱하여 정수 배열로 사용합니다.

## 문제

정수 배열 `nums`가 주어집니다. 이 배열에서 연속된 원소들로 이루어진 부분 배열 중, 합이 가장 큰 부분 배열의 합을 구하세요. 이 합을 반환해야 합니다. 

부분 배열은 반드시 최소 하나의 원소를 포함해야 합니다.

## 입력

첫 번째 줄에 공백으로 구분된 정수들로 이루어진 배열 `nums`가 주어집니다. (예: 5개의 정수)

## 출력

가장 큰 합을 나타내는 정수 하나를 출력합니다.

## 제약 조건

배열의 원소 개수 N: 1 < N ≤ 10^5
원소 값 범위: -10^4 ≤ nums[i] ≤ 10^4

## 예제 1

**입력**
```
1 2 -1 3
```

**출력**
```
5
```

*배열 전체 [1, 2, -1, 3]의 합이 5로 최대입니다.*

## 예제 2

**입력**
```
-2 -3 1 5
```

**출력**
```
6
```

*부분 배열 [1, 5]의 합이 6으로 최대입니다.*

## 예제 3

**입력**
```
-10 -5 -1
```

**출력**
```
-1
```

*모든 원소가 음수일 경우, 가장 큰 원소(-1)가 최대 합이 됩니다.*

## 힌트

- 부분 배열의 합을 누적하여 계산해 나가는 접근법을 고려해 보세요.
- 현재까지의 합이 음수라면, 이 합은 이후의 합에 불리하게 작용하므로 초기화하는 것이 유리합니다.


## 알고리즘 요약

카데네 알고리즘 (Kadane's Algorithm). 배열을 한 번만 순회하며, 현재까지의 최대 합과 전체 최대 합을 동시에 갱신하는 그리디(Greedy) 알고리즘입니다.

## 풀이 해설

풀이 해설: 이 문제는 전형적인 '최대 합 부분 배열' 문제로, 효율적인 풀이를 위해 카데네 알고리즘(Kadane's Algorithm)을 사용합니다. 이 알고리즘은 배열을 한 번만 순회(O(N))하며 가장 큰 합을 찾아냅니다.

1. 초기화:
   - `globalMax` (전체 최대 합): 배열의 첫 번째 원소로 초기화합니다. 이 값이 현재까지 발견된 가장 큰 합을 저장합니다.
   - `currentMax` (현재까지의 최대 합): 배열의 첫 번째 원소로 초기화합니다. 이 값은 현재 위치까지 연속된 부분 배열의 최대 합을 저장합니다.

2. 순회 (i=1부터 N-1까지):
   - `currentMax` 갱신: 현재 원소 `nums[i]`가 `currentMax`에 더해진 값과, 단순히 `nums[i]` 자체 중 더 큰 값을 `currentMax`에 저장합니다. (즉, 현재 합이 음수라면, 이전 합을 버리고 새로 시작하는 것이 유리합니다.)
   - `globalMax` 갱신: `globalMax`는 항상 `globalMax`와 `currentMax` 중 더 큰 값으로 갱신됩니다. 이것이 지금까지 발견된 최고의 합입니다.

3. 시간 복잡도: 배열을 한 번 순회하므로 O(N)입니다. 공간 복잡도는 O(1)입니다.

## 참고 코드 (javascript)

```javascript
/**
 * @param {number[]} nums - 정수 배열
 * @returns {number} - 최대 합 부분 배열의 합
 */
const maxSubArray = (nums) => {
    if (!nums || nums.length === 0) {
        return 0;
    }

    // globalMax: 전체 배열에서 발견된 최대 합
    let globalMax = nums[0];
    // currentMax: 현재 위치까지 연속된 부분 배열의 최대 합
    let currentMax = nums[0];

    for (let i = 1; i < nums.length; i++) {
        const num = nums[i];

        // 1. currentMax 갱신: 현재 원소를 포함하여 합을 계산하거나, 아니면 현재 원소부터 새로 시작하는 것이 더 좋을지 비교
        // Math.max(num, currentMax + num)은 현재 원소만 사용하는 것과 이전 합을 이어가는 것 중 큰 값을 선택합니다.
        currentMax = Math.max(num, currentMax + num);

        // 2. globalMax 갱신: 지금까지 발견된 최대 합을 갱신합니다.
        globalMax = Math.max(globalMax, currentMax);
    }

    return globalMax;
};

// Node.js 환경을 위한 입력 처리 예시
function solve() {
    const fs = require('fs');
    // 표준 입력 전체를 동기적으로 읽는 가정 (실제 테스트 환경에 따라 입력 방식은 달라질 수 있음)
    // 예시: '1 2 -1 3' 형태의 문자열이 입력되었다고 가정
    
    // 테스트를 위해 샘플 입력을 직접 할당합니다. 실제 코딩 테스트 환경에서는 process.stdin 처리가 필요합니다.
    const inputString = process.argv[2]; 
    if (!inputString) {
        console.log("Usage: node solution.js " + "<space_separated_numbers>");
        return;
    }
    
    const nums = inputString.split(' ').map(s => parseInt(s.trim()));
    
    const result = maxSubArray(nums);
    console.log(result);
}

// solve(); // 실제 제출 시 주석 해제 및 환경에 맞게 수정 필요
```
