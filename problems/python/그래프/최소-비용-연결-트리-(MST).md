# 최소 비용 연결 트리 (MST)
*python · 그래프 · 보통 · MST, 크루스칼 알고리즘, Union-Find*

## 입출력 환경

입력은 표준 입력(stdin)으로 받으며, 파이썬의 sys.stdin.readline 등을 사용하여 효율적으로 처리하는 것이 좋습니다.

## 문제

주어진 N개의 도시와 그 사이를 연결하는 여러 개의 도로(간선)들이 있습니다. 각 도로는 고유한 비용을 가지고 있으며, 이 도로는 양방향으로 사용 가능합니다.

우리는 모든 도시가 최소의 총 비용으로 서로 연결되도록 하는 가장 저렴한 네트워크(트리 구조)를 구축하려고 합니다. 즉, 간선들을 선택하여 모든 도시가 연결되지만, 사이클이 발생하지 않도록 하면서 전체 비용 합이 최소가 되게 해야 합니다.

최소 신장 트리(Minimum Spanning Tree, MST)의 총 비용을 구하는 것이 목표입니다.

## 입력

첫째 줄에 도시의 개수 N과 도로의 개수 M이 주어집니다. (N: 1 <= N <= 10^3, M: 0 <= M <= 5*10^4)
다음 M개의 줄에는 각 도로의 정보를 담고 있습니다. i번째 줄은 '비용 시작도시 끝도시' 형식으로 주어지며, 비용(w), 시작도시(u), 끝도시(v) 순서로 되어 있습니다.
(도시는 1부터 N까지 번호가 매겨집니다.)

## 출력

모든 도시를 연결하는 최소 비용의 총합을 하나의 정수로 출력합니다.

## 제약 조건

N: 1 <= N <= 10^3
M: 0 <= M <= 5*10^4
비용(w): 1 <= w <= 10^9

## 예제 1

**입력**
```
4 5
1 1 2
3 1 3
2 2 3
4 1 4
5 2 4
```

**출력**
```
6
```

*간선들 중 (비용, u, v) 순서로 정렬한 후 크루스칼 알고리즘을 적용합니다. 선택되는 간선은 (1, 2), (2, 3), (4, 1)입니다.*

## 예제 2

**입력**
```
3 3
10 1 2
5 2 3
1 1 3
```

**출력**
```
6
```

*가장 저렴한 간선부터 선택하며, 사이클을 만들지 않도록 합니다. (1, 3) -> (2, 3) -> (1, 2)를 선택합니다.*

## 힌트

- 사이클이 발생하는 것을 방지하는 자료구조가 필요합니다.
- 모든 간선을 비용을 기준으로 오름차순 정렬한 후 순회하는 것이 효율적입니다.


## 알고리즘 요약

크루스칼 알고리즘(Kruskal's Algorithm) 또는 프림 알고리즘(Prim's Algorithm) 사용. 크루스칼이 간선 목록을 기준으로 처리하기에 적합하며, Union-Find 자료구조를 사용하여 사이클 발생 여부를 판별합니다.

## 풀이 해설

풀이 아이디어는 최소 신장 트리(MST)를 찾는 것입니다. 우리는 모든 도시가 연결되도록 하는 가장 저렴한 간선들의 집합을 찾아야 합니다.

1. **정렬**: 주어진 M개의 도로(간선) 정보를 비용 순으로 오름차순 정렬합니다. 비용이 낮은 간선부터 선택하는 것이 최소 비용을 보장하기 때문입니다.
2. **Union-Find (Disjoint Set Union, DSU)**: 사이클 발생 여부를 효율적으로 체크하기 위해 Union-Find 자료구조를 사용합니다. 초기에는 N개의 도시가 모두 독립된 집합(세트)으로 존재한다고 가정합니다.
3. **순회 및 연결**: 정렬된 간선을 하나씩 순회하며, 현재 간선 (u, v)의 양 끝점 u와 v가 이미 같은 집합에 속해 있는지 확인합니다 (Find 연산). 
    - 만약 `Find(u) != Find(v)`라면, 이 간선을 선택해도 사이클이 발생하지 않습니다. 따라서 이 간선의 비용을 총 비용에 더하고 두 도시를 하나의 집합으로 합칩니다 (Union 연산).
    - 만약 `Find(u) == Find(v)`라면, 이미 같은 집합에 속해 있다는 의미이므로, 이 간선을 선택하면 사이클이 발생합니다. 따라서 이 간선은 무시합니다.
4. **종료**: 모든 간선을 확인하거나 (또는 N-1개의 간선을 선택하여) 총 비용을 반환합니다. 크루스칼 알고리즘의 시간 복잡도는 정렬 시간과 Union-Find 연산 시간을 합한 $\mathcal{O}(M \log M + M \alpha(N))$ 입니다. $M$은 간선의 수, $N$은 도시의 수이며, $\alpha(N)$은 아커만 함수의 역함수로 매우 느리게 증가하여 거의 상수 시간으로 간주됩니다.

## 참고 코드 (python)

```python
import sys
# 재귀 깊이 제한 늘리기 (큰 그래프 처리를 위해)
sys.setrecursionlimit(2000)

def solve():
    # 입력을 빠르게 받기 위한 설정
    input = sys.stdin.read().split()
    if not input: # 입력이 비어있을 경우 처리
        return 0
    
    N = int(input[0])  # 도시 개수
    M = int(input[1])  # 도로 개수
    
    edges = []
    idx = 2 # 실제 간선 데이터 시작 인덱스
    for _ in range(M):
        w = int(input[idx])   # 비용
        u = int(input[idx+1]) # 시작 도시
        v = int(input[idx+2]) # 끝 도시
        edges.append((w, u, v))
        idx += 3
    
    # 크루스칼 알고리즘 준비
    # 간선을 비용 기준으로 오름차순 정렬
    edges.sort()
    
    # Union-Find 자료구조 구현
    parent = list(range(N + 1)) # 1부터 N까지 사용하므로 크기 N+1
    rank = [0] * (N + 1)

def find_set(i):
    if parent[i] == i:
        return i
    # 경로 압축
    parent[i] = find_set(parent[i])
    return parent[i]

def union_sets(i, j):
    root_i = find_set(i)
    root_j = find_set(j)
    
    if root_i != root_j:
        # 랭크를 이용한 합치기 (Union by Rank)
        if rank[root_i] < rank[root_j]:
            parent[root_i] = root_j
        elif rank[root_i] > rank[root_j]:
            parent[root_j] = root_i
        else:
            parent[root_j] = root_i # 어느 쪽으로 붙여도 상관없음
            rank[root_i] += 1
            
        return True # 합병 성공
    return False # 이미 같은 집합에 속함

    # MST 계산 과정
    min_cost = 0
    edges_count = 0
    
    for w, u, v in edges:
        if union_sets(u, v):
            min_cost += w
            edges_count += 1
            # N-1개의 간선이 선택되면 MST가 완성되므로 종료할 수 있음
            if edges_count == N - 1:
                break
    
    return min_cost

print(solve())
```
