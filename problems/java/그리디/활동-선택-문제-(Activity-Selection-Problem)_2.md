# 활동 선택 문제 (Activity Selection Problem)
*java · 그리디 · 보통 · 그리디, 정렬*

## 입출력 환경

Java 환경에서는 입력 속도를 위해 java.io.BufferedReader와 java.util.StringTokenizer를 사용하는 것이 좋습니다.

## 문제

당신은 여러 개의 활동(Activity) 목록을 받았습니다. 각 활동은 시작 시간, 종료 시간, 그리고 가치를 가집니다. 주어진 활동들 중 서로 시간이 겹치지 않으면서(비겹침) 전체 가치의 합이 최대가 되는 활동들의 조합을 찾아야 합니다. 

활동 A는 (시작 시간, 종료 시간, 가치)로 표현됩니다. 선택한 활동들의 총 가치를 구하시오.

주의: 모든 활동은 동시에 진행될 수 없으며, 선택된 활동들 간의 시간 간격이 0이거나 양수여야 합니다. 즉, 활동 A가 끝나고 활동 B가 시작할 때, B의 시작 시간이 A의 종료 시간보다 크거나 같아야 합니다.

## 입력

첫 번째 줄에는 활동의 개수 N이 주어집니다. 이후 N개의 줄에 걸쳐 각 활동의 (시작 시간, 종료 시간, 가치)가 공백으로 구분되어 주어집니다.

## 출력

선택된 활동들의 최대 가치 합을 출력합니다.

## 제약 조건

1. N: 1부터 1000까지
2. 시간 및 가치: 1부터 100,000까지
3. 시간 복잡도: O(N log N) 또는 O(N^2) 이하가 권장됩니다.

## 예제 1

**입력**
```
4
1 3 5
2 5 7
4 6 10
6 8 3
```

**출력**
```
22
```

*가장 먼저 끝나는 활동(1-3, 가치 5)을 선택하고, 다음으로 겹치지 않는 활동(4-6, 가치 10)을 선택한 후, 마지막 활동(6-8, 가치 3)을 선택하여 총 5+10+3 = 18입니다. 하지만 이 문제에서는 DP 접근이 필요하며, 최대 가치는 (1-3, 가치 5) + (2-5, 가치 7)는 겹치므로 선택 불가. 최적 조합은 (1-3, 가치 5) + (4-6, 가치 10) + (6-8, 가치 3)이 아닙니다. (1-3, 가치 5)와 (2-5, 가치 7) 중 더 큰 가치를 가진 것을 선택하고, 그 이후의 조합을 찾는 것이 핵심입니다. (2-5, 가치 7)을 선택하고, 다음으로 겹치지 않는 활동 (6-8, 가치 3)을 선택하여 총 10이 최대입니다. (다만, 문제의 난이도를 고려하여 그리디로 풀기 위해, 가장 끝나는 시간이 빠른 활동을 선택하는 방식으로 진행합니다. 이 예제는 DP가 필요하지만, 그리디 원칙을 따르기 위해 (1-3) -> (4-6) -> (6-8)을 선택하여 18이 가장 합리적인 그리디 답입니다. (최대 가치: 18)*

## 예제 2

**입력**
```
3
1 2 10
2 3 10
3 4 10
```

**출력**
```
20
```

*활동은 시간이 겹치지 않게 선택되어야 합니다. (1-2)를 선택하고, 다음으로 겹치지 않는 활동 (3-4)을 선택하는 것이 가장 좋습니다. (10 + 10 = 20)*

## 힌트

- 활동들을 어떤 기준으로 정렬할지 생각해보세요.
- 단순히 가치가 큰 활동부터 선택하는 것은 틀릴 수 있습니다. 시간 제약 조건을 고려해야 합니다.


## 알고리즘 요약

이 문제는 '활동 선택 문제'의 가치 기반 변형입니다. 일반적인 활동 선택 문제는 단순히 겹치지 않는 활동의 최대 '개수'를 찾는 그리디 문제입니다. 하지만 가치가 포함된 경우, 단순 그리디로는 최적해를 찾기 어려워 DP(Dynamic Programming)가 필요합니다. 그러나 난이도를 '보통'으로 유지하기 위해, 활동들을 종료 시간이 빠른 순서대로 정렬한 뒤, 현재 활동이 이전에 선택된 활동과 겹치는지 확인하며 누적 가치를 계산하는 '강화된 그리디' 접근을 사용합니다.

## 풀이 해설

풀이 전략: 이 문제는 엄밀히 말하면 '가중치 구간 스케줄링(Weighted Interval Scheduling)' 문제로, 일반적으로 동적 계획법(DP)을 사용합니다. 그러나 주어진 난이도와 제약 조건 내에서 그리디 원칙을 적용하여 풀이합니다. 핵심 아이디어는 '종료 시간이 빠른 활동'을 우선적으로 고려하는 것입니다.

1. 데이터 구조화: 모든 활동 (시작 시간, 종료 시간, 가치)을 저장합니다.
2. 정렬: 활동들을 '종료 시간'을 기준으로 오름차순 정렬합니다. 종료 시간이 빠를수록 다음 활동을 선택할 여유 공간이 많기 때문입니다.
3. DP 배열 정의: `dp[i]`를 'i번째 활동까지 고려했을 때 얻을 수 있는 최대 가치'라고 정의합니다.
4. DP 점화식: `dp[i]`를 계산하기 위해, i번째 활동을 선택할지 말지를 결정합니다.
    a. i번째 활동을 선택하는 경우: 이 활동의 가치 + (i번째 활동과 겹치지 않으면서 최대 가치를 얻을 수 있는 가장 마지막 활동 j까지의 최대 가치)를 가져옵니다. 즉, `value[i] + dp[p(i)]` (여기서 `p(i)`는 i보다 시작 시간이 빠르고 i와 겹치지 않는 가장 마지막 활동 인덱스).
    b. i번째 활동을 선택하지 않는 경우: `dp[i-1]`을 가져옵니다.
5. 최대값 선택: `dp[i] = max(dp[i-1], value[i] + dp[p(i)])`를 반복합니다. 최종 결과는 `dp[N-1]`입니다.

시간 복잡도: 정렬에 O(N log N), DP 계산에 O(N^2) (혹은 이진 탐색을 이용해 O(N log N))이 소요되므로, 전체 시간 복잡도는 O(N^2) 또는 O(N log N)입니다.

## 참고 코드 (java)

```java
import java.io.*;
import java.util.*;

class Activity {
    int start, end, value;
    public Activity(int s, int e, int v) {
        this.start = s;
        this.end = e;
        this.value = v;
    }
}

public class Main {

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            int N = Integer.parseInt(br.readLine());
            Activity[] activities = new Activity[N];

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                int value = Integer.parseInt(st.nextToken());
                activities[i] = new Activity(start, end, value);
            }

            // 1. 종료 시간 기준으로 정렬 (Greedy/DP 접근의 핵심)
            Arrays.sort(activities, Comparator.comparingInt(a -> a.end));

            // 2. DP 배열: dp[i]는 i번째 활동까지 고려했을 때의 최대 가치
            long[] dp = new long[N];

            for (int i = 0; i < N; i++) {
                // 1. 현재 활동을 선택하지 않았을 때의 최대 가치 (이전 단계까지의 최대값)
                long notSelected = (i == 0) ? 0 : dp[i - 1];
                long selectedValue = activities[i].value;

                // 2. 현재 활동을 선택할 경우의 최대 가치
                // 겹치지 않는 가장 가까운 이전 활동 j를 찾기 위해 이진 탐색을 사용합니다.
                // (시작 시간이 i의 종료 시간보다 작거나 같은 활동 중 최대 가치를 가진 dp[j]를 찾음)
                long prevMaxProfit = 0;
                int bestIndex = -1;
                
                // 이진 탐색을 통해 activities[i]가 겹치지 않는 가장 늦은 활동 j를 찾음
                // 활동 j의 종료 시간이 activities[i]의 시작 시간보다 작거나 같아야 함.
                int low = 0;
                int high = i - 1;
                int latestNonOverlappingIndex = -1;

                while (low <= high) {
                    int mid = low + (high - low) / 2;
                    if (activities[mid].end <= activities[i].start) {
                        // 조건을 만족하는 활동을 찾았으므로, 더 뒤쪽을 탐색
                        latestNonOverlappingIndex = mid;
                        low = mid + 1;
                    } else {
                        // 너무 늦게 끝나는 활동이므로, 더 앞쪽을 탐색
                        high = mid - 1;
                    }
                }

                if (latestNonOverlappingIndex != -1) {
                    // 겹치지 않는 가장 마지막 활동까지의 최대 가치(dp[latestNonOverlappingIndex])를 가져옴
                    prevMaxProfit = dp[latestNonOverlappingIndex];
                }
                
                long selected = selectedValue + prevMaxProfit;
                
                // 3. dp[i] 업데이트: 선택하는 경우와 선택하지 않는 경우 중 큰 값을 선택
                dp[i] = Math.max(notSelected, selected);
            }

            System.out.println(dp[N - 1]);

        } catch (Exception e) {
            // 예외 처리 로직 (실제 코딩 테스트에서는 생략 가능)
        }
    }
}
```
