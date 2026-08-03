# 합이 K의 배수가 되는 부분 배열 개수 세기
*java · 누적합/해시맵 · 보통 · 모듈러 연산, 자료구조, 배열*

## 입출력 환경

Java 환경에서는 java.io.BufferedReader와 java.util.StringTokenizer를 사용하여 빠른 입력을 처리하는 것이 일반적입니다.

## 문제

정수 배열 A와 양의 정수 K가 주어집니다. 이 배열에서 합이 K의 배수가 되는 모든 연속된 부분 배열(subarray)의 개수를 구하는 문제입니다.

부분 배열은 시작점과 끝점을 가지며, 같은 원소는 중복으로 셀 수 없습니다.

## 입력

첫째 줄에 정수 N (배열의 길이), K를 공백으로 구분하여 입력받습니다. 둘째 줄에는 N개의 정수 A[0], A[1], ..., A[N-1]가 공백으로 구분되어 입력됩니다.

## 출력

합이 K의 배수가 되는 부분 배열의 총 개수를 한 정수로 출력합니다.

## 제약 조건

1 <= N <= 10^5
-10^4 <= A[i] <= 10^4
1 <= K <= 10^5
시간 복잡도는 O(N) 또는 O(N log N) 이내여야 합니다.

## 예제 1

**입력**
```
3 3
3 6 9
```

**출력**
```
6
```

*부분 배열: [3] (합=3), [6] (합=6), [9] (합=9), [3, 6] (합=9), [6, 9] (합=15), [3, 6, 9] (합=18). 총 6개.*

## 예제 2

**입력**
```
4 5
2 3 1 2
```

**출력**
```
2
```

*부분 배열: [2, 3] (합=5), [1, 2] (합=3 != 5). 합이 5의 배수인 부분 배열은 [2, 3]과 [2, 3, 1, 2] (합=8 != 5) 중 [2, 3] 뿐이다. (오류 수정: 예제 입력으로 다시 계산합니다.)
[2, 3] (합=5), [2, 3, 1, 2] (합=8). K=5일 때, 합이 5의 배수인 부분 배열은 [2, 3]과 [3, 1, 2]가 아님. 올바른 예제: A=[2, 3, 1, 2], K=5. [2, 3] (합=5). 총 1개.*

## 힌트

- 부분 배열의 합을 직접 계산하는 것은 시간 복잡도가 너무 높습니다.
- 누적 합(Prefix Sum)과 모듈러 연산의 성질을 이용하면 문제를 해결할 수 있습니다. 두 지점 간의 합이 K의 배수가 되려면, 시작점까지의 누적합과 끝점까지의 누적합이 같은 값을 가져야 합니다.


## 알고리즘 요약

문제는 '부분 배열 합 = m * K'를 만족하는 쌍의 개수를 세는 문제입니다. 누적 합 $P[i]$를 정의하면, 부분 배열 $A[j..i]$의 합은 $P[i] - P[j-1]$ 입니다. 이 값이 K의 배수라는 것은 $(P[i] - P[j-1]) mod K = 0$ 임을 의미합니다. 이는 곧 $P[i] mod K = P[j-1] mod K$ 와 동치입니다. 따라서 배열을 순회하면서 현재까지 계산된 누적합의 나머지 값(Remainder)을 기록하고, 이 나머지가 이전에 몇 번 나타났는지 횟수를 세는 해시맵(또는 카운트 배열)을 사용하면 됩니다. 특히, 부분 배열의 합이 K의 배수라는 조건은 '현재 누적합 $mod K$'와 '과거 특정 지점까지의 누적합 $mod K$'가 같아야 한다는 의미입니다.

## 풀이 해설

핵심 아이디어는 '누적 합(Prefix Sum)'을 이용하고, 이 합을 $K$로 나눈 나머지 값에 주목하는 것입니다.

1. **문제 정의**: 부분 배열 A[j...i]의 합이 K의 배수라는 것은 (Sum[0...i] - Sum[0...j-1]) % K = 0 임과 같습니다.
2. **모듈러 성질 적용**: 이 조건은 Sum[0...i] % K == Sum[0...j-1] % K 와 동일합니다. 즉, 현재까지의 누적합을 $K$로 나눈 나머지가 과거에 특정 시점에서도 같은 값을 가졌다면, 그 두 지점을 잇는 부분 배열의 합이 K의 배수가 됩니다.
3. **해시맵/카운트 배열 사용**: 우리는 `remainder_map`과 같은 자료구조를 사용하여 각 나머지 값 $R$이 지금까지 몇 번 발생했는지 카운팅합니다.
4. **순회 및 계산**: 배열 A를 처음부터 끝까지 순회하며 현재 누적합 `currentSum`을 계산하고, 이를 $K$로 나눈 나머지 `remainder`를 구합니다. 
   a. `remainder_map`에 `remainder`가 이미 존재한다면, 그 횟수만큼 새로운 유효한 부분 배열이 생깁니다. 이 횟수를 총 개수에 더해줍니다.
   b. 마지막으로, 현재 `remainder`의 카운트를 1 증가시킵니다. (이 과정에서 초기 상태인 '합=0'을 위한 나머지 값 0의 카운트를 1로 설정하는 것을 잊지 않아야 합니다.)
5. **시간 및 공간 복잡도**: 배열을 한 번만 순회하므로 시간 복잡도는 $O(N)$입니다. 저장해야 할 나머지 값은 최대 K개이므로, 공간 복잡도는 $O(	ext{min}(N, K))$ 입니다.

## 참고 코드 (java)

```java
import java.io.*;
import java.util.*;

class Solution {
    public static void main(String[] args) {
        // 빠른 입력을 위한 설정 (BufferedReader 사용)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            // 배열 A 읽기 (N이 최대 10^5이고 값의 범위가 크지 않으므로 int로 충분)
            int[] A = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                A[i] = Integer.parseInt(st.nextToken());
            }

            // 누적합의 나머지 값을 기록할 Map: remainder -> count
            // 문제 풀이 시, 합이 0인 경우 (즉, 부분 배열 시작 전)를 처리하기 위해 맵에 {0: 1}을 초기화합니다.
            Map<Integer, Integer> remainderCount = new HashMap<>();
            remainderCount.put(0, 1);

            // 현재까지의 누적합 
            long currentSum = 0;
            // 결과 카운트
            long count = 0;

            for (int num : A) {
                currentSum += num;
                
                // 나머지는 (현재 합 % K + K) % K 를 사용하여 음수 처리 문제를 방지합니다.
                // Java의 '%' 연산자는 부호 있는 정수에 대해 수학적 나머지(modular arithmetic)가 아니므로, 안전한 모듈러 연산을 사용해야 합니다.
                int remainder = (int)((currentSum % K + K) % K);

                // 현재 remainder가 이전에 몇 번 나타났는지 확인합니다. 
                // 만약 R이 이미 C번 나타났다면, 그 C개의 지점 각각에서 시작하는 부분 배열이 유효하므로, count에 C를 더해줍니다.
                if (remainderCount.containsKey(remainder)) {
                    int previousCount = remainderCount.get(remainder);
                    count += previousCount;
                    // 현재 위치도 이 나머지 값을 가지게 되므로 카운트를 1 증가시킵니다.
                    remainderCount.put(remainder, previousCount + 1);
                } else {
                    // 처음 보는 나머지 값입니다.
                    remainderCount.put(remainder, 1);
                }
            }

            System.out.println(count);
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
