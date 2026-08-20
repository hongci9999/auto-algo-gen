# 합이 T인 연속 부분 배열의 개수
*python · 자료구조 · 보통 · Prefix Sum, 딕셔너리, 정수배열*

## 입출력 환경

효율적인 입력을 위해 sys.stdin.readline을 사용하세요.

## 문제

정수 배열 A와 정수 T가 주어집니다. 배열 A에서 합이 정확히 T가 되는 연속된 부분 배열(subarray)의 총 개수를 구하세요. 

연속 부분 배열은 시작점과 끝점을 가지며, 그 안의 모든 원소를 합한 값이 T가 되어야 합니다.

예를 들어, A = [1, 2, 3] 이고 T = 3인 경우, 합이 3인 부분 배열은 [1, 2]와 [3] 두 개입니다.

## 입력

첫 번째 줄에 정수 N이 주어지며, 이는 배열 A의 크기입니다.
두 번째 줄에는 공백으로 구분된 N개의 정수 A[0], A[1], ..., A[N-1]이 주어집니다.
세 번째 줄에 목표 합 T가 주어집니다.

## 출력

합이 T인 연속 부분 배열의 총 개수를 한 정수로 출력합니다.

## 제약 조건

1. 1 <= N <= 10^5
2. 1 <= A[i] <= 10^9
3. 0 <= T <= 10^14

(주의: T가 크기 때문에 누적 합(prefix sum)은 64비트 정수형을 사용해야 합니다.)

## 예제 1

**입력**
```
3
1 2 3
3
```

**출력**
```
2
```

*합이 3인 부분 배열은 [1, 2]와 [3]입니다.*

## 예제 2

**입력**
```
5
10 5 2 7 1
12
```

**출력**
```
2
```

*합이 12인 부분 배열은 [10, 2]와 [5, 7]입니다.*

## 예제 3

**입력**
```
4
1 1 1 1
2
```

**출력**
```
3
```

*합이 2인 부분 배열은 [1, 1] (인덱스 0, 1), [1, 1] (인덱스 1, 2), [1, 1] (인덱스 2, 3) 세 개입니다.*

## 힌트

- 누적 합(Prefix Sum) 개념을 사용해 보세요.
- 현재까지의 누적 합을 저장하고, 목표 합 T를 이용해 필요한 과거 합을 역산하는 방법을 고려해 보세요.


## 알고리즘 요약

누적 합(Prefix Sum)과 해시맵(Dictionary)을 이용한 방법입니다. 부분 배열 A[i...j]의 합은 누적 합 S[j] - S[i-1]과 같습니다. 우리가 원하는 것이 S[j] - S[i-1] = T 이므로, 필요한 과거 합 S[i-1] = S[j] - T가 됩니다. 따라서, 현재 누적 합 S[j]를 구하면서, S[j] - T 값을 해시맵에서 찾아 그 개수를 더해나가면 됩니다.

## 풀이 해설

💡 아이디어: 누적 합(Prefix Sum)을 이용합니다.
1. 누적 합 $P[i]$를 $A[0]$부터 $A[i]$까지의 합이라고 정의합니다. 즉, $P[i] = 	ext{A}[0] + 	ext{A}[1] + 	ext{A}[2] + 	ext{A}[3] + 	ext{A}[4]$.
2. 우리가 원하는 부분 배열 A[i...j]의 합은 $P[j] - P[i-1]$과 같습니다.
3. 이 합이 T가 되려면, $P[j] - P[i-1] = T$가 성립해야 합니다.
4. 따라서, $P[i-1] = P[j] - T$가 되어야 합니다.

단계:
1. `count`라는 변수에 최종 개수를 0으로 초기화합니다.
2. `prefix_sum_map`이라는 딕셔너리를 준비합니다. 이 딕셔너리는 `(누적 합 값: 해당 합이 나타난 횟수)`를 저장합니다. 초기 상태에서 합이 0인 경우는 항상 한 번 존재하므로, `prefix_sum_map[0] = 1`로 초기 설정합니다.
3. 현재 누적 합 `current_sum`을 0으로 초기화합니다.
4. 배열 A를 순회합니다 (인덱스 j).
5. 매 단계마다 `current_sum`에 A[j]를 더합니다.
6. 우리가 찾고자 하는 과거 합 `required_sum`은 `current_sum - T`입니다.
7. 만약 `required_sum`이 `prefix_sum_map`에 존재한다면, 그 값(횟수)만큼 `count`를 증가시킵니다. (이는 `required_sum`을 가졌던 시작점들이 T를 만드는 부분 배열의 개수임을 의미합니다).
8. 현재의 `current_sum`을 `prefix_sum_map`에 추가하거나, 이미 존재하면 횟수를 1 증가시킵니다.

시간 복잡도는 배열을 한 번만 순회하므로 $O(N)$입니다. 공간 복잡도는 최악의 경우 $O(N)$이 됩니다.

## 참고 코드 (python)

```python
import sys
from collections import defaultdict

def solve():
    # 입력 받기 (N, A, T 순서로 읽기 위해 세 줄을 처리)
    try:
        # 첫 줄: N (크기는 사용하지 않으므로 읽기만 함)
        n_line = sys.stdin.readline()
        if not n_line:
            return
        # 두 번째 줄: 배열 A
        a = list(map(int, sys.stdin.readline().split()))
        # 세 번째 줄: 목표 합 T
        t = int(sys.stdin.readline())
    except Exception:
        return

    # 딕셔너리 초기화: {누적 합: 횟수}
    # 합이 0인 경우는 부분 배열 시작 전 항상 1번 존재한다고 간주합니다.
    prefix_sum_map = defaultdict(int)
    prefix_sum_map[0] = 1
    
    current_sum = 0
    count = 0

    for num in a:
        # 1. 현재 누적 합 업데이트
        current_sum += num
        
        # 2. 찾고자 하는 과거 합 (required_sum = current_sum - T)
        required_sum = current_sum - t
        
        # 3. 맵에 required_sum이 존재한다면, 그 개수만큼 count 증가
        if required_sum in prefix_sum_map:
            count += prefix_sum_map[required_sum]
            
        # 4. 현재 누적 합을 맵에 기록 (혹은 횟수 증가)
        prefix_sum_map[current_sum] += 1

    print(count)

if __name__ == "__main__":
    solve()
```
