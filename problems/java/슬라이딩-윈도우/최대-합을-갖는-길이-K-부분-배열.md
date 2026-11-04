# 최대 합을 갖는 길이 K 부분 배열
*java · 슬라이딩 윈도우 · 보통 · 배열, 슬라이딩 윈도우, 누적 합*

## 입출력 환경

Java 환경에서 빠른 입출력을 위해 BufferedReader와 StringTokenizer 사용을 권장합니다.

## 문제

정수 배열 A와 길이 K가 주어집니다. 이 배열에서 길이가 정확히 K인 모든 연속된 부분 배열(subarray)이 존재합니다. 이 중 합(sum)이 최대가 되는 부분 배열의 합을 구하는 문제입니다. 배열의 원소 값은 양수, 음수, 0을 포함할 수 있습니다.

예시: A = [1, 4, 2, 3], K = 2
부분 배열: [1, 4] (합 5), [4, 2] (합 6), [2, 3] (합 5)
최대 합: 6

## 입력

첫 번째 줄에 정수 N과 K가 공백으로 구분되어 주어지고, 두 번째 줄부터 N개의 정수 원소 A[0], A[1], ..., A[N-1]이 공백으로 구분되어 주어집니다.

## 출력

최대 합을 갖는 길이 K 부분 배열의 합을 하나의 정수 형태로 출력합니다.

## 제약 조건

1. 1 ≤ N ≤ 100,000
2. 1 ≤ K ≤ N
3. -1000 ≤ A[i] ≤ 1000
4. 시간 복잡도는 O(N) 또는 O(N log N) 이하여야 합니다.

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

*길이 2의 모든 부분 배열 중 합이 가장 큰 것은 [4, 2]의 합 6입니다.*

## 예제 2

**입력**
```
5 3
5 -1 3 2 0
```

**출력**
```
7
```

*길이 3의 부분 배열 중 최대 합은 [5, -1, 3]의 합 7입니다.*

## 힌트

- 모든 부분 배열의 합을 개별적으로 계산하면 시간 복잡도가 높아집니다.
- 슬라이딩 윈도우(Sliding Window) 기법을 사용하면 O(1)의 시간 복잡도로 다음 윈도우의 합을 계산할 수 있습니다.


## 알고리즘 요약

Sliding Window (슬라이딩 윈도우) 기법을 활용합니다. 초기 윈도우(길이 K)의 합을 계산한 후, 이후 배열을 순회하며 윈도우를 한 칸씩 이동시킬 때, 이전 윈도우의 합에서 빠지는 원소를 빼고, 새로 들어오는 원소를 더하여 다음 윈도우의 합을 O(1) 시간에 계산합니다. 이 과정을 반복하며 최대 합을 갱신합니다.

## 풀이 해설

풀이 아이디어: 이 문제는 고정된 길이 K의 부분 배열의 최대 합을 찾는 문제입니다. 만약 매번 K개의 원소를 더한다면 시간 복잡도는 O(N*K)가 되어 N이 커질 경우 시간 초과가 발생합니다. 따라서 O(N) 시간 복잡도를 목표로 해야 합니다. 

단계 1. 초기 윈도우 합 계산: 배열의 처음 K개 원소 A[0]부터 A[K-1]까지의 합을 계산하여 초기 최대 합(maxSum)으로 설정합니다. 
단계 2. 슬라이딩 윈도우 구현: i를 K부터 N-1까지 증가시키며 윈도우를 이동시킵니다. 윈도우가 한 칸 이동할 때마다, 이전 윈도우의 합(currentSum)에서 윈도우의 가장 왼쪽 원소 A[i-K]를 빼주고, 새로운 오른쪽 원소 A[i]를 더합니다. 이 과정은 O(1) 시간에 수행됩니다. 
단계 3. 최대 합 갱신: 계산된 새로운 currentSum이 현재까지의 maxSum보다 크면 maxSum을 갱신합니다. 
시간 복잡도: 초기 합 계산에 O(K)가 걸리고, 나머지 N-K개의 윈도우 이동에 O(1)씩 N-K번의 연산이 걸립니다. 따라서 총 시간 복잡도는 O(K + (N-K)) = O(N)입니다.

## 참고 코드 (java)

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입력을 위한 설정
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 배열 원소 입력
        int[] A = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        // 1. 초기 윈도우 합 계산 (A[0] ~ A[K-1])
        long currentSum = 0;
        for (int i = 0; i < K; i++) {
            currentSum += A[i];
        }
        
        long maxSum = currentSum;

        // 2. 슬라이딩 윈도우 이동 (i는 새로운 윈도우의 끝 인덱스)
        // i는 K부터 N-1까지 반복하며 윈도우를 한 칸씩 오른쪽으로 이동시킵니다.
        for (int i = K; i < N; i++) {
            // 윈도우 이동: 이전 윈도우의 합 - 빠지는 원소 + 들어오는 원소
            // 빠지는 원소: A[i-K]
            // 들어오는 원소: A[i]
            currentSum = currentSum - A[i - K] + A[i];
            
            // 3. 최대 합 갱신
            maxSum = Math.max(maxSum, currentSum);
        }

        System.out.println(maxSum);
    }
}
```
