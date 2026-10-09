# 최대 합이 K보다 작은 부분 배열의 길이
*java · 슬라이딩 윈도우 · 보통 · 슬라이딩 윈도우, 배열, Two Pointers*

## 입출력 환경

Java 환경에서 입력을 받을 때는 Scanner를 사용하거나, 빠른 입력을 위해 BufferedReader와 StringTokenizer를 사용하는 것을 권장합니다.

## 문제

정수 배열 A와 정수 K가 주어집니다. 배열 A의 연속된 부분 배열 중, 합이 K보다 크지 않은 최대 길이를 구하시오.

부분 배열의 합이 K보다 작거나 같은 경우, 그 길이를 기록하고, 최대 길이를 최종 결과로 반환합니다.

## 입력

첫 번째 줄에 정수 N (배열의 길이)이 주어집니다.
두 번째 줄에 N개의 정수 A[0], A[1], ..., A[N-1]이 공백으로 구분되어 주어집니다.
세 번째 줄에 정수 K가 주어집니다.

## 출력

최대 길이를 나타내는 정수 하나만 출력합니다.

## 제약 조건

1. $1 	ext{ <= } N 	ext{ <= } 10^5$
2. $-10^9 	ext{ <= } A[i] 	ext{ <= } 10^9$ (합계를 계산할 때는 long 타입을 사용해야 합니다.)
3. $-10^{18} 	ext{ <= } K 	ext{ <= } 10^{18}$

## 예제 1

**입력**
```
3
1 2 3
5
```

**출력**
```
2
```

*합이 5 이하인 가장 긴 부분 배열은 [1, 2] 또는 [2, 3]이며, 길이는 2입니다.*

## 예제 2

**입력**
```
4
3 1 2 5
8
```

**출력**
```
3
```

*합이 8 이하인 가장 긴 부분 배열은 [3, 1, 2] 또는 [1, 2, 5]이며, 길이는 3입니다.*

## 예제 3

**입력**
```
5
1 1 1 1 1
2
```

**출력**
```
2
```

*합이 2 이하인 가장 긴 부분 배열은 [1, 1]이며, 길이는 2입니다.*

## 힌트

- 두 포인터(Two Pointers) 기법을 활용하는 것이 효율적입니다.
- 현재 합(Current Sum)이 K를 초과하면, 왼쪽 포인터를 이동시켜 합을 줄여야 합니다.


## 알고리즘 요약

슬라이딩 윈도우(Sliding Window) 기법을 사용합니다. 오른쪽 포인터(right)를 한 칸씩 전진시키면서 현재 합(currentSum)을 계산합니다. 만약 currentSum이 K를 초과하면, 왼쪽 포인터(left)를 전진시키면서 currentSum에서 해당 원소를 빼주고, 최대 길이 갱신 로직을 반복합니다.

## 풀이 해설

이 문제는 '슬라이딩 윈도우' 기법을 사용하여 O(N)의 시간 복잡도로 해결할 수 있습니다.

**1. 아이디어:**
우리는 길이가 최대인 부분 배열을 찾아야 합니다. 윈도우의 오른쪽 끝(right)을 전진시키며 윈도우를 확장하고, 합이 K를 초과하게 되는 순간 윈도우의 왼쪽 끝(left)을 전진시켜 합을 다시 K 이하로 되돌리는 과정을 반복합니다.

**2. 단계:**
*   `left` 포인터와 `right` 포인터를 0으로 초기화하고, `currentSum`을 0으로 초기화하며, `maxLen`을 0으로 초기화합니다.
*   `right` 포인터를 배열의 끝까지 이동시킵니다.
*   매 반복마다 `currentSum`에 `A[right]`를 더합니다.
*   **조건 검사:** 만약 `currentSum`이 K를 초과하면, 윈도우를 축소해야 합니다. 이 과정은 `currentSum > K`인 동안 반복됩니다.
    *   `currentSum`에서 `A[left]`를 <0xEB><0xBA><0x8D>니다.
    *   `left` 포인터를 1 증가시킵니다.
*   **결과 갱신:** 윈도우가 유효한 상태(currentSum <= K)가 되면, 현재 윈도우의 길이(`right - left + 1`)와 `maxLen`을 비교하여 `maxLen`을 갱신합니다.
*   모든 `right` 포인터 이동이 끝나면 `maxLen`이 최종 답이 됩니다.

**3. 시간 복잡도:**
`left` 포인터와 `right` 포인터는 각각 배열을 최대 한 번씩만 순회하므로, 시간 복잡도는 $O(N)$입니다. (N은 배열의 길이)

## 참고 코드 (java)

```java
import java.util.Scanner;
import java.util.Arrays;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 1. N 입력 받기
        if (!scanner.hasNextInt()) return;
        int N = scanner.nextInt();
        
        // 2. 배열 A 입력 받기 (long 타입으로 저장하여 오버플로우 방지)
        long[] A = new long[N];
        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextLong();
        }
        
        // 3. K 입력 받기
        long K = scanner.nextLong();

        // 슬라이딩 윈도우 로직 시작
        long currentSum = 0;
        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < N; right++) {
            // 윈도우 확장: right 포인터를 한 칸 이동시키고 합에 더함
            currentSum += A[right];

            // 윈도우 축소: 합이 K를 초과하면, left 포인터를 이동시키며 합을 줄임
            while (currentSum > K) {
                // A[left]를 currentSum에서 제거
                currentSum -= A[left];
                // left 포인터 이동
                left++;
            }
            
            // 현재 윈도우의 길이 (right - left + 1)를 최대 길이와 비교하여 갱신
            // 이 시점에서 currentSum은 반드시 K 이하임을 보장함
            maxLen = Math.max(maxLen, right - left + 1);
        }

        System.out.println(maxLen);
        scanner.close();
    }
}
```
