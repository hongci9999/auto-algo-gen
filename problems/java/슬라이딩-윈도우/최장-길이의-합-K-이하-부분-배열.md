# 최장 길이의 합 K 이하 부분 배열
*java · 슬라이딩 윈도우 · 보통 · 배열, 슬라이딩 윈도우, 투포인터*

## 입출력 환경

Java 환경에서 표준 입력(System.in)을 사용하며, 효율적인 입출력을 위해 BufferedReader와 StringTokenizer 사용을 권장합니다.

## 문제

정수 배열 A와 양의 정수 K가 주어집니다. 배열 A의 부분 배열 중 합이 K를 초과하지 않으면서, 가장 긴 길이의 부분 배열을 찾아 그 길이를 출력하는 문제입니다.

부분 배열은 연속된 원소들로 이루어져야 합니다. 모든 원소는 양수입니다.

## 입력

첫 번째 줄에 배열 A의 원소 개수 N이 주어집니다. 두 번째 줄에 N개의 정수 원소(A[0], A[1], ..., A[N-1])가 공백으로 구분되어 주어집니다. 세 번째 줄에 정수 K가 주어집니다.

## 출력

가장 긴 부분 배열의 길이(정수)를 출력합니다.

## 제약 조건

1. $1 	ext{ ≤ } N 	ext{ ≤ } 100,000$
2. $1 	ext{ ≤ } A[i] 	ext{ ≤ } 1000$
3. $1 	ext{ ≤ } K 	ext{ ≤ } 10,000,000$
4. 시간 복잡도는 O(N)을 목표로 합니다.

## 예제 1

**입력**
```
5
1 2 3 1 2
7
```

**출력**
```
4
```

*부분 배열 [1, 2, 3, 1]의 합이 7 이하인 가장 긴 배열의 길이는 4입니다.*

## 예제 2

**입력**
```
3
5 1 2
4
```

**출력**
```
2
```

*부분 배열 [5]는 합이 5로 K=4를 초과하므로 제외됩니다. [1, 2]의 합은 3으로, 최대 길이는 2입니다.*

## 힌트

- 원소들의 합을 효율적으로 관리하기 위해 '슬라이딩 윈도우(Sliding Window)' 기법을 고려해 보세요.
- 두 개의 포인터(left, right)를 사용하여 현재 윈도우의 합을 유지하며 탐색하는 것이 핵심입니다.


## 알고리즘 요약

슬라이딩 윈도우(Sliding Window) 기법을 사용합니다. 오른쪽 포인터(right)를 전진시키며 윈도우에 원소를 추가하고, 현재 윈도우의 합이 K를 초과하면 왼쪽 포인터(left)를 전진시켜 합을 줄이는 과정을 반복합니다. 매 순간 유효한 윈도우의 길이를 최대 길이와 비교하여 갱신합니다.

## 풀이 해설

아이디어: 이 문제는 합의 제약 조건을 만족하는 가장 긴 연속 부분 배열을 찾는 문제입니다. 원소들이 모두 양수이므로, 윈도우의 합이 K를 초과하게 되면, 윈도우의 시작점(왼쪽 포인터)을 이동시키는 것 외에는 합을 줄일 방법이 없습니다. 따라서 슬라이딩 윈도우(Sliding Window)를 적용합니다.

단계:
1. 변수 초기화: `left` 포인터(0), `right` 포인터(0), `currentSum`(0), `maxLength`(0)을 설정합니다.
2. 확장 단계 (Right Pointer): `right` 포인터를 배열의 끝까지 이동시키면서 `currentSum`에 `A[right]`를 더합니다.
3. 축소 단계 (Left Pointer): 만약 `currentSum`이 K를 초과하게 되면, `left` 포인터를 전진시키면서 `currentSum`에서 `A[left]`를 빼줍니다. 이 과정을 `currentSum <= K`가 될 때까지 반복합니다.
4. 결과 갱신: 윈도우의 합이 유효해지면 (즉, `currentSum <= K`), 현재 윈도우의 길이(`right - left + 1`)를 계산하고 `maxLength`와 비교하여 최댓값으로 갱신합니다.
5. 반복: 이 과정을 `right` 포인터가 끝까지 도달할 때까지 반복합니다.

시간 복잡도: `left` 포인터와 `right` 포인터 모두 배열의 원소들을 한 번씩만 순회하므로, 전체 시간 복잡도는 O(N)입니다.

## 참고 코드 (java)

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) {
        // 효율적인 입력을 위해 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 1. N (원소 개수)
        int N = Integer.parseInt(br.readLine());

        // 2. 배열 A
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        // 3. K (최대 합)
        int K = Integer.parseInt(br.readLine());

        // 슬라이딩 윈도우 로직 시작
        int left = 0;
        long currentSum = 0;
        int maxLength = 0;

        for (int right = 0; right < N; right++) {
            // 1. 윈도우 확장: right 포인터 이동 및 합 추가
            currentSum += A[right];

            // 2. 윈도우 축소: 합이 K를 초과하면 left 포인터 이동
            while (currentSum > K) {
                currentSum -= A[left];
                left++;
            }

            // 3. 최대 길이 갱신: 현재 유효한 윈도우의 길이 계산
            // 길이 = right - left + 1
            int currentLength = right - left + 1;
            maxLength = Math.max(maxLength, currentLength);
        }

        System.out.println(maxLength);
    }
```
