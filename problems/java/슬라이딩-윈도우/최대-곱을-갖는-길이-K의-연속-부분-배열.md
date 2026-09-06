# 최대 곱을 갖는 길이 K의 연속 부분 배열
*java · 슬라이딩 윈도우 · 보통 · 배열, 슬라이딩 윈도우, 최대값*

## 입출력 환경

Java 환경에서는 `java.io.BufferedReader`와 `java.util.StringTokenizer`를 사용하여 효율적으로 입력을 처리하는 것이 권장됩니다.

## 문제

정수 배열 A와 길이 K가 주어집니다. 배열 A에서 정확히 K개의 원소를 포함하는 모든 연속 부분 배열(subarray)이 존재합니다. 이들 모든 부분 배열 중에서 원소들의 곱이 가장 큰 부분 배열의 최댓값을 구하는 문제입니다.

주의사항: 원소들의 곱은 매우 커질 수 있으므로, 계산 과정에서 오버플로우가 발생할 수 있으며, 결과는 반드시 `long` 자료형으로 처리해야 합니다.

## 입력

첫 번째 줄에 정수 N과 정수 K가 주어집니다. (N: 배열의 길이, K: 부분 배열의 길이)
두 번째 줄에는 공백으로 구분된 N개의 정수 A[0], A[1], ..., A[N-1]이 순서대로 주어집니다.

## 출력

가장 큰 곱을 갖는 길이 K의 부분 배열의 최댓값을 한 줄에 출력합니다.

## 제약 조건

1. $1 	ext{ <= } N 	ext{ <= } 30$
2. $1 	ext{ <= } K 	ext{ <= } N$
3. $1 	ext{ <= } A[i] 	ext{ <= } 10$
(최종 결과는 `long` 자료형 범위 내에 존재한다고 가정합니다.)

## 예제 1

**입력**
```
4 2
1 2 3 4
```

**출력**
```
12
```

*길이 2인 모든 부분 배열의 곱 중 최댓값은 3 * 4 = 12입니다.*

## 예제 2

**입력**
```
5 3
2 3 2 4 5
```

**출력**
```
24
```

*길이 3인 부분 배열 (2, 3, 2)의 곱은 12, (3, 2, 4)의 곱은 24, (2, 4, 5)의 곱은 40입니다. (수정) 최댓값은 2 * 4 * 5 = 40입니다.*

## 힌트

- 모든 부분 배열을 순회하며 곱을 계산하는 것은 비효율적입니다.
- 슬라이딩 윈도우 기법을 사용하여 O(N) 시간 복잡도로 문제를 해결할 수 있습니다.


## 알고리즘 요약

슬라이딩 윈도우 기법을 사용하여 O(N) 시간 복잡도로 해결합니다. 초기 윈도우(첫 K개 원소)의 곱을 계산한 후, 윈도우를 한 칸씩 오른쪽으로 이동시키면서 이전 윈도우의 가장 왼쪽 원소를 곱셈 과정에서 제거하고, 새로운 오른쪽 원소를 곱셈 과정에 추가합니다. 이 과정을 통해 모든 부분 배열의 곱을 효율적으로 계산할 수 있습니다.

## 풀이 해설

아이디어: 모든 가능한 부분 배열을 개별적으로 곱하는 것은 시간 복잡도가 $O(N 	imes K)$가 되어 비효율적입니다. 따라서 '슬라이딩 윈도우(Sliding Window)' 기법을 사용하여 배열의 크기 K를 유지하며 윈도우를 한 칸씩 이동하면서 곱을 계산합니다. 

단계 1: 초기화
첫 번째 윈도우(인덱스 0부터 K-1까지)의 곱을 계산하여 `currentProduct` 변수에 저장하고, 이를 현재의 최대 곱인 `maxProduct`로 초기화합니다.

단계 2: 윈도우 이동
윈도우의 시작 위치를 $i=K$부터 배열의 끝($N-1$)까지 한 칸씩 이동시키면서 반복합니다. 새로운 윈도우는 $[i-K+1, i]$를 나타냅니다.

단계 3: 곱 업데이트
`currentProduct`를 업데이트하는 과정은 다음과 같습니다:
1. 윈도우를 한 칸 이동했으므로, 가장 왼쪽 원소인 $A[i-K]$를 현재 곱에서 '나눕니다'. (나눗셈은 부동 소수점 오차를 유발할 수 있으므로, 원소들이 0이 아닐 때만 적용 가능하며, 문제 제약 조건상 모든 원소가 1 이상이므로 안전합니다.)
2. 새로운 오른쪽 원소인 $A[i]$를 현재 곱에 '곱합니다'.

단계 4: 최댓값 갱신
업데이트된 `currentProduct`와 `maxProduct`를 비교하여 `maxProduct`를 갱신합니다. 이 과정을 모든 $i$에 대해 반복합니다.

시간 복잡도: 배열을 단 한 번만 순회하므로 시간 복잡도는 $O(N)$입니다. 공간 복잡도는 $O(1)$입니다.

## 참고 코드 (java)

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입출력을 위한 설정
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 첫 줄: N과 K를 읽기
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 두 번째 줄: 배열 A를 읽기
        st = new StringTokenizer(br.readLine());
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        // 현재 윈도우의 곱을 저장할 변수 (long 사용 필수)
        long currentProduct = 1; 
        
        // 1. 초기 윈도우 (0부터 K-1까지) 계산
        for (int i = 0; i < K; i++) {
            currentProduct *= A[i];
        }

        // 현재 최대 곱을 초기화
        long maxProduct = currentProduct;

        // 2. 윈도우를 이동시키며 계산 (i는 새로운 원소의 인덱스)
        for (int i = K; i < N; i++) {
            // 윈도우 이동: A[i-K]를 제거하고 A[i]를 추가
            
            // 1. 가장 왼쪽 원소 제거 (A[i-K])
            // 문제 제약 조건상 A[i]는 1 이상이므로 0으로 나누는 경우는 없음
            currentProduct /= A[i - K]; 
            
            // 2. 가장 오른쪽 원소 추가 (A[i])
            currentProduct *= A[i];
            
            // 3. 최대 곱 갱신
            if (currentProduct > maxProduct) {
                maxProduct = currentProduct;
            }
        }

        System.out.println(maxProduct);
    }
}
```
