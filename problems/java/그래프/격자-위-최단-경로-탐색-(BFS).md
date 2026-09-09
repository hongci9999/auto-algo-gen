# 격자 위 최단 경로 탐색 (BFS)
*java · 그래프 · 보통 · BFS, 최단거리, 격자*

## 입출력 환경

Java 환경에서 BufferedReader와 StringTokenizer를 사용하여 입력을 처리하는 것이 효율적입니다.

## 문제

당신은 R행 C열 크기의 격자 위에서 움직이는 탐사 로봇을 제어합니다. 이 격자에는 장애물(1)과 이동 가능한 공간(0)이 섞여 있습니다.

로봇은 상하좌우 네 방향으로만 이동할 수 있으며, 장애물은 통과할 수 없습니다. 주어진 시작점 (start_r, start_c)에서 목표점 (end_r, end_c)까지 도달하는 최소 이동 횟수를 구하세요.

만약 목표점에 도달할 수 없다면 -1을 출력해야 합니다.

각 칸의 값은 다음과 같습니다:
- 0: 이동 가능한 공간
- 1: 장애물 (통과 불가)

## 입력

첫째 줄에 격자의 행의 개수 R과 열의 개수 C가 주어집니다. (1 ≤ R, C ≤ 100)
다음 R줄에 걸쳐 R행의 격자 값이 주어지며, 각 값은 0 또는 1입니다.
마지막 줄에는 시작점의 행과 열 (start_r, start_c)과 목표점의 행과 열 (end_r, end_c)이 순서대로 주어집니다. (0 ≤ start_r, start_c, end_r, end_c < R, C)

## 출력

최소 이동 횟수를 정수 형태로 출력합니다. 도달 불가능하면 -1을 출력합니다.

## 제약 조건

R, C <= 100. 시간 복잡도는 O(R * C) 이내여야 합니다.

## 예제 1

**입력**
```
3 3
0 0 0
0 1 0
0 0 0
0 2 2
```

**출력**
```
4
```

*직관적으로 최단 경로는 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2)를 거치며 4번의 이동이 필요합니다.*

## 예제 2

**입력**
```
3 3
0 1 0
1 1 1
0 1 0
0 0 2 0
```

**출력**
```
-1
```

*중앙에 장애물이 가로막고 있어 시작점과 목표점을 연결할 수 없습니다.*

## 힌트

- 최단 경로를 찾는 문제이며, 모든 간선의 가중치가 1인 그래프 탐색 문제입니다.
- 너비 우선 탐색(BFS)을 사용하여 시작점에서부터 거리를 층별로 퍼져나가며 탐색해야 합니다.


## 알고리즘 요약

BFS (Breadth-First Search). 시작점을 큐(Queue)에 넣고, 현재 위치에서 상하좌우 네 방향을 탐색합니다. 방문 기록(Visited 배열)을 사용하여 이미 방문한 곳이나 장애물은 건너뛰고, 도착 지점에 도달했을 때 큐에 저장된 거리를 반환합니다.

## 풀이 해설

풀이 아이디어는 너비 우선 탐색(BFS)을 이용하는 것입니다. BFS는 시작점에서부터 거리가 가까운 지점부터 순차적으로 탐색하기 때문에, 목표 지점에 도달했을 때의 거리가 곧 최단 거리가 됩니다.

단계별 풀이:
1. 초기화: 시작 위치를 큐에 넣고, 해당 위치의 거리를 0으로 설정하며, 방문 여부를 표시합니다. 또한, 시작점과 목표점의 좌표를 저장할 변수가 필요합니다.
2. 탐색 과정: 큐가 빌 때까지 반복합니다. 큐에서 현재 좌표(r, c)와 현재까지의 거리(dist)를 꺼냅니다.
3. 목표 확인: 만약 현재 좌표가 목표점과 같다면, 현재의 거리(dist)가 바로 최소 이동 횟수이므로 이를 반환하고 탐색을 종료합니다.
4. 다음 위치 탐색: 상하좌우 네 방향 (dr, dc)에 대해 다음 위치 (nr, nc)를 계산합니다.
5. 유효성 검사: 다음 위치 (nr, nc)가 다음 세 가지 조건을 모두 만족하는지 확인합니다:
    a) 격자 범위 내에 있는지 (0 ≤ nr < R, 0 ≤ nc < C).
    b) 장애물이 아닌지 (격자 값이 1이 아닌지).
    c) 아직 방문하지 않은 곳인지 (visited 배열 확인).
6. 큐에 추가 및 갱신: 위의 조건을 만족하면, 해당 위치를 방문 처리하고, 큐에 (nr, nc)와 (dist + 1)을 추가합니다.
7. 종료: 큐가 비게 될 때까지 목표에 도달하지 못했다면, 목표점에 도달할 수 없다는 의미이므로 -1을 반환합니다.

시간 복잡도는 BFS가 격자 전체를 한 번 탐색하므로, O(R * C)입니다. 공간 복잡도는 큐와 방문 배열 때문에 O(R * C)입니다.

## 참고 코드 (java)

```java
import java.util.*;
import java.io.*;

class Solution {
    // 4방향 이동: (상, 하, 좌, 우)
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        // 빠른 입출력을 위해 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        int[][] grid = new int[R][C];
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 시작점과 목표점 좌표 읽기
        st = new StringTokenizer(br.readLine());
        int startR = Integer.parseInt(st.nextToken());
        int startC = Integer.parseInt(st.nextToken());
        int endR = Integer.parseInt(st.nextToken());
        int endC = Integer.parseInt(st.nextToken());

        // BFS 실행
        int result = bfs(R, C, grid, startR, startC, endR, endC);
        System.out.println(result);
    }

    // BFS를 위한 좌표와 거리 정보를 담는 클래스
    static class State { 
        int r, c, dist; 
        State(int r, int c, int dist) { 
            this.r = r; 
            this.c = c; 
            this.dist = dist; 
        }
    }

    public static int bfs(int R, int C, int[][] grid, int startR, int startC, int endR, int endC) {
        // 방문 배열 초기화
        boolean[][] visited = new boolean[R][C];
        Queue<State> queue = new LinkedList<>();

        // 시작점 큐에 추가 및 방문 처리
        queue.offer(new State(startR, startC, 0));
        visited[startR][startC] = true;

        while (!queue.isEmpty()) {
            State current = queue.poll();
            int r = current.r;
            int c = current.c;
            int dist = current.dist;

            // 1. 목표 확인
            if (r == endR && c == endC) {
                return dist;
            }

            // 2. 상하좌우 네 방향 탐색
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                // 3. 유효성 검사
                // 3-1. 격자 경계 검사
                if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
                // 3-2. 장애물 검사 (1이면 통과 불가)
                if (grid[nr][nc] == 1) continue;
                // 3-3. 방문 여부 검사
                if (visited[nr][nc]) continue;

                // 유효하면 큐에 추가하고 방문 처리
                visited[nr][nc] = true;
                queue.offer(new State(nr, nc, dist + 1));
            }
        }

        // 큐가 비었으나 목표에 도달하지 못함
        return -1;
    }
```
