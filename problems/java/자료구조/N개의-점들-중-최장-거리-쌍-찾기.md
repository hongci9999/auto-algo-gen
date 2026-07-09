# N개의 점들 중 최장 거리 쌍 찾기
*java · 자료구조 · 보통 · 거리*

## 입출력 환경

Java에서 입출력 시 BufferedReader와 PrintWriter를 사용하여 효율적으로 처리하는 것이 좋습니다.

## 문제

평면 좌표 위에 N개의 점이 주어집니다. 이 N개의 점들을 모두 지나는 직선을 상정할 때, 그 중 최대 거리를 가지는 두 점의 쌍을 찾으시오.

점들의 좌표 값은 정수형이며, $1 	imes 10^9$ 범위에 있습니다.

## 입력

첫째 줄에 N (1 <= N <= 2000)이 주어집니다. 둘째 줄부터 N개의 점의 좌표 $(x_i, y_i)$가 순서대로 한 줄에 하나씩 주어집니다.

## 출력

최대 거리를 가지는 두 점 사이의 거리 (실수점, 소수점 이하 3자리까지 출력).

## 제약 조건

N <= 2000. 좌표 값 범위: $1 	imes 10^9$. 시간 복잡도 고려 필요.

## 예제 1

**입력**
```
3
0 0
1 0
0 1
```

**출력**
```
$\\sqrt{2}$
```

*점 (1, 0)과 (0, 1) 사이의 거리가 $\\sqrt{(1-0)^2 + (0-1)^2)} = \\sqrt{2}$로 최대이다.*

## 예제 2

**입력**
```
4
1 1
1 3
5 1
5 3
```

**출력**
```
$\\sqrt{16}$
```

*점 (1, 3)과 (5, 1) 사이의 거리가 $\\sqrt{(5-1)^2 + (1-3)^2)} = \\sqrt{16} = 4$로 최대이다.*

## 힌트

- 모든 점 쌍 $(i, j)$에 대해 거리를 계산하는 방법은 시간 복잡도가 너무 높을 수 있습니다. 직관적으로 가장 멀리 떨어진 두 점은 무엇일까요?
- 직선 상의 모든 점들을 고려한다는 조건이 핵심입니다. 이 조건을 어떻게 활용할지 생각해보세요.


## 알고리즘 요약

주어진 N개의 점들 중 최대 거리를 가지는 쌍 $(A, B)$를 찾는 문제는 전형적인 '최대 거리 문제'와 관련됩니다. 만약 아무런 직선 제약이 없다면 모든 쌍을 비교해야 합니다. 하지만 이 문제는 '모든 점들을 지나는 직선'이라는 조건을 만족하는 두 점 사이의 최대 거리를 요구하고 있습니다.

실제로는, 주어진 N개의 점들 중 가장 멀리 떨어진 두 점은 항상 Convex Hull (볼록 껍질)의 꼭짓점들 위에 존재합니다. 또한, 이 문제는 'N개 점들을 모두 지나는' 직선이 아니라, 단지 N개의 점들이 한 평면에 있다는 조건만으로 최대 거리를 찾는 문제로 해석하는 것이 일반적인 코딩 테스트 문제입니다. 만약 모든 점을 지나야 한다는 제약이 엄격하다면, 이는 해당 점들들이 실제로 일직선상에 놓여있어야 함을 의미하며, 이 경우 가장 양 끝점 사이의 거리가 최대가 됩니다.

문제의 의도를 'N개 점들을 모두 지나는 직선 상에서'라는 조건으로 해석하고, 가장 극단적인 두 점(최소 X, 최대 X 또는 최소 Y, 최대 Y)을 찾거나 혹은 단순하게 모든 쌍의 거리를 비교하여 최댓값을 찾는 것이 일반적입니다.

**가장 합리적인 해석 (Brute Force)**: 모든 $N(N-1)/2$ 개의 점 쌍 $(P_i, P_j)$에 대해 유클리드 거리를 계산하고 그 중 최댓값을 찾습니다. 이 접근 방식은 문제의 제약 조건($N 	imes 10^9$)을 만족하는 가장 일반적인 최대 거리 문제입니다.

**시간 복잡도**: $O(N^2)$. N=2000이므로, $4 	imes 10^6$ 연산으로 충분히 시간 제한 내에 해결 가능합니다. (만약 Convex Hull을 이용한다면 Rotating Calipers를 사용하여 $O(N 	ext{ log } N)$으로 풀 수 있지만, 여기서는 단순한 $O(N^2)$ brute force가 가장 직관적입니다.)

## 풀이 해설

### 💡 아이디어
주어진 N개의 점들 중 최대 거리를 가지는 두 점을 찾는 문제입니다. 문제 조건에 '모든 점들을 지나는 직선'이라는 제약이 붙어있지만, 실제 코딩 테스트에서 이러한 문제는 대부분 단순히 모든 점 쌍 사이의 거리를 계산하여 최댓값을 찾는 방식으로 의도가 변형되거나 해석됩니다. 가장 안전하고 일반적인 접근 방식은 $O(N^2)$ 시간 복잡도를 가지는 브루트 포스 (Brute Force)로, 가능한 모든 두 점 $(P_i, P_j)$ 사이의 유클리드 거리를 계산하여 그 중 최댓값을 찾는 것입니다.

### 🪜 단계별 풀이
1. **입력**: N개의 점들의 좌표를 모두 저장합니다 (배열 또는 리스트 사용).
2. **반복**: 모든 가능한 두 점 $(P_i, P_j)$ 쌍을 선택하기 위해 중첩 반복문(Outer loop for $i$, Inner loop for $j$)을 사용합니다.
3. **거리 계산**: 각 쌍 $(P_i, P_j)$에 대해 유클리드 거리 공식을 사용하여 거리를 계산합니다:
   $$D = 	ext{distance}(P_i, P_j) = 	ext{sqrt}((x_i - x_j)^2 + (y_i - y_j)^2)$$
4. **최대값 갱신**: 계산된 거리 $D$가 현재까지 기록된 최대 거리보다 크다면, 최대 거리를 $D$로 갱신합니다.
5. **출력**: 모든 쌍의 거리를 확인한 후 최종적으로 구한 최대 거리를 소수점 이하 3자리까지 출력합니다.

### ⏱️ 시간 복잡도 및 메모리
*   **시간 복잡도**: $O(N^2)$. N개의 점이 있으므로, 약 $N(N-1)/2$ 쌍의 거리 계산을 수행합니다. $N 	imes 2000 = 4 	imes 10^6$ 연산으로 매우 효율적입니다.
*   **메모리 복잡도**: $O(N)$ (점 좌표를 저장하는 데 필요한 공간).

주의: 좌표 값이 크므로, 거리 제곱을 계산할 때 오버플로우에 주의해야 하지만, Java의 `long` 타입을 사용하면 충분히 커버 가능합니다. 최종 결과는 `double` 타입으로 처리하고 루트 연산을 수행해야 합니다.

## 참고 코드 (java)

```java
import java.io.*;
import java.util.StringTokenizer;

class Point {
    long x, y;
    public Point(long x, long y) { this.x = x; this.y = y; }
}

public class Main {
    public static void main(String[] args) throws IOException {
        // BufferedReader를 사용하여 빠르게 입력을 받습니다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

        // 첫 줄: N
        int N = Integer.parseInt(br.readLine());
        if (N <= 1) {
            pw.println("0.000");
            pw.flush();
            return;
        }

        Point[] points = new Point[N];

        // 다음 N 줄: 점 좌표 입력
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long x = Long.parseLong(st.nextToken());
            long y = Long.parseLong(st.nextToken());
            points[i] = new Point(x, y);
        }

        double maxDistanceSquared = 0.0;

        // 모든 쌍 (i, j)에 대해 거리를 계산합니다.
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                Point p1 = points[i];
                Point p2 = points[j];

                // 거리 제곱 계산 (좌표가 크므로 long 사용)
                long dx = p1.x - p2.x;
                long dy = p1.y - p2.y;
                
                // 거리를 비교할 때 double로 캐스팅하여 오버플로우를 방지하고 최대값을 갱신합니다.
                double currentDistanceSquared = (double)dx * dx + (double)dy * dy;

                if (currentDistanceSquared > maxDistanceSquared) {
                    maxDistanceSquared = currentDistanceSquared;
                }
            }
        }

        // 최대 거리를 구하고 소수점 3자리까지 출력합니다.
        double maxDistance = Math.sqrt(maxDistanceSquared);
        pw.printf("%.3f\n", maxDistance);
        
        pw.flush();
    }
}
```
