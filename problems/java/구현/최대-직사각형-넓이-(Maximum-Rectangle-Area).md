# 최대 직사각형 넓이 (Maximum Rectangle Area)
*java · 구현 · 보통 · 배열, 구현*

## 입출력 환경

Java의 경우, 표준 입력(System.in)을 사용하여 N, M과 격자 데이터를 읽고, 결과를 표준 출력(System.out)으로 출력해야 합니다. 효율적인 입출력을 위해 BufferedReader와 StringTokenizer를 사용하는 것을 권장합니다.

## 문제

N개의 흑백 타일로 이루어진 직사각형 격자판이 주어집니다. 이 격자판에서 '1'로만 이루어진 가장 넓은 직사각형의 넓이를 구하는 문제입니다.

격자판의 크기는 N행 M열이며, 각 칸은 0 또는 1로 채워져 있습니다. 0은 흰색, 1은 검은색 타일을 의미합니다.

## 입력

첫째 줄에 N과 M이 주어집니다. (N: 행의 개수, M: 열의 개수)
다음 N줄에 걸쳐 M개의 정수(0 또는 1)가 공백으로 구분되어 주어지며, 각 줄이 한 행을 나타냅니다.

## 출력

가장 넓은 '1'로만 이루어진 직사각형의 넓이 (정수)를 출력합니다.

## 제약 조건

1 <= N, M <= 100
격자판의 모든 값은 0 또는 1입니다. (시간 복잡도는 O(N*M) 또는 O(N*M*min(N,M)) 이하가 권장됩니다.)

## 예제 1

**입력**
```
3 4
1 0 1 1
1 1 1 0
1 1 0 0
```

**출력**
```
4
```

*2행 1열부터 3행 2열까지의 2x2 직사각형이 가장 넓습니다. (1,1), (1,2), (2,1), (2,2) 위치의 1들.*

## 예제 2

**입력**
```
3 3
1 1 1
1 1 1
1 1 1
```

**출력**
```
9
```

*전체 격자판이 3x3의 직사각형을 이루어 가장 넓습니다.*

## 힌트

- 가장 넓은 직사각형은 반드시 어떤 행(Row)을 기준으로 '높이'가 결정되어야 합니다.
- 각 행을 기준으로, 해당 행을 포함하는 가장 높은 연속된 '1'의 높이를 계산하는 것이 핵심입니다.


## 알고리즘 요약

이 문제는 '최대 직사각형 넓이' 문제로, '히스토그램 최대 직사각형 넓이' 문제를 N번 반복하여 해결할 수 있습니다. 각 행을 기준으로, 해당 행의 1의 연속된 높이를 히스토그램으로 만들고, 이 히스토그램에서 최대 직사각형 넓이를 구합니다. 이를 모든 행에 대해 수행합니다.

## 풀이 해설

### 💡 아이디어: 히스토그램 최대 직사각형 넓이 응용

이 문제는 2차원 배열에서 최대 직사각형 넓이를 구하는 문제입니다. 일반적으로 O(N^2) 또는 O(N^3)의 풀이가 가능하지만, 더 효율적인 방법이 존재합니다.

핵심 아이디어는 '각 행을 기준으로, 그 행을 바닥으로 하는 최대 직사각형의 높이'를 계산하는 것입니다.

1. **높이 배열 (Height Array) 생성**: 먼저, N행 M열의 원본 배열 `A`가 주어졌을 때, 우리는 별도의 1차원 배열 `H` (높이 배열)를 만듭니다. `H[j]`는 j번째 열에 대해, 현재 행까지 연속적으로 1이 유지되는 최대 높이입니다.

2. **반복 및 계산**: 우리는 행(i)을 순회하며 이 높이 배열 `H`를 업데이트합니다. 만약 `A[i][j]`가 1이면, `H[j]`는 이전 행의 높이 `H[j] + 1`이 됩니다. 만약 `A[i][j]`가 0이면, `H[j]`는 0이 됩니다.

3. **히스토그램 최대 넓이 구하기**: 매 행 `i`가 끝날 때마다, 현재의 높이 배열 `H`는 하나의 '히스토그램'을 형성합니다. 이 히스토그램에서 가로로 가장 넓은 직사각형의 넓이(즉, 높이 배열 `H`를 사용하여 만들 수 있는 최대 넓이)를 구하고, 이 값을 전체 최대 넓이와 비교하여 갱신합니다.

### 🛠️ 히스토그램 최대 직사각형 넓이 계산 (O(M)):

주어진 높이 배열 `H` (크기 M)가 있을 때, 최대 넓이는 스택(Stack)을 이용해 O(M) 시간에 계산할 수 있습니다.

*   각 높이 `H[j]`를 막대의 높이라고 간주합니다.
*   스택을 사용하여, 현재 막대 `j`의 높이 `H[j]`보다 작거나 같은 가장 가까운 왼쪽 막대와 오른쪽 막대(L, R)를 찾습니다.
*   이때, 넓이는 `H[j] * (R - L - 1)`이 됩니다. 모든 막대에 대해 이 계산을 수행하고 최댓값을 찾습니다.

### ⏱️ 시간 복잡도:

*   행(N)을 순회: N번
*   각 행에서 높이 업데이트: O(M)
*   각 행에서 히스토그램 넓이 계산: O(M) (스택 사용)

총 시간 복잡도는 O(N * M)이 되어 매우 효율적입니다.

## 참고 코드 (java)

```java
import java.util.Arrays;
import java.util.Stack;
import java.util.Scanner;

public class Main {
    
    // 스택을 이용해 주어진 히스토그램 배열에서 최대 직사각형 넓이를 O(M)에 계산하는 함수
    public static int largestRectangleArea(int[] heights) {
        int n = heights.length;
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;

        for (int i = 0; i <= n; i++) {
            // i == n 일 때는, 모든 막대가 스택에 남아있을 수 있으므로 높이 0을 임시로 처리합니다.
            int h = (i == n) ? 0 : heights[i];
            
            while (!stack.isEmpty() && heights[stack.peek()] >= h) {
                int height = heights[stack.pop()];
                // 현재 높이(height)가 기준이 되는 직사각형의 폭은, 
                // 스택의 top()부터 현재 인덱스(i) 직전까지입니다.
                // 폭 = i (현재 인덱스) - stack.peek() - 1 (왼쪽 경계) + 1
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            
            if (i < n) {
                stack.push(i);
            } else {
                // i == n 일 때는, 모든 처리를 마쳤으므로 추가 로직은 필요 없습니다.
            }
        }
        return maxArea;
    }

    public static void main(String[] args) {
        // Java에서 효율적인 입출력을 위해 Scanner 대신 BufferedReader를 사용합니다.
        java.io.BufferedReader br = new java.io.BufferedReader(new java.io.InputStreamReader(System.in));
        String line = null;
        try {
            // 첫 줄에서 N과 M을 읽습니다.
            String[] nm = br.readLine().split("\s+");
            if (nm.length < 2) return; 
            int N = Integer.parseInt(nm[0]); // 행의 개수
            int M = Integer.parseInt(nm[1]); // 열의 개수

            // 격자판 데이터를 저장할 배열
            int[][] grid = new int[N][M];
            for (int i = 0; i < N; i++) {
                String[] rowData = br.readLine().split("\s+");
                for (int j = 0; j < M; j++) {
                    grid[i][j] = Integer.parseInt(rowData[j]);
                }
            } 
            
            // 높이 배열 (Height Array)을 저장할 배열. 크기는 M
            int[] heights = new int[M];
            int maxArea = 0;

            // 행(i)을 순회하며 높이 배열을 업데이트하고 최대 넓이를 계산합니다.
            for (int i = 0; i < N; i++) {
                // 1. 높이 배열 업데이트 (H[j] = grid[i][j] == 1 ? H[j] + 1 : 0)
                for (int j = 0; j < M; j++) {
                    if (grid[i][j] == 1) {
                        heights[j] += 1;
                    } else {
                        heights[j] = 0;
                    }
                }
                
                // 2. 현재 높이 배열(히스토그램)에서 최대 넓이 계산
                int currentMaxArea = largestRectangleArea(heights);
                
                // 3. 전체 최대 넓이 갱신
                maxArea = Math.max(maxArea, currentMaxArea);
            }
            
            System.out.println(maxArea);
            
        } catch (Exception e) {
            // 예외 처리 (입력 실패 등) 
        } 
    }
}
```
