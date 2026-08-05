# 최대 합을 갖는 길이 K의 연속 부분 배열 찾기
*java · 슬라이딩 윈도우 · 보통 · 배열, 슬라이딩 윈도우*

## 입출력 환경

효율적인 입출력을 위해 java.io.BufferedReader와 java.util.StringTokenizer를 사용하는 것이 권장됩니다.

## 문제

정수 배열 A와 정수 K가 주어집니다. 여기서 '연속 부분 배열'이란 A의 특정 시작 인덱스부터 끝 인덱스까지의 원소들로 이루어진 부분을 의미합니다.

당신은 길이 K를 가지는 모든 연속 부분 배열 중에서 합이 가장 큰(최댓값) 부분 배열을 찾아 그 최댓값을 출력해야 합니다. 

만약 주어진 배열 A의 길이가 K보다 작다면, 문제에서 정의한 조건을 만족하는 부분 배열은 존재하지 않습니다. 이 경우 0을 출력하세요.

## 입력

첫 번째 줄에 정수 N과 정수 K가 공백으로 구분되어 주어집니다. (N: 배열의 길이, K: 원하는 부분 배열의 길이)
두 번째 줄에는 공백으로 구분된 N개의 정수 원소들이 순서대로 주어집니다.

## 출력

최대 합을 갖는 길이 K의 연속 부분 배열의 합(정수)을 출력합니다. 만약 A의 길이가 K보다 작다면 0을 출력합니다.

## 제약 조건

1 <= N ≤ 10^5
1 <= K <= N (단, N < K인 경우는 별도 처리)
-1000 <= A[i] <= 1000

## 예제 1

**입력**
```
4 2
1 4 2 3
```

**출력**
```
6
```

*길이 2인 부분 배열들: [1, 4](5), [4, 2](6), [2, 3](5). 최댓값은 6입니다.*

## 예제 2

**입력**
```
5 3
-1 -5 -2 -3 -8
```

**출력**
```
-8
```

*길이 3인 부분 배열들: [-1, -5, -2](-8), [-5, -2, -3](-10), [-2, -3, -8](-13). 최댓값은 -8입니다.*

## 예제 3

**입력**
```
3 5
10 20 30
```

**출력**
```
0
```

*배열의 길이(3)가 K(5)보다 작으므로, 조건에 맞는 부분 배열이 없어 0을 출력합니다.*

## 힌트

- 모든 가능한 시작점을 순회하며 합을 계산하는 것은 비효율적입니다.
- 슬라이딩 윈도우(Sliding Window) 기법을 사용하여 이전 창의 합에서 빠지는 원소와 새로 들어오는 원소만 반영하면 시간 복잡도를 줄일 수 있습니다.


## 알고리즘 요약

슬라이딩 윈도우 (Sliding Window):
1. 초기화: 첫 K개 원소를 이용하여 초기 윈도우의 합(CurrentSum)을 계산합니다.
2. 탐색: 배열의 인덱스를 i=K부터 N-1까지 순회하며 창을 오른쪽으로 한 칸 이동시킵니다.
3. 업데이트: 새로운 CurrentSum은 이전 CurrentSum에서 (i-K)번째 원소를 빼고, 현재 i번째 원소를 더하여 얻습니다.
4. 기록: 매 단계마다 계산된 CurrentSum과 지금까지 발견한 최대 합(MaxSum)을 비교하고 MaxSum을 갱신합니다.

## 풀이 해설

### 아이디어 및 접근 방식
이 문제는 길이 K를 고정한 슬라이딩 윈도우 기법으로 해결할 수 있습니다. 단순히 모든 시작점부터 K만큼의 합을 계산하는 것은 O(N*K)의 시간 복잡도를 가집니다. 하지만, 창(Window)을 한 칸씩 이동시키면서 이전 창의 정보를 재활용하면 O(1) 시간에 다음 창의 합을 계산할 수 있어 전체 시간 복잡도는 O(N)으로 최적화됩니다.

### 단계별 풀이
1. **예외 처리**: 먼저 배열 A의 길이가 K보다 작은지 확인합니다. 작다면 정의에 따라 0을 반환합니다.
2. **초기 합 계산 (Initialization)**: 처음부터 K개의 원소(A[0] ~ A[K-1])를 더하여 초기 `currentSum`을 계산하고, 이 값을 잠정적인 최대값(`maxSum`)으로 설정합니다.
3. **슬라이딩 윈도우 이동 (Sliding Window)**: 배열의 인덱스를 i = K부터 N-1까지 순회하며 창을 오른쪽으로 한 칸씩 밀어냅니다.
    *   **이전 원소 제거**: 현재 `currentSum`에서 창을 벗어나는 가장 왼쪽 원소 A[i - K]를 <0xEB><0xBA><0x8D>니다. (Subtract)
    *   **새 원소 추가**: 새로운 원소 A[i]를 더합니다. (Add)
    *   **최댓값 갱신**: 업데이트된 `currentSum`을 `maxSum`과 비교하여, 더 큰 값으로 `maxSum`을 갱신합니다.
4. **결과 반환**: 모든 순회가 끝난 후의 `maxSum`이 최종 답입니다.

### 시간 및 공간 복잡도
*   **시간 복잡도: O(N)** - 배열 전체를 단 한 번만 순회하므로, N에 선형적으로 비례하는 시간이 걸립니다.
*   **공간 복잡도: O(1)** - 추가적인 메모리 할당 없이 변수들로 계산이 가능합니다.

## 참고 코드 (java)

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 효율적인 입출력을 위해 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 1. N과 K 읽기 (첫 번째 줄)
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 예외 처리: 배열 길이가 K보다 작으면 0 출력
        if (N < K) {
            System.out.println(0);
            return;
        }

        // 2. 배열 A 읽기 (두 번째 줄)
        st = new StringTokenizer(br.readLine());
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        // 3. 슬라이딩 윈도우 초기화
        long currentSum = 0;
        // 처음 K개 원소의 합으로 초기화
        for (int i = 0; i < K; i++) {
            currentSum += A[i];
        }
        long maxSum = currentSum;

        // 4. 슬라이딩 윈도우 이동 (인덱스 K부터 N-1까지)
        for (int i = K; i < N; i++) {
            // 창을 오른쪽으로 한 칸 이동: 
            // 1. 가장 왼쪽 원소 A[i - K] 제거
            currentSum -= A[i - K];
            // 2. 새로운 원소 A[i] 추가
            currentSum += A[i];
            
            // 최대 합 갱신
            maxSum = Math.max(maxSum, currentSum);
        }

        System.out.println(maxSum);
    }
}
```
