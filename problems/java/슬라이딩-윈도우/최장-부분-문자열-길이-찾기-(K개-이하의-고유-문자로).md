# 최장 부분 문자열 길이 찾기 (K개 이하의 고유 문자로)
*java · 슬라이딩 윈도우 · 보통 · 문자열, 슬라이딩 윈도우, HashMap*

## 입출력 환경

Java 환경에서 표준 입력을 처리하기 위해 java.util.Scanner 또는 BufferedReader를 사용합니다. 여기서는 String과 Integer를 분리하여 입력받는다고 가정합니다.

## 문제

주어진 문자열 $S$와 정수 $K$가 주어집니다. $S$의 모든 부분 문자열 중, 고유한 문자의 종류(distinct characters)가 최대 $K$개 이하인 가장 긴 부분 문자열의 길이를 구하는 문제입니다.

예시: S = "araac", K = 2 
"raa"는 'r', 'a' 두 개의 고유 문자를 가지므로 유효하며, 길이는 3입니다. 모든 부분 문자열을 탐색할 필요 없이 최장 길이를 찾아야 합니다.

## 입력

첫째 줄에 문자열 S와 공백으로 구분된 정수 K가 한 줄에 입력됩니다 (예: "araac" 2).

## 출력

가장 긴 부분 문자열의 길이(정수)를 출력합니다.

## 제약 조건

문자열 S의 길이는 1부터 10만 이하이며, K는 1 이상 26 이하입니다. 시간 복잡도는 O(N) 수준을 목표로 합니다.

## 예제 1

**입력**
```
"araac" 2
```

**출력**
```
3
```

*고유 문자가 2개 이하인 가장 긴 부분 문자열은 "raa" 또는 "aac"이며, 길이는 3입니다.*

## 예제 2

**입력**
```
"eceba" 2
```

**출력**
```
3
```

*고유 문자가 2개 이하인 가장 긴 부분 문자열은 "ece"나 "ceb"이며, 길이는 3입니다. 전체는 'e', 'c', 'b', 'a'로 최대 4개입니다.*

## 예제 3

**입력**
```
"abcde" 5
```

**출력**
```
5
```

*모든 문자가 고유하므로, 가장 긴 부분 문자열은 전체 문자열인 "abcde"이며 길이는 5입니다.*

## 힌트

- Sliding Window (슬라이딩 윈도우) 기법을 사용하면 시간 복잡도를 최적화할 수 있습니다.
- 현재 윈도우 내의 문자의 종류(distinct count)를 효율적으로 추적하기 위해 해시맵(HashMap)이나 배열을 활용하세요.


## 알고리즘 요약

슬라이딩 윈도우 기법: 윈도우의 시작 포인터 $L$과 끝 포인터 $R$을 사용하여 현재 부분 문자열 $S[L..R]$를 유지합니다. 문자의 종류 개수가 $K$를 초과하면, $L$을 이동시켜 왼쪽 문자를 제거하고 윈도우를 축소시킵니다. 그렇지 않으면 $R$을 이동시키며 윈도우를 확장합니다. 매 단계마다 현재 윈도우의 길이를 최대 길이와 비교하여 업데이트합니다.

## 풀이 해설

풀이 아이디어는 슬라이딩 윈도우(Sliding Window) 기법을 사용하는 것입니다. 이 문제를 단순하게 풀 경우 모든 부분 문자열에 대해 고유 문자의 개수를 세야 하므로 $O(N^2)$ 또는 그 이상의 복잡도가 발생할 수 있습니다.

**1. 단계 설정:**
*   두 포인터 $L$ (Left)과 $R$ (Right)을 0으로 초기화하여 현재 유효한 윈도우를 나타냅니다.
*   문자 빈도를 저장하고 고유 문자 개수를 계산하기 위해 `HashMap<Character, Integer>` 또는 크기 26의 배열을 사용합니다.
*   최대 길이를 저장할 변수 `maxLength`를 0으로 초기화합니다.

**2. 윈도우 확장 (R 이동):**
*   $R$ 포인터를 문자열 끝까지 한 칸씩 전진시키며 현재 문자를 맵에 추가하고 빈도를 증가시킵니다.

**3. 윈도우 축소 (L 이동 - 제약 조건 확인):**
*   만약 현재 고유한 문자의 종류가 $K$를 초과하게 된다면, 유효하지 않은 상태이므로 윈도우를 축소해야 합니다.
*   $L$ 포인터를 전진시키고, $S[L]$의 빈도를 줄입니다. 만약 $S[L]$의 빈도가 0이 되어 사라지면, 고유 문자 종류가 하나 감소했음을 기록합니다.
*   이 과정을 반복하여 고유 문자의 개수가 다시 $K$ 이하가 될 때까지 진행합니다.

**4. 최대 길이 갱신:**
*   윈도우의 크기 $(R - L + 1)$는 항상 유효한 상태를 나타내므로, 매 단계마다 이 길이를 `maxLength`와 비교하여 최댓값을 갱신합니다.

**시간 복잡도:** $L$과 $R$ 포인터 모두 문자열을 한 번만 순회하며 최대 $N$번의 이동을 하므로, 시간 복잡도는 $O(N)$입니다. 공간 복잡도는 고유 문자의 최대 개수($26$)에 비례하는 $O(	ext{알파벳 크기})$ 또는 $O(1)$로 일정합니다.

## 참고 코드 (java)

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        // 테스트 환경에 맞게 입력 형식을 가정하고 처리합니다.
        // 실제 코딩테스트에서는 Scanner나 BufferedReader를 사용하여 한 줄 전체를 읽는 방식이 일반적입니다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();

        if (line == null || line.trim().isEmpty()) return;

        // 예시 입력 형식: "araac" 2 와 같이 문자열과 숫자가 붙어있을 수 있으므로 분리하여 처리
        String[] parts = line.split("\s+");
        if (parts.length < 2) { 
             // 테스트 시뮬레이션을 위해 샘플 값을 하드코딩하거나, 정확한 입력 로직이 필요합니다.
             // 여기서는 첫 번째 파트가 문자열 S, 두 번째 파트가 K라고 가정하고 진행합니다.
            System.out.println("Error: Invalid input format.");
            return;
        }

        String s = parts[0].replace("\"", ""); // 따옴표 제거 처리
        int k; 
        try {
             k = Integer.parseInt(parts[1]);
         } catch (NumberFormatException e) {
             System.out.println("Error: K must be an integer.");
             return;
         }

        System.out.println(longestSubstringWithKDistinct(s, k));
    }

    /**
     * 고유 문자가 최대 K개인 가장 긴 부분 문자열의 길이를 계산합니다.
     * @param s 원본 문자열
     * @param k 허용되는 고유 문자 개수
     * @return 최대 길이
     */
    public static int longestSubstringWithKDistinct(String s, int k) {
        if (s == null || s.isEmpty() || k <= 0) return 0;

        // 윈도우 내의 문자 빈도를 저장합니다.
        HashMap<Character, Integer> charFrequency = new HashMap<>();
        int left = 0; // 왼쪽 포인터
        int maxLength = 0;

        // R을 오른쪽으로 이동시키며 윈도우를 확장 (R은 끝 인덱스)
        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);
            
            // 1. 현재 문자를 윈도우에 추가하고 빈도를 증가시킵니다.
            charFrequency.put(currentChar, charFrequency.getOrDefault(currentChar, 0) + 1);

            // 2. 고유 문자 개수가 K를 초과하면 윈도우 축소 (L 이동)
            while (charFrequency.size() > k) {
                char leftChar = s.charAt(left);
                
                // 왼쪽 문자의 빈도를 감소시킵니다.
                int count = charFrequency.get(leftChar) - 1;
                charFrequency.put(leftChar, count);
                
                // 빈도가 0이 되면 해당 문자는 더 이상 윈도우에 존재하지 않으므로 제거합니다.
                if (count == 0) {
                    charFrequency.remove(leftChar);
                }
                
                // 왼쪽 포인터를 한 칸 전진시킵니다.
                left++; 
            }
            
            // 3. 현재 유효한 윈도우의 길이를 최대 길이와 비교하여 업데이트합니다.
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
```
