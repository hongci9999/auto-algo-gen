# 최장 부분 문자열 (Longest Substring)
*java · 슬라이딩 윈도우 · 보통 · 문자열, 슬라이딩 윈도우, 자료구조*

## 입출력 환경

Java의 BufferedReader와 StringTokenizer를 사용하여 입력을 처리합니다.

## 문제

문자열 S와 정수 K가 주어집니다. 문자열 S의 부분 문자열 중에서, 서로 다른 문자의 개수가 K개 이하인 가장 긴 부분 문자열의 길이를 구하세요. 이 부분 문자열은 반드시 S의 연속된 부분 문자열이어야 합니다.

예시: S = "araac", K = 2
S의 부분 문자열 중 다른 문자가 2개 이하인 가장 긴 부분 문자열은 "araa" (길이 4) 입니다. (a, r만 포함)

## 입력

첫 번째 줄에는 문자열 S가 주어지고, 두 번째 줄에는 정수 K가 주어집니다.

## 출력

찾은 가장 긴 부분 문자열의 길이(정수)를 출력합니다.

## 제약 조건

S의 길이 N은 1부터 100,000까지입니다. K는 1부터 26까지의 정수입니다. 시간 복잡도는 O(N) 또는 O(N log N) 이내여야 합니다.

## 예제 1

**입력**
```
araac
2
```

**출력**
```
4
```

*다른 문자가 2개 이하인 가장 긴 부분 문자열은 "araa"이며, 길이는 4입니다.*

## 예제 2

**입력**
```
aabbcc
3
```

**출력**
```
6
```

*전체 문자열 "aabbcc" 자체가 다른 문자가 3개 이하이므로, 가장 긴 부분 문자열의 길이는 6입니다.*

## 예제 3

**입력**
```
abcde
1
```

**출력**
```
1
```

*다른 문자가 1개 이하인 부분 문자열은 "a", "b", "c", "d", "e"이며, 최대 길이는 1입니다.*

## 힌트

- 문자열을 순회하면서 현재 유효한 부분 문자열의 범위를 유지하는 슬라이딩 윈도우 기법을 사용해 보세요.
- 현재 윈도우 내의 문자 빈도를 기록하고, 고유 문자 개수를 체크할 자료구조(HashMap 또는 배열)가 필요합니다.


## 알고리즘 요약

슬라이딩 윈도우 (Sliding Window) 기법을 사용합니다. 두 포인터(Left, Right)를 사용하여 현재 윈도우 S[Left...Right]를 유지하고, 윈도우 내 고유 문자 개수가 K를 초과하면 Left 포인터를 이동시켜 윈도우를 축소합니다. 동시에 최대 윈도우 길이를 갱신합니다.

## 풀이 해설

풀이 해설:
1. 아이디어: 이 문제는 '최장 부분 문자열'이라는 조건과 '제약 조건(K개 이하의 고유 문자)'이 붙은 전형적인 슬라이딩 윈도우 문제입니다. 전체 문자열을 한 번만 순회하며, 현재 윈도우가 조건을 위반할 때마다 윈도우를 조정하는 방식으로 해결합니다.
2. 단계:
   a. 자료구조 준비: 현재 윈도우 S[L...R] 내의 문자 빈도를 저장할 HashMap(또는 배열)을 준비합니다. L과 R 두 개의 포인터를 0으로 초기화합니다.
   b. 확장 (Right 포인터 이동): R을 0부터 N-1까지 증가시키며 문자 S[R]을 윈도우에 포함시킵니다. 이 문자의 빈도를 Map에 추가합니다.
   c. 축소 (Left 포인터 이동): Map에 저장된 고유 문자(Map.size())의 개수가 K를 초과할 경우, 윈도우가 조건을 위반했다는 의미입니다. 따라서 Left 포인터를 이동시켜 윈도우를 축소해야 합니다. S[L] 문자를 Map에서 제거(빈도 감소)하고 L을 1 증가시킵니다. 이 과정을 Map.size() <= K가 될 때까지 반복합니다.
   d. 결과 갱신: 윈도우가 유효하게 유지될 때마다, 현재 윈도우의 길이 (R - L + 1)를 최대 길이와 비교하여 갱신합니다.
3. 시간 복잡도: R 포인터는 N번, L 포인터는 최대 N번 이동합니다. 각 단계에서 Map 연산은 O(1) 시간이 걸리므로, 전체 시간 복잡도는 O(N)입니다. 이는 매우 효율적입니다.

## 참고 코드 (java)

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 첫 번째 줄: 문자열 S
        String s = br.readLine();
        // 두 번째 줄: 정수 K
        int k = Integer.parseInt(br.readLine());

        // 슬라이딩 윈도우 구현
        int n = s.length();
        int left = 0;
        int maxLength = 0;
        // 문자의 빈도수를 저장하는 맵
        java.util.Map<Character, Integer> charCount = new HashMap<>();

        // Right 포인터를 이동시키며 윈도우 확장
        for (int right = 0; right < n; right++) {
            char charR = s.charAt(right);
            // 1. 현재 문자를 윈도우에 추가
            charCount.put(charR, charCount.getOrDefault(charR, 0) + 1);

            // 2. 윈도우가 조건을 위반했는지 확인하고, 위반했다면 왼쪽(L) 포인터로 축소
            // Map의 크기(고유 문자 개수)가 K를 초과할 때까지 축소합니다.
            while (charCount.size() > k) {
                char charL = s.charAt(left);
                
                // 왼쪽 문자를 제거
                int count = charCount.get(charL); 
                charCount.put(charL, count - 1);
                
                // 빈도수가 0이 되면 Map에서 키를 제거하여 고유 문자 개수를 줄입니다.
                if (count - 1 == 0) {
                    charCount.remove(charL);
                }
                
                // Left 포인터 이동
                left++;
            }
            
            // 3. 현재 윈도우의 길이(right - left + 1)를 최대 길이와 비교하여 갱신
            maxLength = Math.max(maxLength, right - left + 1);
        }

        System.out.println(maxLength);
    }
}
```
