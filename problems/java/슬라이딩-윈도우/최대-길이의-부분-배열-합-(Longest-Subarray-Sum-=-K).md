# 최대 길이의 부분 배열 합 (Longest Subarray Sum <= K)
*java · 슬라이딩 윈도우 · 보통 · 배열, 두포인터, Sliding Window*

## 입출력 환경

Java에서 빠른 입출력을 위해 BufferedReader와 StringTokenizer를 사용하는 것이 권장됩니다.

## 문제

정수 배열 A와 목표 합 K가 주어졌을 때, 합이 K를 초과하지 않는 가장 긴 연속된 부분 배열의 길이를 구하세요. 

부분 배열은 반드시 연속적이어야 하며, 모든 원소는 양수라고 가정합니다.

## 입력

첫 번째 줄에 정수 N (배열의 길이)과 정수 K (목표 합)가 공백으로 구분되어 주어집니다. 
두 번째 줄에는 공백으로 구분된 N개의 정수 A[0]부터 A[N-1]이 순서대로 주어집니다.

## 출력

최대 길이의 부분 배열의 길이를 하나의 정수로 출력합니다.

## 제약 조건

1. N의 범위: 1 <= N <= 10^5
2. K의 범위: 1 <= K <= 10^9
3. A[i]의 범위: 1 <= A[i] <= 10^9
4. 합계가 오버플로우 될 수 있으므로, 합 계산 시 long 자료형을 사용해야 합니다.

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

*부분 배열 [3, 1, 2]의 합은 6으로 K=8 이하이며, 길이가 최대입니다.*

## 예제 2

**입력**
```
5 10
1 2 3 4 5
```

**출력**
```
3
```

*부분 배열 [1, 2, 3]의 합은 6으로 K=10 이하입니다. 최대 길이는 3입니다.*

## 힌트

- 두 개의 포인터(left, right)를 사용하여 연속된 구간을 관리해 보세요.
- 현재 합계가 K를 초과하면, 왼쪽 포인터를 이동시켜 합계를 줄여야 합니다 (Sliding Window 원리).


## 알고리즘 요약

슬라이딩 윈도우 기법(Two Pointers). 오른쪽 포인터(right)를 전진시키면서 현재 구간의 합을 누적합니다. 만약 누적된 합이 K를 초과하면, 왼쪽 포인터(left)를 전진시키며 해당 원소를 합계에서 제외하여 윈도우 크기를 줄이고 다시 확인하는 과정을 반복합니다. 이 과정에서 최대 길이를 기록합니다.

## 풀이 해설

문제는 '합이 K 이하인 가장 긴 연속 부분 배열'을 찾는 문제입니다. 이는 대표적인 슬라이딩 윈도우(Sliding Window) 기법으로 해결할 수 있습니다.

**1. 아이디어 (Two Pointers / Sliding Window):**
두 개의 포인터, `left`와 `right`를 사용합니다. `right`는 항상 배열의 끝에서부터 확장하는 역할을 하며, 현재 고려하는 부분 배열을 정의합니다.

**2. 단계별 접근:**
*   초기화: `left = 0`, `currentSum = 0L` (long 타입으로 합 계산), `maxLength = 0`으로 설정합니다.
*   반복 확장 (Right Pointer): `right`를 0부터 배열의 끝까지 순회하며, 매번 `A[right]`를 `currentSum`에 더합니다.
*   유효성 검사 및 수축 (Left Pointer 이동): 만약 `currentSum`이 K보다 커진다면, 현재 윈도우는 유효하지 않습니다. 이 문제를 해결하기 위해 왼쪽 포인터(`left`)를 1 증가시키고, 제거된 원소 `A[left]`를 `currentSum`에서 빼줍니다. 이 과정을 `currentSum <= K`가 될 때까지 반복합니다.
*   최대 길이 갱신: 합이 다시 유효한 상태가 되면 (`currentSum <= K`), 현재 윈도우의 크기(`right - left + 1`)를 계산하여 `maxLength`와 비교하고 더 큰 값으로 갱신합니다.

**3. 시간 복잡도:**
오른쪽 포인터는 N번, 왼쪽 포인터 역시 최대 N번만 이동하므로, 전체 시간 복잡도는 $O(N)$입니다. 공간 복잡도는 $O(1)$입니다.

## 참고 코드 (java)

```java
import java.io.*;
import java.util.*;

public class Solution {
    // 배열 A의 길이 N과 목표 합 K를 받아서 최대 길이를 반환하는 함수
    public static int solve(long[] A, long K) {
        int n = A.length;
        if (n == 0) return 0;

        int left = 0;
        long currentSum = 0; // 합은 오버플로우 방지를 위해 long 사용
        int maxLength = 0;

        // right 포인터로 윈도우를 확장 (O(N))
        for (int right = 0; right < n; right++) {
            currentSum += A[right];

            // 합이 K를 초과하면, 왼쪽에서부터 윈도우를 수축시킨다 (O(1) amortized)
            while (currentSum > K && left <= right) {
                currentSum -= A[left];
                left++;
            }
            
            // 현재 윈도우 [left, right]는 합이 K 이하임이 보장됨
            // 최대 길이 업데이트: current length = right - left + 1
            maxLength = Math.max(maxLength, (right - left + 1));
        }
        return maxLength;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 첫 줄: N과 K를 읽기 위한 가상의 입력 처리 (실제 채점 환경에 맞게 조정 필요)
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st1.nextToken());
        long k = Long.parseLong(st1.nextToken());

        // 두 번째 줄: 배열 A를 읽기 위한 가상의 입력 처리
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        long[] a = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = Long.parseLong(st2.nextToken());
        }

        System.out.println(solve(a, k));
    }
}
```
