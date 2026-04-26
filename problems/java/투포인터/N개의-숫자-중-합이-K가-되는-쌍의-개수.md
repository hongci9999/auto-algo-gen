# N개의 숫자 중 합이 K가 되는 쌍의 개수
*java · 투포인터 · 보통 · 배열, 투포인터, 정렬*

## 입출력 환경

Java 환경에서는 표준 입력을 사용하며, 대용량 입력을 처리하기 위해 BufferedReader와 StringTokenizer를 사용하는 것이 효율적입니다.

## 문제

정수 배열 `A`가 주어집니다. 이 배열에는 $N$개의 숫자가 포함되어 있습니다. 여러분은 이 배열에서 합이 특정 값 $K$가 되는 서로 다른 두 수의 쌍 $(A[i], A[j])$의 개수를 찾아야 합니다. 단, 같은 인덱스를 가진 숫자는 쌍을 이룰 수 없습니다. 이 문제는 순서가 중요하지 않으므로, $(A[i], A[j])$와 $(A[j], A[i])$는 같은 쌍으로 간주합니다. 배열의 원소값은 중복될 수 있습니다.

## 입력

첫째 줄에 정수 $N$이 주어지고, 다음 줄에 공백으로 구분된 $N$개의 정수 $A[0], A[1], \dots, A[N-1]$가 주어집니다.

## 출력

합이 $K$가 되는 쌍의 개수를 정수 형태로 출력합니다.

## 제약 조건

$-10^5 \le A[i] \le 10^5$, $1 \le N \le 10^5$. $K$ 값은 문제에서 별도로 주어지지 않았으므로, 문제 조건에 따라 $K$를 사용해야 합니다. (가정: 문제의 의도는 $K$가 주어진 경우이므로, $K$를 입력으로 받도록 수정하거나, $K$를 문제 본문에 포함해야 합니다. 여기서는 $K$를 입력으로 받는다고 가정합니다.)

**수정된 입력 형식:**
첫째 줄에 정수 $N$과 목표 합 $K$가 주어지고, 다음 줄에 공백으로 구분된 $N$개의 정수 $A[0], A[1], \dots, A[N-1]$가 주어집니다.

## 예제 1

**입력**
```
5 7
1 3 4 2 6
```

**출력**
```
3
```

*쌍은 (1, 6), (3, 4), (3, 2) 입니다. 총 3쌍입니다.*

## 예제 2

**입력**
```
6 10
2 2 5 5 8 8
```

**출력**
```
5
```

*쌍은 (2, 8)의 4개 조합과 (5, 5)의 1개 조합입니다. 총 5쌍입니다.*

## 힌트

- 쌍의 개수를 세는 문제는 시간 복잡도가 중요합니다.
- 투 포인터 기법은 배열이 정렬되어 있을 때 매우 효율적입니다.


## 알고리즘 요약

이 문제는 '합이 K가 되는 쌍의 개수'를 찾는 문제입니다. 배열을 미리 정렬한 후, 투 포인터(Two Pointers) 기법을 사용하여 시간 복잡도를 $O(N)$에 줄일 수 있습니다. 정렬 후, 한 포인터 $L$을 시작점에, 다른 포인터 $R$을 끝점에 두고, $A[L] + A[R]$의 합을 $K$와 비교하며 이동합니다. 만약 합이 $K$보다 작으면 $L$을 증가시키고, 크면 $R$을 감소시킵니다. 이때, 원소값이 중복되는 경우의 카운팅에 주의해야 합니다.

## 풀이 해설

### 💡 아이디어: 투 포인터와 카운팅

시간 복잡도를 $O(N^2)$에서 $O(N 	imes 	ext{정렬 시간})$으로 줄이는 것이 핵심입니다. 먼저 배열 $A$를 오름차순으로 정렬합니다. 이 후, 두 개의 포인터 $L$ (왼쪽)과 $R$ (오른쪽)을 각각 배열의 시작점과 끝점에 둡니다. $A[L] + A[R]$의 합을 $K$와 비교하며 포인터를 움직여 나갑니다.

### 🪜 단계별 풀이

1. **정렬**: 입력받은 배열 $A$를 오름차순으로 정렬합니다. (시간 복잡도: $O(N 	ext{ log } N)$)
2. **초기화**: 총 쌍의 개수를 저장할 변수 `count`를 0으로 초기화합니다. 포인터 $L=0$, $R=N-1$로 설정합니다.
3. **탐색**: $L < R$인 동안 반복합니다.
    a. **합 계산**: 현재 $A[L] + A[R]$의 합을 계산합니다.
    b. **합 비교**: 
        i. **합이 $K$보다 작을 때 ($A[L] + A[R] < K$):** 합을 키워야 하므로 $L$을 오른쪽으로 이동시킵니다 ($L++$).
        ii. **합이 $K$보다 클 때 ($A[L] + A[R] > K$):** 합을 줄여야 하므로 $R$을 왼쪽으로 이동시킵니다 ($R--$).
        iii. **합이 $K$와 같을 때 ($A[L] + A[R] = K$):** 쌍을 찾았습니다. 이 경우, $A[L]$과 $A[R]$이 각각 몇 번씩 반복되는지 (중복 횟수)를 확인해야 합니다. 만약 $A[L] = A[R]$이라면, $L$과 $R$ 사이의 모든 원소들이 같은 값이고 합이 $K$가 되므로, 조합 $C(m, 2) = m(m-1)/2$ 공식을 사용합니다. 그렇지 않다면, $A[L]$과 $A[R]$이 각각 반복되는 횟수 $countL$과 $countR$을 센 후, $countL 	imes countR$ 만큼의 쌍을 더합니다. 이후 $L$과 $R$을 각각 전진/후진시키고, 다음 탐색을 위해 $L$과 $R$의 포인터를 조정합니다.
4. **종료**: $L 	o R$이 될 때까지 반복한 후, `count`를 반환합니다.

### ⏱️ 시간 복잡도

배열 정렬에 $O(N 	ext{ log } N)$이 걸리고, 투 포인터 탐색은 포인터가 한 번씩만 움직이므로 $O(N)$이 걸립니다. 전체 시간 복잡도는 $O(N 	ext{ log } N)$입니다. (이는 $N$이 최대 $10^5$일 때 충분히 빠릅니다.)

## 참고 코드 (java)

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        // 대용량 입력을 위한 설정
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // N: 배열 크기, K: 목표 합
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 배열 A 읽기
        int[] A = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        // 1. 배열을 정렬합니다. (O(N log N))
        Arrays.sort(A);

        long count = 0;
        int left = 0;
        int right = N - 1;

        // 2. 투 포인터 탐색 (O(N))
        while (left < right) {
            int sum = A[left] + A[right];
            
            if (sum < K) {
                // 합이 K보다 작으면, 왼쪽 포인터를 이동시켜 합을 키운다.
                left++;
            } else if (sum > K) {
                // 합이 K보다 크면, 오른쪽 포인터를 이동시켜 합을 줄인다.
                right--;
            } else { // sum == K
                // 합이 K와 같을 때
                
                // 1. 현재 A[left]과 A[right]이 같은 값인지 확인
                if (A[left] == A[right]) {
                    // 모든 원소가 같고 합이 K가 될 때 (예: 5, 5, 5, 5, K=10)
                    // left부터 right까지의 원소 개수 m = right - left + 1
                    long m = right - left + 1;
                    // 조합 C(m, 2) = m * (m - 1) / 2
                    count += m * (m - 1) / 2;
                    // 모든 쌍을 세었으므로, 반복 중단
                    break;
                } else { 
                    // A[left]과 A[right]이 다를 때
                    // A[left]의 연속된 출현 횟수 (countL)
                    int valL = A[left];
                    int countL = 0;
                    int tempL = left;
                    while (tempL < N && A[tempL] == valL) {
                        countL++;
                        tempL++;
                    }
                    
                    // A[right]의 연속된 출현 횟수 (countR)
                    int valR = A[right];
                    int countR = 0;
                    int tempR = right;
                    while (tempR >= 0 && A[tempR] == valR) {
                        countR++;
                        tempR--;
                    }
                    
                    // 쌍의 개수 = countL * countR
                    count += (long) countL * countR;
                    
                    // 카운팅한 영역을 건너뛰기 위해 포인터 이동
                    left = tempL;
                    right = tempR;
                }
            }
        }

        System.out.println(count);
    }
}
```
