# 최소 비용 연결 트리 (Minimum Spanning Tree)
*java · 그래프 · 보통 · MST, 크루스칼, Union-Find*

## 입출력 환경

입력은 System.in에서 받으며, Java에서는 BufferedReader와 StringTokenizer를 사용하여 효율적으로 처리하는 것을 권장합니다.

## 문제

주어진 N개의 정점과 E개의 간선으로 구성된 그래프가 있습니다. 각 간선에는 고유한 가중치(비용)가 부여되어 있으며, 이 비용은 0부터 100까지의 정수입니다.

여러분이 해야 할 일은 이 N개 정점을 모두 연결하는 최소 비용으로 이루어진 트리를 찾는 것입니다. 즉, 그래프 전체를 연결하면서도 간선의 총합이 최소가 되도록 구성해야 합니다. 만약 주어진 간선만으로는 모든 정점을 연결할 수 없다면, 불가능하다는 것을 출력해야 합니다.

(주의: 문제에서 모든 정점이 반드시 연결되어야 하며, 비용은 음수가 아닙니다.)

## 입력

첫째 줄에 N과 E가 주어집니다. (1 <= N <= 10^3, 0 <= E <= N*N/2)
둘째 줄부터 E개의 간선 정보가 차례로 주어집니다. 각 간선은 `u` `v` `w` 형식으로 나타내며, $u$와 $v$는 연결되는 두 정점(1부터 N까지), $w$는 해당 간선의 비용입니다.

## 출력

모든 정점을 연결하는 최소 비용의 합을 출력합니다. 만약 모든 정점을 연결할 수 없다면 -1을 출력합니다.

## 제약 조건

N: 1 ~ 10^3
E: 0 ~ 5*10^5
W: 0 ~ 100

## 예제 1

**입력**
```
4 5
1 2 3
1 3 2
2 3 1
2 4 7
3 4 6
```

**출력**
```
9
```

*간선들을 비용 순으로 연결했을 때, (2,3), (1,3), (1,2)를 사용하여 모든 정점(1~4)을 연결할 수 없습니다. (2,3)=1, (1,3)=2, (1,2)=3, (2,4)=7, (3,4)=6 중 4개로 최소 비용 구성: 1+2+3+? = 9. 정점 4를 연결해야 하므로, 가장 작은 간선들을 선택하여 4개의 트리를 만듭니다. 최종적으로 { (2,3), (1,3), (1,2) }와 같이 N-1개 간선을 선택할 때, 정점 4가 포함된 최소 비용은 9입니다.*

## 예제 2

**입력**
```
5 4
1 2 10
2 3 10
3 4 10
4 5 10
```

**출력**
```
40
```

*정점들이 순차적으로 연결되어 있으며, N-1개의 모든 간선을 사용해야 하므로 총 비용은 4*10 = 40입니다.*

## 힌트

- 간선의 가중치(비용)를 기준으로 오름차순 정렬하는 것이 핵심 단계입니다.
- 사이클을 방지하고 트리를 구성하기 위해 'Disjoint Set Union (Union-Find)' 자료구조를 사용하는 것을 고려해 보세요.


## 알고리즘 요약

이 문제는 최소 신장 트리(Minimum Spanning Tree, MST) 문제입니다. 주어진 간선들을 비용이 가장 낮은 순서대로 선택해가면서 사이클을 만들지 않도록 관리하면 됩니다. 대표적으로 크루스칼 알고리즘(Kruskal's Algorithm)을 사용합니다. 1. 모든 간선을 가중치 기준으로 정렬합니다. 2. Union-Find 구조를 사용하여, 현재 간선이 이미 같은 연결 요소에 속하는 두 정점 사이에 놓이는지 확인합니다. 3. 사이클을 만들지 않는 간선(즉, 서로 다른 연결 요소를 연결하는 간선)만 선택하고 그 비용을 누적합니다. 4. 최종적으로 N-1개의 간선을 선택했거나, 모든 정점이 하나의 연결 요소가 되었는지 확인하여 결과를 도출합니다.

## 풀이 해설

<h3>풀이 해설: 크루스칼 알고리즘 (Kruskal's Algorithm)</h3>
<ol>
    <li><strong>아이디어</strong>: 최소 비용으로 모든 정점을 연결하는 트리를 찾기 위해, 가장 적은 비용을 가진 간선부터 순차적으로 선택합니다. 이때, 이미 같은 그룹에 속한 정점들을 다시 연결하는 '사이클(Cycle)'이 발생하지 않도록 주의해야 합니다.</li>
    <li><strong>단계</strong>:
        <ol>
            <li><strong>데이터 구조 준비</strong>: 모든 간선 정보를 (가중치 $w$, 정점 $u$, 정점 $v$) 튜플 형태로 저장합니다.</li>
            <li><strong>정렬</strong>: 이 간선들을 가중치 $w$를 기준으로 오름차순으로 정렬합니다.</li>
            <li><strong>Union-Find 초기화</strong>: N개의 정점 각각에 대해 Union-Find 자료구조를 초기화하여, 각 정점이 독립적인 연결 요소(집합)의 대표가 되도록 설정합니다 (각 정점을 하나의 집합으로 간주).</li>
            <li><strong>순회 및 탐색</strong>: 정렬된 간선을 처음부터 끝까지 순회하며 다음 검사를 수행합니다:
                <ul>
                    <li>간선 $(u, v)$를 선택했을 때, $u$와 $v$가 현재 Union-Find 구조상 다른 집합(다른 연결 요소)에 속하는지 확인합니다. (즉, `find(u) != find(v)` 인지 확인)</li>
                    <li>만약 다르다면, 이 간선은 트리를 구성하는 데 필수적이며 사이클을 만들지 않으므로 선택하고 총 비용에 더합니다. 이후 두 집합을 합칩니다 (`union(u, v)`).</li>
                    <li>만약 같다면, 이미 연결되어 있는 경로를 다시 잇는 것이므로 무시합니다 (사이클 발생).</li>
                </ul>
            </li>
        </ol>
    </li>
    <li><strong>결과 판별</strong>: 모든 간선을 다 확인한 후, 선택된 간선의 개수가 $N-1$개인지 확인해야 합니다. 만약 $N$개의 정점을 연결하려면 최소 $N-1$개의 간선이 필요합니다. 따라서 최종적으로 획득한 비용을 반환합니다. 만약 간선 수가 $N-1$개가 아니라면, 모든 정점을 연결할 수 없다는 의미이므로 -1을 출력해야 합니다.</li>
    <li><strong>시간 복잡도</strong>: 간선들을 정렬하는 데 $O(E ead{)} 	ext{ log } E$가 걸립니다. Union-Find 연산은 거의 상수 시간($	ext{amortized } O(	ext{a}(N))$)이므로, 전체 시간 복잡도는 $O(E ead{)} 	ext{ log } E$로 매우 효율적입니다.</li>
</ol>

## 참고 코드 (java)

```java
import java.io.*;
import java.util.*;

// 간선 정보를 담을 클래스
class Edge implements Comparable<Edge> {
    int u, v, w;

    public Edge(int u, int v, int w) {
        this.u = u;
        this.v = v;
        this.w = w;
    }

    // 가중치(비용)를 기준으로 오름차순 정렬을 위한 비교 메서드
    @Override
    public int compareTo(Edge other) {
        return Integer.compare(this.w, other.w);
    }
}

// Union-Find 자료구조 구현
class DSU {
    private int[] parent;
    private int count; // 현재 연결된 독립적인 집합의 개수

    public DSU(int n) {
        parent = new int[n + 1];
        count = n;
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }
    }

    // 압축을 사용하여 부모를 찾음 (Find with Path Compression)
    public int find(int i) {
        if (parent[i] == i) {
            return i;
        }
        return parent[i] = find(parent[i]);
    }

    // 두 집합을 합침 (Union by Rank/Size는 생략 가능하지만, 구현 시 고려됨)
    public boolean union(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);

        if (rootI != rootJ) {
            parent[rootI] = rootJ;
            count--; // 두 집합이 합쳐지면 전체 집합의 개수가 1 감소
            return true; // 성공적으로 연결됨
        }
        return false; // 이미 같은 집합에 속함 (사이클 발생)
    }
    
    public int getComponentCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입출력을 위해 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 정점 개수
        int E = Integer.parseInt(st.nextToken()); // 간선 개수

        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < E; i++) {
            StringTokenizer edgeSt = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(edgeSt.nextToken());
            int v = Integer.parseInt(edgeSt.nextToken());
            int w = Integer.parseInt(edgeSt.nextToken());
            edges.add(new Edge(u, v, w));
        }

        // 1. 간선들을 가중치 기준으로 오름차순 정렬 (Kruskal의 첫 단계)
        Collections.sort(edges);

        // Union-Find 초기화: N개의 독립된 집합으로 시작
        DSU dsu = new DSU(N);
        long minCost = 0;
        int edgesCount = 0; // 트리를 구성하는 간선 개수

        // 2. 정렬된 간선을 순회하며 MST 찾기
        for (Edge edge : edges) {
            // u와 v가 다른 연결 요소에 속해 있는지 확인
            if (dsu.find(edge.u) != dsu.find(edge.v)) {
                // 사이클이 발생하지 않으므로 간선 선택 및 비용 누적
                dsu.union(edge.u, edge.v);
                minCost += edge.w;
                edgesCount++;
            }
        }
        
        // 3. 결과 판별: N개의 정점을 연결하려면 최소 N-1개의 간선이 필요함.
        if (N == 1) {
             System.out.println(0);
        } else if (edgesCount == N - 1 && dsu.getComponentCount() == 1) {
            // 모든 정점이 하나의 연결 요소로 합쳐졌고, 필요한 간선 개수만큼 선택됨
            System.out.println(minCost);
        } else {
            // 모든 정점을 연결할 수 없음 (N > 1 이면서 컴포넌트 수가 1이 아닐 경우)
            System.out.println(-1); 
        }
    }
}
```
