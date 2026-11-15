# 최대 합이 K의 배수인 부분 배열 길이
*python · 자료구조 · 보통 · 누적합, 딕셔너리, 부분 배열, 모듈러 연산*

## 입출력 환경

입력은 sys.stdin.readline을 사용하며, 첫 줄에 N과 K가, 다음 줄에 배열 A가 주어집니다.

## 문제

정수 배열 A와 양의 정수 K가 주어집니다. 배열 A에서 합이 K의 배수가 되는 부분 배열을 찾고, 그중 가장 긴 부분 배열의 길이를 구하는 문제입니다.

부분 배열은 A[i]부터 A[j]까지의 원소들로 구성됩니다. 즉, A[i] + A[i+1] + ... + A[j]의 합이 K로 나누어 떨어져야 합니다.

## 입력

첫째 줄에 정수 N과 정수 K가 공백으로 구분되어 주어집니다. 둘째 줄에는 N개의 정수 A[0], A[1], ..., A[N-1]가 공백으로 구분되어 주어집니다.

## 출력

가장 긴 부분 배열의 길이(정수)를 한 줄로 출력합니다.

## 제약 조건

1. 1 ≤ N ≤ 10^5
2. 1 ≤ K ≤ 10^5
3. -10^9 ≤ A[i] ≤ 10^9
4. 시간 복잡도는 O(N) 또는 O(N log N) 이하여야 합니다.

## 예제 1

**입력**
```
4 3
4 5 1 2
```

**출력**
```
4
```

*배열 전체 합 12는 3의 배수이므로, 최대 길이는 4입니다.*

## 예제 2

**입력**
```
5 6
1 2 3 4 5
```

**출력**
```
3
```

*합이 6의 배수인 가장 긴 부분 배열은 [1, 2, 3] (합 6) 또는 [2, 3, 4, 5] (합 14, X) 등이며, 최대 길이는 3입니다.*

## 예제 3

**입력**
```
3 2
1 1 1
```

**출력**
```
2
```

*합이 2의 배수인 가장 긴 부분 배열은 [1, 1] (합 2)입니다. 최대 길이는 2입니다.*

## 힌트

- 부분 배열의 합은 누적 합(Prefix Sum)의 차이로 표현할 수 있습니다.
- 합이 K의 배수라는 조건은 모듈러 연산(Modulo)을 이용하여 변환할 수 있습니다.


## 알고리즘 요약

누적 합과 딕셔너리(Hash Map)를 이용한 접근법입니다. 부분 배열의 합이 K의 배수라는 조건을 모듈러 연산과 결합하여, 특정 나머지 값이 처음 등장한 지점의 인덱스를 저장하고, 현재 인덱스와 비교하여 최대 거리를 계산합니다.

## 풀이 해설

## 💡 아이디어: 누적 합과 모듈러 연산

부분 배열 A[i]부터 A[j]까지의 합을 $S_{i,j}$라고 할 때, $S_{i,j} = 	ext{PrefixSum}[j] - 	ext{PrefixSum}[i-1]$ 입니다.

우리가 원하는 조건은 $S_{i,j} mod K = 0$ 입니다.
이것을 모듈러 연산으로 변환하면:
$(	ext{PrefixSum}[j] - 	ext{PrefixSum}[i-1]) mod K = 0$
$	ext{PrefixSum}[j] mod K = 	ext{PrefixSum}[i-1] mod K$

즉, 어떤 지점 $j$까지의 누적 합의 나머지가, 이전에 어떤 지점 $i-1$까지의 누적 합의 나머지 값과 같으면, 그 사이의 부분 배열 합은 K의 배수가 됩니다.

## 🛠 단계별 풀이

1. **초기화:** 최대 길이를 0으로 설정하고, 누적 합(current_sum)을 0으로 시작합니다. 또한, 나머지 값(remainder)을 저장할 딕셔너리 `remainder_map`을 준비합니다.
2. **기준점 설정:** 누적 합을 시작하기 전(즉, 인덱스 -1 시점)의 나머지는 0입니다. 따라서 `remainder_map[0] = -1` 로 설정하여, 나머지 0이 발견될 경우 배열의 시작부터의 길이를 계산할 수 있도록 합니다.
3. **순회 및 계산:** 배열 A를 처음부터 끝까지 순회합니다 (인덱스 $i$).
    a. `current_sum`에 $A[i]$를 더합니다.
    b. 현재 나머지를 계산합니다: `remainder = current_sum % K`. (Python에서는 음수 처리 시 주의해야 하므로, `(current_sum % K + K) % K` 공식을 사용합니다.)
    c. **검색:** 만약 `remainder`가 이미 `remainder_map`에 존재한다면, 이는 이전에 동일한 나머지를 가졌던 지점($i_{prev} = 	ext{remainder_map}[	ext{remainder}]$)이 있다는 의미입니다. 따라서 $i_{prev}$와 현재 인덱스 $i$ 사이의 부분 배열은 합이 K의 배수입니다. 이때의 길이는 $i - i_{prev}$이며, 최대 길이를 갱신합니다.
    d. **저장:** 만약 `remainder`가 `remainder_map`에 존재하지 않는다면, 이 나머지를 처음 발견한 지점인 현재 인덱스 $i$를 저장합니다: `remainder_map[remainder] = i`.
4. **결과 반환:** 순회가 끝난 후, 저장된 최대 길이 값을 반환합니다.

## ⏱ 시간 복잡도

*   시간 복잡도: $O(N)$ (배열을 한 번만 순회하며, 딕셔너리 접근 및 삽입은 평균 $O(1)$ 시간 복잡도를 가집니다.)
*   공간 복잡도: $O(K)$ (최악의 경우 모든 나머지 값 $0$부터 $K-1$까지 딕셔너리에 저장될 수 있습니다.)

## 참고 코드 (python)

```python
import sys

def solve():
    # sys.stdin.readline을 사용하여 입력을 받습니다.
    try:
        # 첫 줄: N과 K
        line1 = sys.stdin.readline().split()
        if not line1: return
        N = int(line1[0])
        K = int(line1[1])
        
        # 두 번째 줄: 배열 A
        A = list(map(int, sys.stdin.readline().split()))
    except EOFError:
        return
    except Exception:
        # 입력 형식이 잘못되었을 경우 처리
        return
    
    # remainder_map: {나머지 값: 해당 나머지가 처음 발견된 인덱스}
    # 초기 상태: 누적 합 0 (나머지 0)은 가상의 인덱스 -1에서 발견됨.
    remainder_map = {0: -1}
    
    current_sum = 0
    max_length = 0
    
    for i in range(N):
        current_sum += A[i]
        
        # 모듈러 연산 처리: 파이썬의 % 연산자는 음수에 대해 다르게 동작할 수 있으므로,
        # 항상 (X % K + K) % K 공식을 사용하여 0부터 K-1 사이의 양의 나머지를 보장합니다.
        remainder = current_sum % K
        if remainder < 0: # A[i]가 음수일 때 발생 가능
             remainder = (remainder + K) % K
        
        # 1. 나머지가 이미 맵에 존재하는가? (즉, 이전에 같은 합의 나머지를 가졌는가?)
        if remainder in remainder_map:
            # 이전에 발견된 인덱스: remainder_map[remainder]
            # 현재 인덱스: i
            # 길이 = 현재 인덱스 - 이전 인덱스
            length = i - remainder_map[remainder]
            max_length = max(max_length, length)
        else:
            # 2. 이 나머지를 처음 발견했다면, 인덱스를 맵에 저장한다.
            remainder_map[remainder] = i
            
    print(max_length)

solve()
```
