# 최대 사각형 넓이 (Maximum Rectangle Area)
*java · 자료구조 · 보통 · 이진탐색, 스택, 누적합*

## 입출력 환경

Java 환경에서 표준 입력을 사용하며, 성능을 위해 `BufferedReader`와 `StringTokenizer`를 활용하는 것이 권장됩니다.

## 문제

주어진 $N 	imes M$ 크기의 이진 지도(Binary Map)가 있습니다. 각 칸은 0 또는 1로 채워져 있으며, 1은 장애물, 0은 빈 공간을 나타냅니다. 여러분은 이 지도의 빈 공간(0)으로만 이루어진 직사각형 영역 중 최대 넓이를 가지는 직사각형을 찾아야 합니다.

단, 직사각형의 경계는 반드시 주어진 지도의 경계와 일치해야 합니다.

이 문제를 해결하기 위해, '높이'를 기준으로 사각형 넓이를 계산하는 방식을 사용합니다. 즉, 직사각형의 바닥 행(Bottom Row)을 고정하고, 그 행을 포함하는 최대 높이를 찾습니다.

## 입력

첫 번째 줄에 $N$과 $M$이 주어집니다. ($N$: 행의 개수, $M$: 열의 개수)
다음 $N$ 줄에 걸쳐 $M$개의 0 또는 1로 이루어진 문자열이 주어집니다. (문자열 '0' 또는 '1'로 구성)

## 출력

최대 넓이를 가지는 직사각형의 넓이(정수)를 출력합니다.

## 제약 조건

1 ≤ N, M ≤ 100. 각 칸은 '0' 또는 '1'로만 구성됩니다. 시간 복잡도는 $O(N 	imes M)$ 또는 $O(N 	imes M 	imes 	ext{log}(N))$ 이하가 요구됩니다.

## 예제 1

**입력**
```
3 4
0010
0000
0100
```

**출력**
```
8
```

*세 번째 행(0100)을 바닥으로 가정할 때, 가장 넓은 직사각형은 (0, 0)부터 (2, 3)까지의 영역을 포함하는 0으로만 이루어진 사각형입니다. (0, 0)부터 (2, 1)까지의 0으로만 이루어진 직사각형의 높이는 3, 너비는 2이므로 넓이는 6입니다. 하지만 (1, 1)부터 (2, 3)까지는 0으로만 이루어진 직사각형이 존재하며, 이 경우 최대 넓이는 8입니다. (예: 0,0부터 2,3까지의 0으로만 이루어진 영역)*

## 예제 2

**입력**
```
4 4
0000
0100
0000
0000
```

**출력**
```
12
```

*가장 넓은 사각형은 3행에 걸쳐 4열 전체를 차지하는 직사각형입니다. (0,0)부터 (2,3)까지의 0으로만 이루어진 직사각형의 넓이는 3 * 4 = 12입니다.*

## 힌트

- 이 문제는 'Largest Rectangle in Histogram' 문제와 유사합니다.
- 각 행을 기준으로, 현재 칸까지 연속된 0의 개수를 '높이 배열'로 관리하는 것이 핵심입니다.


## 알고리즘 요약

행별 최대 직사각형 넓이 계산 (Largest Rectangle in Histogram 활용)

## 풀이 해설

### 💡 풀이 아이디어

이 문제는 $N 	imes M$ 지도를 한 번에 처리하기 어렵습니다. 핵심은 모든 가능한 직사각형을 검사하는 대신, 직사각형의 '높이'를 기준으로 넓이를 계산하는 것입니다. 마치 직사각형을 그릴 때 바닥 행을 고정하고 그 위로 최대 높이를 확장하는 것과 같습니다.

**1. 높이 배열 (Height Array) 구축:**
$N$개의 행을 순차적으로 순회하면서, 각 열 $j$에 대해 현재 행 $i$까지 연속된 0의 개수, 즉 높이 $H[i][j]$를 계산합니다. 만약 $Grid[i][j]$가 1(장애물)이면 높이는 0이 되고, 0(빈 공간)이면 $H[i-1][j] + 1$이 됩니다.

**2. 히스토그램 최대 넓이 (Largest Rectangle in Histogram):**
각 행 $i$를 처리할 때마다, 해당 행의 높이 배열 $H[i]$는 하나의 히스토그램을 형성합니다. 이 히스토그램을 이용하여 '가장 넓은 직사각형의 넓이'를 구하는 문제입니다. 이 문제는 일반적으로 스택(Stack)을 사용하여 $O(M)$ 시간 복잡도로 해결할 수 있습니다.

**3. 전체 최대 넓이:**
모든 행 $i=0$부터 $N-1$까지 위 과정을 반복하며 얻은 최대 넓이 중 가장 큰 값을 최종 답으로 반환합니다.

**시간 복잡도 분석:**
*   높이 배열 구축: $O(N 	imes M)$ 시간. (매 행마다 $M$번의 계산)
*   히스토그램 최대 넓이 계산: 각 행마다 $O(M)$ 시간. (총 $N$번 반복)
*   전체 시간 복잡도: $O(N 	imes M) + N 	imes O(M) = O(N 	imes M)$. 이는 주어진 제약 조건 내에서 효율적입니다.

### ⚙️ 구현 단계 (Largest Rectangle in Histogram 함수)

1.  **스택 초기화:** 스택을 사용하여 현재까지 처리된 인덱스를 저장합니다. 이 스택은 높이 배열의 오름차순(혹은 특정 패턴)을 유지하는 데 사용됩니다.
2.  **반복 및 높이 계산:** 높이 배열의 모든 높이 $h$에 대해 반복합니다. 높이 $h$보다 작은 높이가 스택의 맨 위에 있는 높이보다 크다면, 스택에서 해당 높이를 팝(pop)하고, 이 높이를 기준으로 최대 넓이를 계산합니다.
3.  **넓이 계산:** 스택에서 팝된 높이 $h$가 $L$부터 $R$까지의 폭을 가질 때, 넓이는 $h 	imes (R - L + 1)$입니다. (스택의 크기 및 현재 인덱스를 활용하여 폭 계산)
4.  **마무리:** 모든 높이 배열 처리가 끝난 후, 스택에 남아있는 요소들을 모두 처리하여 최종 최대 넓이를 계산합니다.

## 참고 코드 (java)

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;
import java.util.StringTokenizer;

public class Solution {

    /**
     * 주어진 높이 배열(히스토그램)에서 최대 직사각형 넓이를 계산합니다.
     * Time Complexity: O(M)
     */
    private static int largestRectangleArea(int[] heights) {
        int n = heights.length;
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;

        for (int i = 0; i <= n; i++) {
            // i가 n일 경우, 0 높이를 강제로 넣어 스택에 남은 모든 요소를 처리하게 함
            int h = (i == n) ? 0 : heights[i];
            
            // 현재 높 h가 스택의 맨 위 높이보다 작거나 같으면, 스택을 비우지 않고 진행
            while (!stack.isEmpty() && h < heights[stack.peek()]) {
                int height = heights[stack.pop()];
                // 현재 인덱스 i가 오른쪽 경계(R+1), 스택의 맨 위가 왼쪽 경계(L-1) 역할을 함
                // 폭 = i - 1 - (스택의 맨 위 인덱스) = i - (스택의 맨 위 인덱스) - 1
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            
            // 현재 인덱스를 스택에 푸시
            if (i < n) {
                stack.push(i);
            }
        }
        return maxArea;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // N: 행의 개수, M: 열의 개수
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // Grid[i][j]는 0/1을 저장 (0: 빈 공간, 1: 장애물)
        int[][] grid = new int[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                // '0' 문자 -> 0, '1' 문자 -> 1로 변환하여 저장
                grid[i][j] = line.charAt(j) - '0'; 
            }   
        }

        // heights[j]는 현재 행까지 연속된 0의 높이를 저장하는 배열 (M 크기)
        int[] heights = new int[M];
        int maxArea = 0;

        // N개의 행을 순회하며 최대 넓이를 계산
        for (int i = 0; i < N; i++) {
            // 1. 높이 배열 업데이트 (Heights Array Update)
            for (int j = 0; j < M; j++) {
                if (grid[i][j] == 1) {
                    heights[j] = 0; // 장애물이면 높이 초기화
                } else { // grid[i][j] == 0
                    heights[j] += 1; // 빈 공간이면 높이 증가
                }
            }
            
            // 2. 현재 높이 배열(히스토그램)에서 최대 넓이 계산
            int currentArea = largestRectangleArea(heights);
            maxArea = Math.max(maxArea, currentArea);
        }

        System.out.println(maxArea);
    }
}
```
