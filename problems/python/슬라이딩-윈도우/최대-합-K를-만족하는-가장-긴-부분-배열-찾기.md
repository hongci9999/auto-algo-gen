# 최대 합 K를 만족하는 가장 긴 부분 배열 찾기
*python · 슬라이딩 윈도우 · 보통 · 배열, 슬라이딩 윈도우, 투포인터*

## 입출력 환경

입력은 전체를 문자열로 읽어 처리하거나, sys.stdin.readline을 사용하여 효율적으로 읽는 것이 좋습니다.

## 문제

정수 $A$로 이루어진 배열이 주어지고, 양의 정수 $K$가 주어집니다. 
이 배열에서 합이 $K$ 이하인 가장 긴 연속 부분 배열의 길이를 구하는 문제입니다.

주의: 배열 $A$의 원소들은 모두 양수입니다.

## 입력

첫 번째 줄에 배열의 길이 $N$과 최대 합 $K$가 공백으로 구분되어 주어집니다. 
두 번째 줄에는 배열 $A$의 $N$개 원소가 공백으로 구분되어 주어집니다.

## 출력

한 줄에 가장 긴 부분 배열의 길이(정수)를 출력합니다.

## 제약 조건

1. $1 	ext{ } 	ext{.} 	ext{ } N 	ext{ } 	ext{.} 	ext{ } 1 	ext{ } 	ext{.} 	ext{ } 10^5$ 
2. $1 	ext{ } 	ext{.} 	ext{ } K 	ext{ } 	ext{.} 	ext{ } 10^9$ 
3. $1 	ext{ } 	ext{.} 	ext{ } A[i] 	ext{ } 	ext{.} 	ext{ } 10^9$ 

(시간 복잡도는 $O(N)$을 목표로 합니다.)

## 예제 1

**입력**
```
3 4
1 2 3
```

**출력**
```
2
```

*부분 배열 [1, 2]의 합이 3으로 K=4 이하이며, 길이가 가장 길다.*

## 예제 2

**입력**
```
4 3
1 1 1 1
```

**출력**
```
3
```

*부분 배열 [1, 1, 1]의 합이 3으로 K=3 이하이며, 가장 길다.*

## 예제 3

**입력**
```
5 10
5 1 2 3 1
```

**출력**
```
4
```

*부분 배열 [1, 2, 3, 1]의 합이 7로 K=10 이하이며, 가장 길다.*

## 힌트

- 부분 배열의 합을 효율적으로 계산하고, 합이 K를 초과할 때 윈도우를 어떻게 조정할지 고민해 보세요.
- 슬라이딩 윈도우(Sliding Window) 기법을 사용하면 포인터를 한 번만 움직여 O(N) 시간에 문제를 해결할 수 있습니다.


## 알고리즘 요약

슬라이딩 윈도우 (Sliding Window) 기법을 사용합니다. 두 개의 포인터(left, right)를 사용하여 현재 부분 배열 [left, right]를 유지합니다. 'right' 포인터를 오른쪽으로 이동시키면서 현재 합(current_sum)을 갱신합니다. 만약 current_sum이 $K$를 초과하게 되면, 합을 줄여나가면서 'left' 포인터를 오른쪽으로 이동시켜 합이 다시 $K$ 이하가 될 때까지 윈도우를 축소합니다. 매 순간 조건을 만족하는 윈도우의 길이를 기록하면서 최대값을 갱신합니다.

## 풀이 해설

💡 아이디어: 이 문제는 '합이 K 이하인 가장 긴 연속 부분 배열'을 찾는 문제입니다. 원소들이 모두 양수이므로, 합이 증가하는 것은 항상 한쪽 끝에서 원소를 추가할 때만 가능합니다. 따라서 슬라이딩 윈도우 기법을 적용하는 것이 가장 효율적입니다.

단계:
1. 초기 설정: `left` 포인터(시작점)를 0으로, `current_sum`을 0으로, `max_length`를 0으로 설정합니다.
2. 윈도우 확장 (Right Pointer 이동): `right` 포인터를 배열의 끝까지 1씩 증가시키며 윈도우를 확장합니다. 이때, $A[right]$ 값을 `current_sum`에 더합니다.
3. 윈도우 축소 (Left Pointer 이동): 만약 `current_sum`이 $K$를 초과하게 되면, 윈도우는 유효하지 않은 상태입니다. 이때는 `current_sum`에서 $A[left]$ 값을 빼주고, `left` 포인터를 1 증가시킵니다. 이 과정을 `current_sum`이 다시 $K$ 이하가 될 때까지 반복합니다.
4. 길이 갱신: 윈도우의 합이 $K$ 이하가 된 상태라면, 현재 윈도우의 길이 (`right - left + 1`)를 계산하여 `max_length`와 비교하고 최댓값으로 갱신합니다.
5. 반복: 2~4단계를 배열의 끝까지 반복한 후, `max_length`를 반환합니다.

⏱ 시간 복잡도: `left`와 `right` 포인터가 각각 배열의 원소를 최대 한 번씩만 순회하므로, 전체 시간 복잡도는 $O(N)$입니다. 이는 배열 크기 $N$에 비례하여 매우 효율적입니다.

## 참고 코드 (python)

```python
import sys

def solve():
    # sys.stdin.readline을 사용하여 N, K를 읽습니다.
    try:
        input_nk = sys.stdin.readline().split()
        if not input_nk: return
        N = int(input_nk[0])
        K = int(input_nk[1])
    except EOFError:
        return
    except IndexError:
        # N과 K가 한 줄에 안 들어오는 경우 대비
        return

    # 배열 A를 읽습니다.
    try:
        A = list(map(int, sys.stdin.readline().split()))
    except EOFError:
        A = []
    
    # -------------------------------------------------
    # 슬라이딩 윈도우 구현
    
    left = 0           # 윈도우 시작 포인터
    current_sum = 0    # 현재 윈도우의 합
    max_length = 0     # 최대 길이

    for right in range(N):
        # 1. 윈도우 확장: right 포인터를 움직이며 합을 증가시킵니다.
        current_sum += A[right]

        # 2. 윈도우 축소: 합이 K를 초과하면 left 포인터를 움직여 크기를 줄입니다.
        while current_sum > K:
            current_sum -= A[left]
            left += 1
        
        # 3. 길이 갱신: 현재 윈도우 [left, right]는 합이 K 이하입니다.
        # 현재 길이는 (right - left + 1) 입니다.
        current_length = right - left + 1
        max_length = max(max_length, current_length)

    print(max_length)

if __name__ == "__main__":
    solve()
```
