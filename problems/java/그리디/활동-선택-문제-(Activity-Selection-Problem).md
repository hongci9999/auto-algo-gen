# 활동 선택 문제 (Activity Selection Problem)
*java · 그리디 · 보통 · 정렬, 탐욕 알고리즘*

## 입출력 환경

Java 환경에서는 BufferedReader와 StringTokenizer를 사용하여 빠른 입력을 처리하는 것이 권장됩니다.

## 문제

N개의 활동이 주어집니다. 각 활동은 시작 시간과 종료 시간을 가집니다. 활동 간의 시간 구간이 겹치지 않도록 하는 최대 활동의 개수를 구하는 문제입니다.

두 활동 A와 B가 겹친다는 것은 두 활동의 시간 구간 [start_A, end_A]와 [start_B, end_B]의 교집합이 비어있지 않다는 의미입니다. 즉, max(start_A, start_B) < min(end_A, end_B)일 때 겹칩니다.

문제는 시간 간격이 겹치지 않는 최대 활동의 개수를 구하는 것입니다.

## 입력

첫째 줄에 활동의 개수 N (1 ≤ N ≤ 100,000)이 주어집니다.
다음 N개의 줄에 걸쳐 각 활동의 시작 시간 s와 종료 시간 f가 공백으로 구분되어 주어집니다. (1 ≤ s, f ≤ 10,000,000)

## 출력

겹치지 않는 최대 활동의 개수를 정수 형태로 출력합니다.

## 제약 조건

N: 1부터 100,000까지. 시간 복잡도는 O(N log N)을 목표로 합니다.

## 예제 1

**입력**
```
4
1 4
3 5
0 6
5 7
```

**출력**
```
2
```

*활동 (1, 4)와 (5, 7) 또는 (0, 6)과 (5, 7)처럼 최대 2개를 선택할 수 있습니다.*

## 예제 2

**입력**
```
5
1 2
2 3
3 4
1 3
4 5
```

**출력**
```
4
```

*선택 순서: (1, 2) -> (2, 3) -> (3, 4) -> (4, 5)로 총 4개를 선택할 수 있습니다.*

## 힌트

- 문제를 해결하기 위해 모든 활동을 특정 기준으로 정렬해야 합니다.
- 탐욕적인 선택이 중요하며, 어떤 순서로 정렬해야 가장 효율적인 선택을 할 수 있는지 고민해보세요.


## 알고리즘 요약

이 문제는 전형적인 그리디(Greedy) 알고리즘 문제입니다. 최대 개수의 활동을 선택하려면, 항상 '가장 빨리 끝나는' 활동을 선택하는 것이 최적의 선택임을 증명할 수 있습니다. 따라서 활동들을 종료 시간(Finish Time) 기준으로 오름차순 정렬한 후, 첫 번째 활동을 선택하고, 이후 활동들 중 현재 선택된 활동의 종료 시간보다 시작 시간이 크거나 같은 활동을 순차적으로 선택합니다.

## 풀이 해설

풀이 해설: 활동 선택 문제는 탐욕 알고리즘을 이용합니다. 핵심 아이디어는 '가장 빨리 끝나는 활동'을 항상 선택하는 것이 전체 최대 활동 개수를 보장한다는 것입니다.

1. **데이터 구조화 및 정렬 (Sorting):** 모든 활동(Start Time, Finish Time)을 저장합니다. 그리고 이 활동들을 **종료 시간(Finish Time)을 기준**으로 오름차순 정렬합니다. 종료 시간이 같은 활동은 시작 시간을 기준으로 정렬해도 무방합니다.
2. **탐욕적 선택 (Greedy Selection):** 정렬된 활동 리스트를 순회합니다. 첫 번째 활동은 무조건 선택합니다. 이 활동의 종료 시간을 `lastFinishTime`으로 기록합니다.
3. **최대화 과정:** 다음 활동 $i$에 대해, 만약 활동 $i$의 시작 시간 $S_i$가 `lastFinishTime`보다 크거나 같다면 (즉, 겹치지 않는다면), 이 활동 $i$를 선택합니다. 활동 개수를 1 증가시키고, `lastFinishTime`을 활동 $i$의 종료 시간 $F_i$로 업데이트합니다.
4. **반복:** 이 과정을 모든 활동에 대해 반복하여 최대 활동 개수를 구합니다.

*시간 복잡도:* 정렬에 $O(N 	imes 	ext{log } N)$이 소요되며, 이후 순차 탐색은 $O(N)$이므로, 전체 시간 복잡도는 $O(N 	ext{ log } N)$입니다.

## 참고 코드 (java)

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

// 활동 정보를 담는 클래스
class Activity {
    int start;
    int end;

    public Activity(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입력을 위한 설정
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 첫 줄에서 N (활동 개수) 읽기
        String line = br.readLine();
        if (line == null || line.isEmpty()) {
            System.out.println(0);
            return;
        }
        int N = Integer.parseInt(line.trim());

        Activity[] activities = new Activity[N];
        
        // 나머지 N줄에서 활동 정보 읽기
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            activities[i] = new Activity(start, end);
        }

        // 1. 종료 시간(end)을 기준으로 오름차순 정렬
        Arrays.sort(activities, new Comparator<Activity>() {
            @Override
            public int compare(Activity a1, Activity a2) {
                // 종료 시간을 기준으로 비교 (a1.end - a2.end)
                return Integer.compare(a1.end, a2.end);
            }
        });

        // 2. 그리디 선택 알고리즘 실행
        int count = 1; // 최소 1개는 선택 가능 (N >= 1 가정)
        int lastFinishTime = activities[0].end;

        for (int i = 1; i < N; i++) {
            Activity current = activities[i];
            
            // 현재 활동의 시작 시간이 마지막으로 선택된 활동의 종료 시간보다 크거나 같으면 겹치지 않음
            if (current.start >= lastFinishTime) {
                count++;
                lastFinishTime = current.end;
            }
        }

        System.out.println(count);
    }
}
```
