# 최대 겹치지 않는 $2 	imes 2$ 정사각형의 개수
*java · 시뮬레이션 · 보통 · 구현, 그리드*

## 입출력 환경

Java에서 빠른 입출력을 위해 BufferedReader와 StringTokenizer를 사용하는 것이 권장됩니다.

## 문제

N행 M열로 이루어진 2진수 그리드(0과 1로만 구성)가 주어집니다. 이 그리드 위에서 겹치지 않게 배치할 수 있는 크기 $2 	imes 2$ 정사각형 중, 모든 칸이 1로 채워진 정사각형의 최대 개수를 구하세요.

한 $2 	imes 2$ 정사각형을 배치하면 해당 칸은 더 이상 다른 정사각형의 일부가 될 수 없습니다. 따라서 한 번 사용된 칸은 재사용할 수 없습니다.

## 입력

첫 줄에 N과 M이 주어지고, 다음 N줄에 걸쳐 M개의 0 또는 1로 이루어진 문자열이 주어집니다.

## 출력

최대 개수를 담은 정수 하나를 출력합니다.

## 제약 조건

1 <= N, M <= 1000. 그리드 요소는 0 또는 1입니다.

## 예제 1

**입력**
```
3 3
110
110
000
```

**출력**
```
1
```

*좌상단 $(0, 0)$에서 시작하는 $2 	imes 2$ 정사각형 하나만 가능하며, 이 경우 최대 개수는 1입니다.*

## 예제 2

**입력**
```
4 4
1111
1111
1111
1111
```

**출력**
```
4
```

*그리드를 좌상단부터 순차적으로 스캔하면서 4개의 비겹치는 $2 	imes 2$ 정사각형을 배치할 수 있습니다.*

## 힌트

- 탐욕적인(Greedy) 방식으로 접근하는 것이 가장 효율적입니다.
- 한번 $2 	imes 2$ 정사각형을 배치한 칸은 즉시 사용 불가 상태로 변경해야 합니다.


## 알고리즘 요약

그리드를 순회하며 (i, j)를 $2 	imes 2$ 정사각형의 좌상단 꼭짓점으로 가정합니다. 만약 (i, j), (i+1, j), (i, j+1), (i+1, j+1) 네 칸 모두 1이라면, 하나의 타일을 배치하고 이 네 칸을 '사용됨'으로 표시합니다. 그리고 카운트를 증가시키며 그리드를 계속 탐색합니다.

## 풀이 해설

아이디어: 이 문제는 최대의 비겹치기 조건을 만족해야 하므로, 그리드를 순차적으로 스캔하며 타일을 배치하는 탐욕적(Greedy) 접근법을 사용합니다. 그리드를 좌상단부터 우하단으로 순회하면서, 현재 위치 $(i, j)$가 $2 	imes 2$ 정사각형의 좌상단이 될 수 있는지 확인합니다.

단계:
1. 크기 N행 M열의 그리드를 입력받고, 사용 여부를 표시하기 위해 복사본(또는 직접 수정 가능한 배열)을 준비합니다.
2. 카운트 변수를 0으로 초기화합니다.
3. i를 0부터 N-2까지, j를 0부터 M-2까지 반복하며 순회합니다. (좌상단 꼭짓점을 찾으므로 경계는 -2입니다.)
4. 현재 위치 $(i, j)$에서 시작하는 $2 	imes 2$ 정사각형의 네 칸 (즉, (i, j), (i+1, j), (i, j+1), (i+1, j+1))이 모두 '1' 상태인지 확인합니다. (여기서 '1'은 아직 사용되지 않은 원본 '1'을 의미합니다.)
5. 네 칸이 모두 '1'이라면:
    a. 카운트를 1 증가시킵니다.
    b. 해당 네 칸의 값을 모두 '0' (사용됨)으로 변경하여, 이후 스캔 과정에서 이 칸들이 다시 사용되지 않도록 표시합니다.
6. 모든 순회가 끝나면 최종 카운트 값을 반환합니다.

시간 복잡도: 그리드 전체를 $O(N 	imes M)$로 한 번만 순회하므로, 시간 복잡도는 $O(N 	imes M)$입니다.

## 참고 코드 (java)

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 그리드 값을 저장할 2차원 배열 (문자열을 받아 정수형으로 변환)
        int[][] grid = new int[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                grid[i][j] = line.charAt(j) - '0';
            }
        }

        System.out.println(solve(N, M, grid));
    }

    private static int solve(int N, int M, int[][] grid) {
        int count = 0;

        // 좌상단 꼭짓점을 기준으로 순회합니다. (N-2, M-2까지만 체크해야 2x2가 가능)
        for (int i = 0; i <= N - 2; i++) {
            for (int j = 0; j <= M - 2; j++) {
                
                // 2x2 정사각형의 네 칸을 체크
                if (grid[i][j] == 1 &&
                    grid[i+1][j] == 1 &&
                    grid[i][j+1] == 1 &&
                    grid[i+1][j+1] == 1) {
                    
                    // 유효한 2x2 정사각형 발견
                    count++;
                    
                    // 해당 칸들은 사용되었으므로 0으로 변경 (Marking)
                    grid[i][j] = 0;
                    grid[i+1][j] = 0;
                    grid[i][j+1] = 0;
                    grid[i+1][j+1] = 0;
                }
            }
        }
        return count;
    }
}
```
