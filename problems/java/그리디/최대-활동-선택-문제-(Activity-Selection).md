# 최대 활동 선택 문제 (Activity Selection)
*java · 그리디 · 보통 · 그리디, 정렬, 자료구조*

## 입출력 환경

효율적인 입출력을 위해 java.io.BufferedReader와 java.util.StringTokenizer를 사용하는 것이 좋습니다.

## 문제

당신은 컨퍼런스 주최 측의 스케줄링 담당자입니다. 주최 측은 여러 개의 회의 일정이 주어졌을 때, 서로 시간이 겹치지 않는 최대 개수의 회의를 선택해야 합니다.

각 회의는 시작 시간과 종료 시간으로 이루어져 있습니다. 주어진 모든 회의 중에서, 시간 간섭 없이 참여할 수 있는 최대 회의 횟수를 구하세요. (시간은 정수이며, 종료 시간이 곧 다음 회의의 시작 시간과 같아도 겹치지 않습니다.)

## 입력

첫 번째 줄에는 회의의 개수 N이 주어집니다. 다음 N개의 줄에는 각 회의의 시작 시간(S)과 종료 시간(E)이 공백으로 구분되어 주어집니다.
(S, E는 모두 1 이상 10^9 이하의 정수입니다.)

## 출력

최대 회의 횟수(정수)를 한 줄로 출력합니다.

## 제약 조건

1 <= N <= 100,000
1 <= S, E <= 10^9
시간 복잡도는 O(N log N) 이하로 요구됩니다.

## 예제 1

**입력**
```
3
1 4
2 5
6 8
```

**출력**
```
2
```

*종료 시간이 가장 빠른 순으로 정렬하면, (1, 4)를 선택하고, 다음으로 겹치지 않는 (6, 8)을 선택하여 총 2개의 회의를 선택할 수 있습니다.*

## 예제 2

**입력**
```
4
1 2
2 3
3 4
1 3
```

**출력**
```
3
```

*시간이 겹치지 않으면서 최대 개수를 선택하는 그리디 알고리즘을 사용합니다. (1, 2) -> (2, 3) -> (3, 4) 순서로 선택 가능합니다.*

## 힌트

- 문제의 핵심은 '그리디(Greedy)' 알고리즘을 적용하는 것입니다.
- 어떤 기준으로 정렬해야 가장 효율적인 선택을 할 수 있는지 고민해보세요. 일반적으로 '종료 시간'을 기준으로 정렬하는 것이 이 유형의 문제에서 핵심입니다.


## 알고리즘 요약

활동 선택 문제(Activity Selection Problem)를 해결하는 전형적인 그리디 알고리즘입니다. 모든 활동(회의)을 '종료 시간'을 기준으로 오름차순 정렬합니다. 그리고 정렬된 목록을 순회하면서, 직전에 선택한 활동의 종료 시간보다 크거나 같은 시작 시간을 가진 활동을 계속해서 선택해 나갑니다. 이 방식으로 선택된 활동의 개수가 최대 개수가 됩니다.

## 풀이 해설

풀이 해설: 아이디어 (Greedy Choice Property)
가장 적은 자원을 사용하고 다음 활동을 시작할 수 있게 해주는 선택을 매번 하는 것이 최적해를 보장합니다. 이 문제에서는 '가장 빨리 끝나는 회의'를 선택하는 것이 최적의 그리디 선택입니다.

단계 1: 데이터 구조화 및 정렬
주어진 N개의 회의 (시작 시간 S, 종료 시간 E)를 객체 형태로 저장합니다. 이 데이터를 **종료 시간(E)을 기준으로 오름차순 정렬**합니다. (만약 종료 시간이 같다면, 시작 시간이 빠른 순으로 정렬해도 무방합니다.)

단계 2: 그리디 선택
1. 첫 번째 회의를 무조건 선택하고, 최대 회의 횟수(count)를 1로, 마지막 선택 회의의 종료 시간(lastEndTime)을 해당 회의의 종료 시간으로 초기화합니다.
2. 정렬된 리스트를 두 번째 회의부터 순회합니다.
3. 현재 회의의 시작 시간(S_i)이 `lastEndTime`보다 크거나 같으면, 이 회의는 이전에 선택된 회의와 겹치지 않습니다. 따라서 이 회의를 선택하고, `count`를 1 증가시키며, `lastEndTime`를 현재 회의의 종료 시간으로 업데이트합니다.
4. 그렇지 않다면 (시간이 겹친다면), 이 회의는 선택하지 않고 다음 회의로 넘어갑니다.

시간 복잡도: 전체 시간 복잡도는 주로 정렬 과정에 의해 결정됩니다. 따라서 O(N log N)이 됩니다. 이는 N이 최대 100,000일 때 충분히 효율적입니다.

## 참고 코드 (java)

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

// 회의 정보를 저장하는 간단한 클래스
class Meeting {
    long start;
    long end;

    public Meeting(long start, long end) {
        this.start = start;
        this.end = end;
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 1. 회의 개수 N 읽기
        int N = Integer.parseInt(br.readLine());
        
        Meeting[] meetings = new Meeting[N];
        
        // 2. 모든 회의 정보 읽기
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long start = Long.parseLong(st.nextToken());
            long end = Long.parseLong(st.nextToken());
            meetings[i] = new Meeting(start, end);
        }

        // 3. 종료 시간(end)을 기준으로 정렬 (핵심 그리디 단계)
        // Comparator를 사용하여 종료 시간 오름차순 정렬
        Arrays.sort(meetings, new Comparator<Meeting>() {
            @Override
            public int compare(Meeting m1, Meeting m2) {
                // Long 타입 비교를 위해 Long.compare 사용
                return Long.compare(m1.end, m2.end);
            }
        });

        // 4. 그리디 알고리즘 적용
        int count = 0;
        // 마지막으로 선택된 회의의 종료 시간 (초기값은 매우 작은 값)
        long lastEndTime = -1;

        for (int i = 0; i < N; i++) {
            Meeting currentMeeting = meetings[i];
            
            // 현재 회의의 시작 시간이 마지막 회의의 종료 시간보다 크거나 같은 경우 (겹치지 않음)
            if (currentMeeting.start >= lastEndTime) {
                // 회의 선택
                count++;
                // lastEndTime 갱신
                lastEndTime = currentMeeting.end;
            }
            // 그렇지 않으면 (겹치면) 무시하고 다음 회의로 넘어감
        }

        // 5. 결과 출력
        System.out.println(count);
    }
}
```
