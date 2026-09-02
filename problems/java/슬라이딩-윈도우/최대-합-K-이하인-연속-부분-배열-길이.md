# 최대 합 K 이하인 연속 부분 배열 길이
*java · 슬라이딩 윈도우 · 보통 · 슬라이딩 윈도우, 배열*

## 입출력 환경

자바에서 빠른 입력을 위해 BufferedReader와 StringTokenizer를 사용하세요.

## 문제

정수 배열 A와 양의 정수 K가 주어집니다. 여러분의 목표는 배열 A의 원소 중 합이 K를 넘지 않는 가장 긴 연속된 부분 배열의 길이를 찾는 것입니다.

배열 A의 원소들은 모두 양수입니다. 따라서 합이 증가하는 과정은 단조롭습니다. 이 특성을 이용하여 효율적으로 문제를 해결할 수 있습니다.

## 입력

첫 번째 줄에 정수 N (배열 A의 길이)이 주어집니다. 
두 번째 줄에 N개의 정수 A[0], A[1], ..., A[N-1]이 공백으로 구분되어 주어집니다. 
세 번째 줄에 정수 K가 주어집니다.

## 출력

가장 긴 부분 배열의 길이(정수)를 출력합니다.

## 제약 조건

1.  $1 	ext{ } 	ext{.} 	ext{ } N 	ext{ } 	ext{:} 	ext{ } 1 	ext{ } 	ext{.} 	ext{ } 10^5$
2.  $1 	ext{ } 	ext{.} 	ext{ } A[i] 	ext{ } 	ext{:} 	ext{ } 1 	ext{ } 	ext{.} 	ext{ } 10^9$
3.  $1 	ext{ } 	ext{.} 	ext{ } K 	ext{ } 	ext{:} 	ext{ } 1 	ext{ } 	ext{.} 	ext{ } 10^{14}$ (합이 오버될 수 있으므로 long 사용 권장)

## 예제 1

**입력**
```
4
1 2 3 4
6
```

**출력**
```
3
```

*부분 배열 [1, 2, 3]의 합은 6으로 K 이하이며, 길이가 최대입니다.*

## 예제 2

**입력**
```
5
5 1 1 1 5
5
```

**출력**
```
3
```

*부분 배열 [1, 1, 1]의 합은 3으로 K 이하이며, 최대 길이는 3입니다.*

## 힌트

- 두 포인터(Two Pointers) 기법을 사용하여 탐색 범위를 좁혀나가세요.
- 현재까지의 합(Current Sum)을 유지하며 윈도우를 확장하거나 축소하는 과정을 생각해보세요.


## 알고리즘 요약

슬라이딩 윈도우 (Sliding Window) 기법을 이용합니다. 시작 포인터(Left)와 끝 포인터(Right)를 사용하여 현재 부분 배열의 합을 계산합니다. 합이 K를 초과하면 Left 포인터를 이동시켜 합을 줄이고, K 이하이면 Right 포인터를 이동시켜 합을 늘리며 최대 길이를 갱신합니다.

## 풀이 해설

문제 해결을 위해 슬라이딩 윈도우(Sliding Window) 기법을 사용합니다. 이 방법은 연속된 부분 배열을 탐색하는 문제에 매우 효율적입니다.

**아이디어:** 두 포인터 `left`와 `right`를 사용하여 현재 부분 배열 $A[left..right]$를 정의합니다. `currentSum` 변수를 사용하여 이 부분 배열의 합을 유지합니다.

**단계:**
1.  `left`와 `right` 포인터를 모두 0으로 초기화하고, `currentSum`을 0으로 초기화합니다. 최대 길이를 저장할 `maxLength`도 0으로 초기화합니다.
2.  `right` 포인터를 배열의 끝까지 이동시키며 윈도우를 확장합니다. 매 단계마다 $A[right]$를 `currentSum`에 더합니다.
3.  만약 `currentSum`이 주어진 값 $K$를 초과하게 되면, 윈도우가 너무 커진 것입니다. 이 상태에서는 윈도우를 축소해야 하므로, `left` 포인터를 증가시키고, $A[left]$를 `currentSum`에서 빼줍니다. 이 과정을 `currentSum <= K`가 될 때까지 반복합니다.
4.  `currentSum <= K`를 유지하는 상태가 되면, 현재 윈도우의 길이(`right - left + 1`)를 계산하여 `maxLength`와 비교하고 더 큰 값으로 갱신합니다.
5.  `right` 포인터를 한 칸 이동시켜 2단계로 돌아가 반복합니다.

**시간 복잡도:** `left` 포인터와 `right` 포인터는 각각 배열의 시작부터 끝까지 최대 한 번씩만 이동합니다. 따라서 시간 복잡도는 $O(N)$이며, 이는 매우 효율적입니다.

## 참고 코드 (java)

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        // 빠른 입력을 위한 설정
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 1. N (배열 길이) 읽기
        int N = Integer.parseInt(br.readLine());

        // 2. 배열 A 읽기
        StringTokenizer stA = new StringTokenizer(br.readLine());
        long[] A = new long[N];
        for (int i = 0; i < N; i++) {
            A[i] = Long.parseLong(stA.nextToken());
        }

        // 3. K 값 읽기
        long K = Long.parseLong(br.readLine());

        // 슬라이딩 윈도우 알고리즘 적용
        int left = 0;
        long currentSum = 0;
        int maxLength = 0;

        // right 포인터를 이동시키며 윈도우 확장
        for (int right = 0; right < N; right++) {
            // 윈도우에 A[right]를 추가하여 합 갱신
            currentSum += A[right];

            // 합이 K를 초과하면 윈도우 축소 (left 포인터 이동)
            while (currentSum > K) {
                // A[left]를 합에서 제외
                currentSum -= A[left];
                // left 포인터 이동
                left++;
            }

            // 현재 윈도우의 길이 계산 및 최대 길이 갱신
            // (이 시점에는 currentSum <= K가 보장됨)
            maxLength = Math.max(maxLength, right - left + 1);
        }

        System.out.println(maxLength);
    }
}
```
