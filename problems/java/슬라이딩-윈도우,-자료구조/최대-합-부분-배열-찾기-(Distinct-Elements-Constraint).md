# 최대 합 부분 배열 찾기 (Distinct Elements Constraint)
*java · 슬라이딩 윈도우, 자료구조 · 보통 · 슬라이딩 윈도우, HashMap, 배열*

## 입출력 환경

자바 환경에서 빠른 입출력을 위해 java.util.Scanner 대신 BufferedReader와 StringTokenizer를 사용하는 것을 권장합니다.

## 문제

정수 배열 A와 정수 K가 주어집니다. 이 배열에서 '서로 다른 원소의 개수가 K개 이하'인 부분 배열 중 합이 가장 큰 값을 찾아라.

부분 배열은 연속된 원소들의 집합입니다. 배열 전체가 하나의 부분 배열이며, 최소한 길이가 1인 부분 배열을 고려해야 합니다.

## 입력

첫째 줄에 정수 N과 K가 주어집니다. (N: 배열의 길이, K: 허용되는 최대 고유 원소 개수)
둘째 줄에는 공백으로 구분된 N개의 정수 A[0], A[1], ..., A[N-1]이 주어집니다.

## 출력

가장 합이 큰 부분 배열의 합을 하나의 정수로 출력합니다.

## 제약 조건

1. 1 <= N <= 10^5
2. 1 <= K <= N
3. -10^9 <= A[i] <= 10^9
4. 시간 복잡도는 O(N) 또는 O(N log N) 이내여야 합니다.

## 예제 1

**입력**
```
4 2
1 2 1 3
```

**출력**
```
6
```

*K=2 이하의 고유 원소 개수를 가진 최대 합 부분 배열은 [2, 1, 3] (합: 6)입니다.*

## 예제 2

**입력**
```
5 1
-1 5 -1 5 5
```

**출력**
```
15
```

*K=1이므로 같은 원소만 연속된 최대 합을 찾아야 합니다. [5, 5, 5] (합: 15)가 가장 큽니다.*

## 힌트

- 고정된 창(Window)의 크기 대신, 조건을 만족하는 범위 자체를 슬라이딩해야 합니다.
- 현재 윈도우 내의 '서로 다른 원소의 개수'와 '총합'을 효율적으로 관리할 자료구조가 필요합니다.


## 알고리즘 요약

슬라이딩 윈도우 기법과 해시맵(HashMap)을 이용한 빈도수 추적. 오른쪽 포인터(R)로 윈도우를 확장하며 조건을 검사하고, 조건 위반 시 왼쪽 포인터(L)를 이동시켜 윈도우를 축소합니다.

## 풀이 해설

### 아이디어: 슬라이딩 윈도우
이 문제는 '조건을 만족하는 연속된 구간 중 최댓값'을 찾는 전형적인 문제입니다. 조건을 정의하고 (서로 다른 원소가 K개 이하), 이 조건을 유지하면서 윈도우를 효율적으로 확장/축소해야 합니다. 따라서 슬라이딩 윈도우(Sliding Window) 기법이 가장 적합합니다.

### 단계별 풀이:
1. **자료구조 준비:** 현재 윈도우 [L, R]의 상태를 추적하기 위한 자료구조가 필요합니다.
    - `Map<Integer, Integer> freq`: 배열 A에 포함된 원소들의 빈도수를 저장합니다. (Key: 원소 값, Value: 개수)
    - `long currentSum`: 현재 윈도우 [L, R]의 합을 누적하여 저장합니다.
    - `int maxSum`: 지금까지 발견한 최대 합을 저장합니다.
2. **오른쪽 포인터 (R) 이동 및 확장:** R을 0부터 N-1까지 증가시키며 윈도우를 오른쪽으로 한 칸씩 늘립니다.
    - 새로운 원소 A[R]을 윈도우에 포함시킵니다.
    - `freq`에 A[R]의 빈도수를 1 증가시키고, `currentSum`에 A[R]을 더합니다.
3. **조건 검사 및 왼쪽 포인터 (L) 축소:** 현재 윈도우가 조건을 위반했는지 확인합니다. 조건은 '서로 다른 원소의 개수가 K개 이하'입니다. 즉, `freq.size()`가 K보다 커지면 안 됩니다.
    - 만약 `freq.size() > K`라면, 윈도우를 유효한 상태로 되돌리기 위해 왼쪽 포인터 L을 증가시키며 축소합니다.
    - A[L]을 윈도우에서 제외시킵니다. 따라서 `currentSum`에서 A[L]을 빼고, `freq`의 빈도수를 1 감소시킵니다.
    - **중요:** 만약 A[L]의 빈도수가 0이 되었다면 (즉, 이 원소가 윈도우 내에 더 이상 존재하지 않는다면), `freq`에서 해당 키를 제거해야 합니다. 이것이 '서로 다른 원소의 개수'를 정확히 유지하는 핵심입니다.
    - L을 1 증가시킵니다.
4. **최댓값 갱신:** 윈도우 [L, R]가 조건을 만족할 때마다 (즉, `freq.size() <= K`일 때), 현재의 합(`currentSum`)을 `maxSum`과 비교하여 최댓값을 갱신합니다.
5. **시간 복잡도:** L과 R 포인터는 각각 배열의 끝까지 최대 한 번씩 이동하므로 총 시간 복잡도는 O(N)입니다. 공간 복잡도는 HashMap에 저장되는 원소 수 때문에 O(min(N, K))입니다.

## 참고 코드 (java)

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입력을 위해 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st1.nextToken());
        int K = Integer.parseInt(st1.nextToken());

        long[] A = new long[N];
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Long.parseLong(st2.nextToken());
        }

        // Sliding Window 구현
        Map<Long, Integer> freq = new HashMap<>();
        long currentSum = 0;
        long maxSum = Long.MIN_VALUE; // 합이 음수일 수 있으므로 최소값으로 초기화

        int L = 0;
        for (int R = 0; R < N; R++) {
            // 1. 오른쪽 확장: A[R]을 윈도우에 추가
            long elementR = A[R];
            freq.put(elementR, freq.getOrDefault(elementR, 0) + 1);
            currentSum += elementR;

            // 2. 조건 위반 시 왼쪽 축소 (L 포인터 이동)
            while (freq.size() > K) {
                long elementL = A[L];
                
                // 현재 원소를 윈도우에서 제거
                currentSum -= elementL;
                int count = freq.get(elementL); // 원래 빈도수 가져오기
                freq.put(elementL, count - 1);
                
                // 빈도가 0이 되면 (서로 다른 원소 개수가 줄어들면) Map에서 키 제거
                if (count - 1 == 0) {
                    freq.remove(elementL);
                }
                
                // 왼쪽 포인터 이동
                L++;
            }
            
            // 3. 최댓값 갱신: 현재 윈도우 [L, R]은 조건을 만족하므로 합을 기록
            maxSum = Math.max(maxSum, currentSum);
        }

        System.out.println(maxSum);
    }
}
```
