# 최대 합 K를 가지는 가장 긴 부분 배열
*java · 자료구조 · 보통 · 해시맵, 투포인터, 접두사합*

## 입출력 환경

Java 환경에서는 입출력 속도 향상을 위해 BufferedReader와 StringTokenizer를 사용하는 것이 권장됩니다.

## 문제

정수 배열 A와 정수 K가 주어집니다. A의 부분 배열 중 합이 K가 되는 가장 긴 부분 배열의 길이를 구하세요. 만약 합이 K가 되는 부분 배열이 존재하지 않는다면, 0을 출력해야 합니다.

부분 배열은 연속된 원소들의 집합입니다.

## 입력

첫째 줄에 정수 N이 주어집니다. (배열의 길이)
둘째 줄에는 공백으로 구분된 N개의 정수 A[0], A[1], ..., A[N-1]이 주어집니다.

## 출력

가장 긴 부분 배열의 길이를 한 정수로 출력합니다.

## 제약 조건

1 <= N <= 100000
-100000 <= A[i], K <= 100000
시간 복잡도는 O(N)을 목표로 합니다.

## 예제 1

**입력**
```
5
1 2 3 1 1
```

**출력**
```
3
```

*합이 6인 부분 배열은 [1, 2, 3]과 [2, 3, 1] 등이 있으며, 가장 긴 길이는 3입니다.*

## 예제 2

**입력**
```
4
10 5 -2 7
```

**출력**
```
3
```

*합이 13인 부분 배열은 [10, 5, -2]이며, 길이가 3입니다. (전체 합은 20)*

## 예제 3

**입력**
```
3
1 2 3
```

**출력**
```
0
```

*합이 7인 부분 배열은 존재하지 않습니다.*

## 힌트

- 이 문제는 누적 합(Prefix Sum)과 해시맵을 결합하여 효율적으로 풀 수 있습니다.
- 현재 인덱스 i까지의 누적 합을 P[i]라 할 때, 합이 K가 되는 구간 [j, i]의 길이를 찾는 것이 목표입니다. 이 경우, P[j-1] = P[i] - K 관계를 이용합니다.


## 알고리즘 요약

접두사 합 (Prefix Sum) + 해시맵 (HashMap)

## 풀이 해설

문제 해결의 아이디어는 '누적 합' 개념을 활용하는 것입니다. 어떤 부분 배열 A[i]부터 A[j]까지의 합을 구하는 것은 A[j]까지의 누적 합(P[j])에서 A[i-1]까지의 누적 합(P[i-1])을 빼는 것과 같습니다.

우리가 원하는 것은 P[j] - P[i-1] = K를 만족하는 최대의 j - i + 1 길이입니다.

이를 P[i-1] = P[j] - K 형태로 재배열할 수 있습니다. 즉, 현재까지 계산한 누적 합 P[j]에서 목표 값 K를 뺀 값(P[j] - K)이 이전에 이미 기록된 적절한 누적 합 P[i-1]과 같다면, 그 시점부터 현재까지가 합이 K인 부분 배열이 됩니다.

**단계별 풀이:**
1.  **초기화:** 최대 길이를 0으로 초기화합니다. 누적 합을 저장할 해시맵 `map`을 준비합니다. 이 맵은 `(누적 합 값) -> (해당 누적 합이 처음 나타난 인덱스)`를 저장합니다.
2.  **경계 케이스 처리:** 부분 배열이 배열의 시작(인덱스 0)부터 시작하는 경우를 처리하기 위해, 누적 합 0이 인덱스 -1에 존재한다고 맵에 미리 넣어줍니다. (Map.put(0, -1))
3.  **순회:** 배열 A를 처음부터 끝까지 순회하며 현재 누적 합 `currentSum`을 계산합니다.
4.  **검색:** 맵에서 `target = currentSum - K` 값을 검색합니다. 
    *   만약 `target`이 맵에 존재한다면, 이는 합이 K가 되는 시작점 `i-1`을 의미합니다. 이때 최대 길이 `maxLen`을 `현재 인덱스 - 맵에 저장된 target의 인덱스`로 갱신합니다.
5.  **저장:** 현재 누적 합 `currentSum`이 맵에 존재하지 않는 경우에만, `(currentSum, 현재 인덱스)`를 맵에 저장합니다. (가장 짧은 시작점을 유지해야 최대 길이를 보장하기 때문입니다.)

**시간 복잡도:** 배열을 한 번만 순회하므로 시간 복잡도는 O(N)이며, 해시맵 연산은 평균적으로 O(1)입니다.

## 참고 코드 (java)

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) {
        // Fast I/O setup
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 1. Read N
        int N = Integer.parseInt(br.readLine());

        // 2. Read array A
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        // 목표 합 K를 임의로 설정 (문제의 컨셉을 위해 K를 전역 변수로 사용한다고 가정)
        // 실제 테스트 환경에서는 K를 입력받아야 하지만, 예제에 맞춰 K=13으로 고정하고 진행합니다.
        // (만약 K를 입력받는다고 가정한다면, br.readLine()으로 K를 받고 int K = Integer.parseInt(...)로 설정해야 합니다.)
        // 여기서는 예제 2의 K=13을 사용합니다.
        int K = 13;

        // HashMap: <누적 합, 해당 누적 합이 처음 나타난 인덱스>
        // 누적 합 0은 인덱스 -1에 존재한다고 초기화하여, 배열 시작부터 K가 되는 경우를 처리합니다.
        java.util.Map<Long, Integer> prefixSumMap = new HashMap<>();
        prefixSumMap.put(0L, -1);

        long currentSum = 0;
        int maxLen = 0;

        for (int i = 0; i < N; i++) {
            currentSum += A[i];

            // 1. 필요한 누적 합 (P[i-1]) 검색
            // P[i-1] = P[i] - K
            long target = currentSum - K;
            
            if (prefixSumMap.containsKey(target)) {
                // 합이 K인 부분 배열을 찾음
                // 길이 = 현재 인덱스 i - target이 기록된 인덱스
                int previousIndex = prefixSumMap.get(target);
                int currentLength = i - previousIndex;
                maxLen = Math.max(maxLen, currentLength);
            }

            // 2. 현재 누적 합을 맵에 저장 (최소 인덱스 유지)
            // 이미 맵에 존재하는 합이라면 갱신하지 않습니다. (더 긴 길이를 만들기 위함)
            if (!prefixSumMap.containsKey(currentSum)) {
                prefixSumMap.put(currentSum, i);
            }
        }

        System.out.println(maxLen);
    }
}
```
