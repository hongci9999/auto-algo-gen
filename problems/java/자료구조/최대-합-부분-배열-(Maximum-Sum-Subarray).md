# 최대 합 부분 배열 (Maximum Sum Subarray)
*java · 자료구조 · 보통 · 배열, DP, Kadane's*

## 입출력 환경

Java에서 입력을 받을 때는 BufferedReader와 StringTokenizer를 사용하는 것이 성능상 유리합니다. 배열의 원소값이 10^9까지 가능하므로, 누적 합을 저장할 변수는 long 타입을 사용해야 합니다.

## 문제

어떤 정수 배열 `A`가 주어집니다. 이 배열의 연속된 부분 배열(Subarray) 중 합이 가장 큰 부분 배열의 합을 구하는 문제입니다.

부분 배열은 최소한 하나의 원소를 포함해야 합니다. 따라서 모든 원소가 음수일 경우에도, 가장 큰 값(절댓값이 가장 작은 음수)을 결과로 반환해야 합니다.

## 입력

첫 번째 줄에는 배열의 길이 N이 주어지며, 두 번째 줄에는 공백으로 구분된 N개의 정수 원소들이 주어집니다.

## 출력

가장 큰 합을 가진 부분 배열의 합을 하나의 정수 값으로 출력합니다.

## 제약 조건

N의 범위: 1 <= N <= 100,000
원소값의 범위: -10^9 <= A[i] <= 10^9
시간 복잡도: O(N) 또는 O(N log N) 이하

## 예제 1

**입력**
```
5
1 -2 3 4 -1
```

**출력**
```
7
```

*배열 [3, 4]의 합이 7로 가장 큽니다.*

## 예제 2

**입력**
```
4
-10 -2 -5 -1
```

**출력**
```
-1
```

*모든 원소가 음수이므로, 가장 큰 값인 -1이 결과입니다.*

## 예제 3

**입력**
```
3
5 1 4
```

**출력**
```
10
```

*배열 전체 [5, 1, 4]의 합이 가장 큽니다.*

## 힌트

- 단순히 모든 원소의 합을 구할 필요는 없습니다. 특정 부분 배열의 합만 최대가 될 수 있습니다.
- 배열을 순차적으로 탐색하면서 '현재까지의 합'을 어떻게 갱신할지 생각해 보세요. 이 '현재까지의 합'은 음수일 때 리셋하는 로직이 핵심입니다.


## 알고리즘 요약

카다네 알고리즘 (Kadane's Algorithm)을 활용합니다. 배열을 한 번만 순회하면서, 현재 위치까지의 합(Current Max Sum)을 계산하고, 이 값과 지금까지 기록된 최대 합(Overall Max Sum)을 비교하여 최대 합을 갱신합니다. 만약 현재까지의 합이 음수가 된다면, 그 합은 이후의 합에 기여하는 바가 크지 않으므로 0으로 리셋(혹은 현재 원소값으로 재시작)하는 로직이 필요합니다.

## 풀이 해설

이 문제는 전형적인 '최대 합 부분 배열' 문제이며, O(N) 시간 복잡도로 해결할 수 있는 카다네 알고리즘(Kadane's Algorithm)을 적용합니다.

**아이디어:**
배열을 순차적으로 탐색하면서, '현재 원소까지 포함하여 만들 수 있는 최대 합'을 누적하여 추적합니다. 이 값이 음수라는 것은, 이 합을 이전 단계에 포함시키는 것보다 현재 원소부터 새로 시작하는 것이 더 좋다는 의미입니다.

**단계별 풀이:**
1. **변수 초기화:** `max_so_far` (전체 최대 합)와 `current_max` (현재까지의 최대 합)를 배열의 첫 번째 원소로 초기화합니다. 두 변수 모두 `long` 타입을 사용해야 합니다.
2. **순회:** 배열의 두 번째 원소부터 끝까지 순회합니다.
3. **`current_max` 갱신:** 현재 원소 `A[i]`를 사용하여 `current_max`를 갱신합니다. 이때, `current_max`는 `A[i]` 또는 `current_max + A[i]` 중 더 큰 값을 가지도록 설정합니다. (만약 `current_max + A[i]`가 음수라면, 시작점을 다시 `A[i]`로 잡는 것이 이득입니다).
4. **`max_so_far` 갱신:** `max_so_far`는 `max_so_far`와 `current_max` 중 더 큰 값을 가지도록 갱신합니다. 이 값이 최종 답이 됩니다.

**시간 복잡도:** 배열을 단 한 번만 순회하므로 시간 복잡도는 O(N)입니다. 공간 복잡도는 O(1)입니다.

## 참고 코드 (java)

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // BufferedReader를 사용하여 빠른 입력을 받습니다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 1. N (배열 길이) 읽기
        String line1 = br.readLine();
        if (line1 == null || line1.isEmpty()) {
            return;
        }
        int N = Integer.parseInt(line1.trim());

        // 2. 배열 원소 읽기
        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] arr = new long[N];
        for (int i = 0; i < N; i++) {
            // 원소값이 10^9까지 가능하므로 long 타입으로 저장합니다.
            arr[i] = Long.parseLong(st.nextToken());
        }

        // 카다네 알고리즘 구현
        // 전체 최대 합 (최종 결과)
        long maxSoFar = arr[0]; 
        // 현재까지의 최대 합
        long currentMax = arr[0]; 

        for (int i = 1; i < N; i++) {
            // 1. currentMax 갱신: 현재 원소부터 새로 시작하는 것이 유리한지, 아니면 기존 합에 더하는 것이 유리한지 판단
            // Math.max(A[i], currentMax + A[i])를 통해 최적의 선택을 합니다.
            currentMax = Math.max(arr[i], currentMax + arr[i]);
            
            // 2. maxSoFar 갱신: 전역 최대 합 갱신
            maxSoFar = Math.max(maxSoFar, currentMax);
        }

        System.out.println(maxSoFar);
    }
}
```
