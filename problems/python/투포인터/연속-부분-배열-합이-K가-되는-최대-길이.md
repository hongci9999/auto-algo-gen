# 연속 부분 배열 합이 K가 되는 최대 길이
*python · 투포인터 · 보통 · 배열, 투포인터, 해시맵*

## 입출력 환경

입력은 sys.stdin.readline을 사용하여 처리합니다.

## 문제

정수 배열 `nums`와 목표 합 `K`가 주어집니다. 이 배열에서 합이 정확히 `K`가 되는 가장 긴 연속 부분 배열의 길이를 구하는 문제입니다.

배열의 모든 원소는 양의 정수입니다. 만약 합이 `K`가 되는 부분 배열이 존재하지 않는다면, 0을 출력해야 합니다.

## 입력

첫 번째 줄에 정수 N (배열의 길이)이 주어집니다.
두 번째 줄에 공백으로 구분된 N개의 정수 원소가 주어집니다.

## 출력

가장 긴 부분 배열의 길이(정수)를 출력합니다.

## 제약 조건

N: 1부터 100,000까지. 배열 원소: 1부터 100,000까지. 시간 복잡도는 O(N)을 목표로 합니다.

## 예제 1

**입력**
```
5
1 2 3 2 1
```

**출력**
```
3
```

*K=6 가정 시, [1, 2, 3] 부분 배열의 합이 6이고 길이는 3입니다.*

## 예제 2

**입력**
```
5
1 1 1 1 1
```

**출력**
```
2
```

*K=2 가정 시, [1, 1] 부분 배열의 합이 2이고 가장 긴 길이는 2입니다.*

## 힌트

- 이 문제는 누적 합(Prefix Sum)과 해시 맵(Dictionary)을 활용하는 것이 핵심입니다.
- 현재 위치까지의 누적 합 $S$와 목표 합 $K$를 이용하여, 이전에 어떤 누적 합이 존재했는지 역추적해야 합니다.


## 알고리즘 요약

누적 합(Prefix Sum)과 해시 맵(Hash Map)을 사용합니다. 현재 인덱스 $i$까지의 누적 합을 $S$라고 할 때, 만약 이 부분 배열의 합이 $K$가 되려면, $S - K$라는 합을 가진 지점이 존재해야 합니다. 해시 맵에 '누적 합 : 인덱스'를 저장하여, $S - K$의 가장 빠른 발생 지점을 찾아 거리를 계산합니다.

## 풀이 해설

아이디어:
이 문제는 '합이 K가 되는 가장 긴 연속 부분 배열'을 찾는 문제입니다. 시간 복잡도를 O(N)으로 만들기 위해, 누적 합(Prefix Sum)과 해시 맵을 사용합니다.

단계:
1. 변수 초기화: `max_length`를 0으로, `current_sum`을 0으로 초기화합니다.
2. 맵 초기화: 해시 맵 `prefix_sum_map`을 준비하고, 합 0이 인덱스 -1에서 발생했다는 정보를 미리 저장합니다. (이는 배열의 시작점부터 K가 되는 경우를 처리하기 위함입니다: `prefix_sum_map[0] = -1`).
3. 순회 및 계산: 배열 `nums`를 처음부터 끝까지 순회합니다 (인덱스 `i`).
    a. `current_sum`에 `nums[i]`를 더하여 업데이트합니다.
    b. 목표 합 $K$를 만들기 위해 필요한 이전 누적 합은 `target_sum = current_sum - K`입니다.
    c. 해시 맵에 `target_sum`이 존재하는지 확인합니다. 만약 존재한다면, 이는 합이 $K$가 되는 부분 배열이 존재함을 의미합니다. 이 부분 배열의 길이는 현재 인덱스 $i$에서 맵에 저장된 `target_sum`의 인덱스를 뺀 값입니다. `max_length = max(max_length, i - prefix_sum_map[target_sum])`으로 최대 길이를 갱신합니다.
    d. 맵 업데이트: 현재 누적 합 `current_sum`을 맵에 저장합니다. **주의:** 만약 `current_sum`이 이미 맵에 존재한다면, 덮어쓰지 않습니다. (가장 긴 길이를 구하려면, 같은 합이 발생했을 때 가장 초기에 발생한 인덱스를 유지해야 하기 때문입니다.)
4. 결과 반환: 순회가 끝난 후 `max_length`를 반환합니다.

시간 복잡도: 배열을 한 번만 순회하며, 맵의 삽입 및 조회는 평균 O(1) 시간이 걸리므로, 전체 시간 복잡도는 O(N)입니다.

## 참고 코드 (python)

```python
import sys
from collections import defaultdict

def solve():
    # sys.stdin.readline을 사용하여 입력을 받습니다.
    input = sys.stdin.read().split()
    if not input: return
    
    N = int(input[0])
    nums = [int(x) for x in input[1:]]
    
    # 문제의 목표 합 K를 가정합니다. (샘플에 K가 명시되지 않았으므로, 테스트를 위해 K=6을 사용합니다.)
    # 실제 코딩 테스트에서는 K가 별도로 주어집니다. 여기서는 샘플 1의 K=6을 사용합니다.
    K = 6 

    # prefix_sum_map: {누적 합: 가장 빠른 인덱스}
    # 합 0은 인덱스 -1에서 시작했다고 가정하여 초기화합니다.
    prefix_sum_map = {0: -1}
    current_sum = 0
    max_length = 0

    for i in range(N):
        num = nums[i]
        current_sum += num
        
        # 1. 목표 합을 만들기 위해 필요한 이전 누적 합을 계산
        target_sum = current_sum - K
        
        # 2. 맵에 target_sum이 존재하면, K를 만족하는 부분 배열을 찾음
        if target_sum in prefix_sum_map:
            start_index = prefix_sum_map[target_sum]
            length = i - start_index
            max_length = max(max_length, length)
            
        # 3. 현재 누적 합을 맵에 저장 (최초 발견 인덱스만 저장)
        if current_sum not in prefix_sum_map:
            prefix_sum_map[current_sum] = i
            
    print(max_length)

if __name__ == "__main__":
    solve()
```
