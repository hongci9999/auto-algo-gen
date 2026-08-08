# 최대 길이의 부분 배열 찾기 (Distinct Element)
*java · 슬라이딩 윈도우 · 보통 · 자료구조, 슬라이딩_윈도우*

## 입출력 환경

효율적인 입출력을 위해 java.util.Scanner 대신 BufferedReader와 StringTokenizer를 사용하는 것이 좋습니다.

## 문제

어떤 배열 $A$와 정수 $K$가 주어집니다. 이 배열에서 'distinct'한 원소의 개수가 최대 $K$개 이하인 가장 긴 부분 배열의 길이를 구하는 문제입니다.

부분 배열은 연속된 요소들로 이루어져야 합니다.

## 입력

첫 번째 줄에 정수 N과 K가 공백으로 구분되어 주어집니다. (N: 배열의 길이, K: 허용되는 최대 distinct 원소 개수)
두 번째 줄에는 공백으로 구분된 N개의 정수 A[0]부터 A[N-1]까지가 순서대로 주어집니다.

## 출력

찾은 가장 긴 부분 배열의 길이를 단일 정수로 출력합니다.

## 제약 조건

1 <= N <= 10^5
1 <= K <= N
1 <= A[i] <= 10^9
시간 복잡도는 O(N)이 권장됩니다.

## 예제 1

**입력**
```
4 2
1 2 3 2
```

**출력**
```
3
```

*A=[1, 2, 3, 2], K=2일 때, 부분 배열 [2, 3, 2]는 distinct 원소가 {2, 3} (2개)로 가장 길며 길이가 3입니다.*

## 예제 2

**입력**
```
5 1
5 5 5 5 5
```

**출력**
```
5
```

*A=[5, 5, 5, 5, 5], K=1일 때, 모든 원소가 동일하여 distinct 원소 개수가 항상 1개이므로 전체 배열의 길이 5가 답입니다.*

## 힌트

- 슬라이딩 윈도우 기법을 사용해 보세요.
- 현재 윈도우 내에 어떤 원소가 몇 번 등장했는지 기록하는 자료구조(예: HashMap)가 필요합니다.


## 알고리즘 요약

슬라이딩 윈도우 (Sliding Window)와 빈도수 맵(Frequency Map)을 활용합니다. 오른쪽 포인터(R)를 이동시키며 윈도우를 확장하고, 윈도우 내 distinct 원소의 개수가 K를 초과하면 왼쪽 포인터(L)를 이동시켜 윈도우를 축소시킵니다.

## 풀이 해설

풀이 아이디어:
이 문제는 '최대 길이'를 찾는 전형적인 슬라이딩 윈도우 문제입니다. 한쪽 끝에서 시작하여 다른 쪽 끝으로 윈도우(부분 배열)를 확장해 나가는 방식이 가장 효율적입니다.

단계별 풀이:
1. 초기화: 왼쪽 포인터 L=0, 오른쪽 포인터 R=0, 최대 길이 max_len=0을 설정합니다. 또한, 현재 윈도우 [L, R]에 포함된 원소들의 빈도수를 저장할 HashMap(원소 값 -> 개수)과 현재 distinct 원소의 개수를 추적할 변수 distinct_count를 초기화합니다.
2. 윈도우 확장 (R 이동): R을 1씩 증가시키며 A[R]을 윈도우에 포함시킵니다. HashMap에 A[R]을 추가하고 카운트를 1 증가시킵니다.
3. 제약 조건 확인 및 윈도우 축소 (L 이동): 만약 distinct_count가 K를 초과하게 되면, 현재 윈도우는 유효하지 않습니다. 따라서 L 포인터를 움직여 윈도우를 반드시 축소해야 합니다. A[L]의 빈도수를 HashMap에서 1 감소시키고, 이 원소의 카운트가 0이 되었다면 distinct_count를 1 감소시킵니다.
4. 최대 길이 업데이트: 윈도우 [L, R]이 유효한 상태(distinct_count <= K)일 때마다, 현재 윈도우의 길이 (R - L + 1)을 계산하여 max_len과 비교하고 최댓값을 기록합니다.
5. 반복 종료: R이 배열 끝에 도달할 때까지 2~4단계를 반복하면 됩니다.

시간 복잡도 분석:
L 포인터와 R 포인터는 각각 N번만 움직이며, 각 단계에서 상수 시간($O(1)$) 연산만을 수행합니다. 따라서 전체 시간 복잡도는 $O(N)$이 되어 매우 효율적입니다.

## 참고 코드 (java)

```java
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // 첫 번째 줄: N과 K 입력
        if (!scanner.hasNextInt()) return;
        int n = scanner.nextInt();
        int k = scanner.nextInt();

        // 두 번째 줄: 배열 A 입력
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }

        System.out.println(solve(a, k));
    }

    /**
     * distinct 원소가 K 이하인 가장 긴 부분 배열의 길이를 찾습니다.
     */
    public static int solve(int[] a, int k) {
        // 맵: 값 -> 빈도수 (원소 값을 키로 사용)
        Map<Integer, Integer> freqMap = new HashMap<>();
        int left = 0; // 왼쪽 포인터
        int maxLength = 0;

        // 오른쪽 포인터를 이동시키며 윈도우 확장 (R: Right)
        for (int right = 0; right < a.length; right++) {
            int currentElement = a[right];
            
            // 1. 현재 원소 추가 및 빈도수 업데이트
            freqMap.put(currentElement, freqMap.getOrDefault(currentElement, 0) + 1);
            
            // 2. 제약 조건 확인: distinct 개수가 K를 초과하면 윈도우 축소 (L 이동)
            while (freqMap.size() > k) {
                int leftElement = a[left];
                
                // 왼쪽 원소를 제거하고 빈도수 감소
                int count = freqMap.get(leftElement); 
                freqMap.put(leftElement, count - 1);
                
                // 카운트가 0이 되면 distinct 개수에서 제외됨
                if (count - 1 == 0) {
                    freqMap.remove(leftElement);
                }
                
                // 왼쪽 포인터 이동
                left++;
            }
            
            // 3. 최대 길이 업데이트: 현재 유효한 윈도우의 길이를 계산
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}
```
