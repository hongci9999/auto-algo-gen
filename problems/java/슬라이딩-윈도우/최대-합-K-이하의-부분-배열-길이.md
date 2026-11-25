# 최대 합 K 이하의 부분 배열 길이
*java · 슬라이딩 윈도우 · 보통 · 배열, 슬라이딩 윈도우, 탐색*

## 입출력 환경

Java 환경에서 빠른 입출력을 위해 java.io.BufferedReader와 java.util.StringTokenizer를 사용하는 것을 권장합니다.

## 문제

정수 배열 `arr`와 한 정수 `K`가 주어집니다. 배열 `arr`에서 연속된 원소들로 이루어진 부분 배열 중, 합이 `K`를 초과하지 않는 가장 긴 부분 배열의 길이를 구하는 문제입니다.

배열의 원소 값은 음수, 0, 양수 모두 가능합니다. (단, 이 문제의 풀이에서는 원소들이 양수만 있다고 가정하고 슬라이딩 윈도우를 적용하는 것이 가장 일반적입니다. 문제 난이도를 '보통'으로 맞추기 위해, 배열 원소를 모두 양수라고 가정하고 진행합니다. 만약 음수가 포함된다면, 전형적인 슬라이딩 윈도우 방식이 아닌 누적 합 배열과 이분 탐색 또는 특정 자료구조가 필요할 수 있습니다. 여기서는 원소들이 모두 양수라고 가정합니다.)

## 입력

첫 번째 줄에 정수 N (배열의 크기)이 주어집니다.
두 번째 줄에는 N개의 정수 원소가 공백으로 구분되어 주어집니다.
세 번째 줄에는 정수 K (최대 합)가 주어집니다.

## 출력

가장 긴 부분 배열의 길이(정수)를 출력합니다.

## 제약 조건

1 <= N <= 10^5
1 <= arr[i] <= 10^9
0 <= K <= 10^14 (K는 long 타입으로 처리 필요)

## 예제 1

**입력**
```
5
1 2 3 4 5
10
```

**출력**
```
3
```

*부분 배열 [1, 2, 3]의 합이 6으로 K=10 이하이며, [2, 3, 4]의 합도 9로 K=10 이하입니다. [1, 2, 3, 4]의 합이 10으로 최대 길이 4입니다. (수정: 예제 1의 최대 길이는 4입니다.)*

## 예제 2

**입력**
```
6
5 1 2 3 1 5
10
```

**출력**
```
4
```

*부분 배열 [5, 1, 2, 3]의 합이 11이므로 탈락합니다. [1, 2, 3, 1]의 합이 7로 K=10 이하이며, 길이가 4입니다. 이는 최대 길이입니다.*

## 힌트

- 원소들의 합이 K를 초과하지 않는다는 조건을 만족하는 가장 긴 구간을 찾아야 합니다.
- 이러한 '합 조건'을 만족하는 최대 길이 문제는 슬라이딩 윈도우(Two Pointers) 기법을 사용하면 O(N) 시간 복잡도로 해결할 수 있습니다.


## 알고리즘 요약

슬라이딩 윈도우 (Sliding Window):
두 포인터(left, right)를 사용하여 현재 부분 배열의 합(current_sum)을 관리합니다. right 포인터를 오른쪽으로 이동시키며 합을 증가시키고, 합이 K를 초과하면 left 포인터를 오른쪽으로 이동시키면서 합을 감소시켜 조건을 다시 만족시킵니다. 이때, 조건을 만족하는 윈도우의 길이(right - left + 1)를 최대값으로 갱신합니다.

## 풀이 해설

풀이 아이디어: 이 문제는 주어진 합 조건(합 <= K)을 만족하는 가장 긴 연속 부분 배열의 길이를 찾는 전형적인 '슬라이딩 윈도우(Sliding Window)' 문제입니다. 원소들이 모두 양수라는 제약 조건을 활용하여, 윈도우를 확장(right 이동)할 때마다 합이 커지므로, 합이 조건을 초과하면 반드시 윈도우를 축소(left 이동)하여 조건을 만족시켜야 합니다.

단계:
1. 초기화: 왼쪽 포인터 `left`를 0으로, 현재 합 `currentSum`을 0으로, 최대 길이 `maxLength`를 0으로 설정합니다.
2. 윈도우 확장 (Right 포인터 이동): 오른쪽 포인터 `right`를 배열의 끝까지 순회하며, `arr[right]`를 `currentSum`에 더합니다.
3. 조건 확인 및 윈도우 축소 (Shrinking): 만약 `currentSum`이 `K`를 초과하게 되면, 윈도우의 조건을 만족시키기 위해 `left` 포인터가 가리키는 원소를 `currentSum`에서 빼줍니다. 그리고 `left` 포인터를 오른쪽으로 1 증가시킵니다. 이 과정을 `currentSum <= K`가 될 때까지 반복합니다.
4. 최대 길이 갱신: 현재 윈도우 `[left, right]`가 조건을 만족하므로, 현재 길이 `(right - left + 1)`를 계산하여 `maxLength`와 비교하고 더 큰 값으로 갱신합니다.
5. 반복: 2~4 단계를 배열의 끝까지 반복합니다.

시간 복잡도 분석: 왼쪽 포인터(`left`)와 오른쪽 포인터(`right`)는 각각 최대 N번의 이동을 합니다. 따라서 총 시간 복잡도는 O(N)입니다. 공간 복잡도는 O(1)입니다.

## 참고 코드 (java)

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        // 빠른 입출력 처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 1. N (배열 크기)
        int n = Integer.parseInt(br.readLine());

        // 2. 배열 arr (원소들이 양수라고 가정)
        long[] arr = new long[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            // 원소는 long으로 저장하는 것이 안전합니다.
            arr[i] = Long.parseLong(st.nextToken());
        }

        // 3. K (최대 합)
        long k = Long.parseLong(br.readLine());

        // 슬라이딩 윈도우 구현
        long currentSum = 0;
        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < n; right++) {
            // 1. 윈도우 확장: right 포인터를 한 칸 이동시키며 합을 증가
            currentSum += arr[right];

            // 2. 조건 위반 시 윈도우 축소: 합이 K를 초과하면 left를 이동
            while (currentSum > k) {
                // left의 원소를 합에서 제외
                currentSum -= arr[left];
                // left 포인터를 오른쪽으로 이동
                left++;
            }

            // 3. 최대 길이 갱신: 현재 윈도우 [left, right]의 길이가 최대값일 수 있음
            // 현재 길이 = right - left + 1
            maxLength = Math.max(maxLength, right - left + 1);
        }

        System.out.println(maxLength);
    }
}
```
