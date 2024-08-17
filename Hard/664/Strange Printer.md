# Intuition

When I first tackled this problem, I was thinking about how to minimize the number of turns needed to print a given string. The unique properties of the printer - being able to print sequences of the same character and overwrite existing characters - made me realize that this wasn't a straightforward printing process.

My initial thoughts was to find patterns in the string that could be exploited to reduce the number of turns. It struck me that consecutive identical characters could be printed in one go, which led to the idea of simplifying the input string by removing these duplicates right from the start.

then I realized that the real challenge is in identifying opportunities where we could save turns by printing characters that appear later in the string simultaneously with earlier occurrences. This insight pointed towards a dynamic programming (DP) solution, where we could build up our answer by solving smaller subproblems first.

However, I felt that a straightforward DP approach might not be efficient enough. So what if we could quickly identify where matching characters occur in the string? This led me to the idea of precomputing the next occurrence of each character, which would allow us to jump directly to potential matches without scanning the entire string repeatedly.



# Approach

Let's break down the approach step by step, using pseudo-code to illustrate the concepts:

1. **Preprocessing the Input**
   We start by simplifying our problem, removing consecutive duplicate characters:

   ```
   function removeConsecutiveDuplicates(s):
       result = empty list
       for each character c in s:
           if result is empty or c != last element in result:
               add c to result
       return result
   ```

   This step is crucial because consecutive identical characters can always be printed in a single turn, so they don't affect our minimum turn count. It also potentially reduces the size of our problem, making subsequent steps more efficient.

2. **Setting Up the Dynamic Programming Table**
   We create a 2D table to store our DP results:

   ```
   m = length of simplified string
   dp = 2D array of size m x m, initialized with MAX_VALUE
   for i from 0 to m-1:
       dp[i][i] = 1  // It takes 1 turn to print a single character
   ```

   Here, `dp[i][j]` will represent the minimum number of turns needed to print the substring from index i to j (inclusive).

3. **Precomputing Next Occurrences**
   This is a key optimization in our approach. We create a data structure to quickly find the next occurrence of each character:

   ```
   function computeNextOccurrences(chars):
       lastSeen = empty map
       nextOccurrence = array of size m, initialized with -1
       for i from m-1 down to 0:
           c = chars[i]
           if c exists in lastSeen:
               nextOccurrence[i] = lastSeen[c]
           lastSeen[c] = i
       return nextOccurrence
   ```

   This precomputation allows us to efficiently jump to the next matching character without searching through the entire string each time we need to find a match.

4. **Filling the DP Table**
   Now we come to the core of our algorithm. We fill the DP table in a bottom-up manner:

   ```
   for length from 2 to m:
       for start from 0 to m - length:
           end = start + length - 1
           
           // Initial case: print each character separately
           dp[start][end] = dp[start+1][end] + 1
           
           // Try to find a better solution by matching characters
           currentChar = chars[start]
           nextPos = nextOccurrence[start]
           
           while nextPos != -1 and nextPos <= end:
               dp[start][end] = min(dp[start][end], 
                                    dp[start][nextPos-1] + 
                                    (nextPos+1 <= end ? dp[nextPos+1][end] : 0))
               nextPos = nextOccurrence[nextPos]
   ```

   Let's break this down further:

   - We consider substrings of increasing length, from 2 to the full string length.
   - For each substring, we start with the assumption that we print the first character separately and then handle the rest (`dp[start+1][end] + 1`).
   - Then, we try to optimize by finding matching characters. We use our precomputed `nextOccurrence` to quickly jump to potential matches.
   - When we find a match, we consider splitting the problem into three parts:
     1. From `start` to just before `nextPos`
     2. The matching characters at `start` and `nextPos`
     3. From just after `nextPos` to `end`
   - We calculate the turns needed for parts 1 and 3 using our DP table, and implicitly consider part 2 as free (since we're printing it with the character at `start`).
   - We keep doing this for all potential matches, always keeping the minimum number of turns found.

5. **Retrieving the Result**
   After filling the entire DP table, our answer is in `dp[0][m-1]`, representing the minimum turns needed to print the entire simplified string.

This approach combines dynamic programming with an optimization that allows us to quickly find matching characters. By precomputing the next occurrences, we avoid unnecessary iterations and comparisons, making our solution more efficient.

The key insight here is that we're not just solving smaller subproblems, but we're also using additional information (the next occurrences) to make smarter decisions about how to split our problem. This allows us to potentially skip over many unnecessary comparisons and subproblems.

### Complexity

- **Time complexity: $O(n^3)$**
  Let's break this down:
  - Removing consecutive duplicates: O(n)
  - Setting up the DP table: O(n^2)
  - Precomputing next occurrences: O(n)
  - Filling the DP table: O(n^3)
    - We have three nested loops:
      1. The outer loop for substring length: O(n)
      2. The middle loop for start positions: O(n)
      3. The inner while loop for finding matches: O(n) in the worst case
  
  The dominant factor here is the O(n^3) from filling the DP table, so that's our overall time complexity.

- **Space complexity: $O(n^2)$**
  - The DP table is the main space consumer, requiring O(n^2) space.
  - The simplified character list, next occurrence array, and lastSeen map each take O(n) space.
  - Therefore, the overall space complexity is O(n^2).



### Code
```Java []
class Solution {
    public int strangePrinter(String s) {
        if (s == null || s.isEmpty()) return 0;
        
        // Remove consecutive duplicates
        List<Character> filteredChars = new ArrayList<>();
        for (char c : s.toCharArray()) {
            if (filteredChars.isEmpty() || c != filteredChars.get(filteredChars.size() - 1)) {
                filteredChars.add(c);
            }
        }
        
        int m = filteredChars.size();
        int[][] dp = new int[m][m];
        Arrays.fill(dp[0], Integer.MAX_VALUE);
        for (int i = 0; i < m; ++i) {
            dp[i][i] = 1;
        }
        
        // Precompute the next occurrence for each character
        Map<Character, Integer> lastSeen = new HashMap<>();
        int[] nextOccurrence = new int[m];
        Arrays.fill(nextOccurrence, -1);
        for (int i = m - 1; i >= 0; --i) {
            char c = filteredChars.get(i);
            if (lastSeen.containsKey(c)) {
                nextOccurrence[i] = lastSeen.get(c);
            }
            lastSeen.put(c, i);
        }
        
        // Fill the DP table
        for (int length = 2; length <= m; ++length) {
            for (int start = 0; start <= m - length; ++start) {
                int end = start + length - 1;
                // Initial case: print each character separately
                dp[start][end] = dp[start + 1][end] + 1;
                // Try to find a better solution by matching characters
                char currentChar = filteredChars.get(start);
                int nextPos = nextOccurrence[start];
                while (nextPos != -1 && nextPos <= end) {
                    dp[start][end] = Math.min(dp[start][end], dp[start][nextPos - 1] + (nextPos + 1 <= end ? dp[nextPos + 1][end] : 0));
                    nextPos = nextOccurrence[nextPos];
                }
            }
        }
        
        return dp[0][m - 1];
    }

}


//https://leetcode.com/problems/strange-printer/submissions/1358718572/
```
```C++ []
class Solution {
public:
    int strangePrinter(const std::string& s) {
        if (s.empty()) return 0;
        
        // Remove consecutive duplicates
        std::vector<char> filtered_chars;
        for (char c : s) {
            if (filtered_chars.empty() || c != filtered_chars.back()) {
                filtered_chars.push_back(c);
            }
        }
        
        int m = filtered_chars.size();
        
        // Initialize DP table and last occurrence tracking
        std::vector<std::vector<int>> dp(m, std::vector<int>(m, std::numeric_limits<int>::max()));
        std::vector<int> next_occurrence(m, -1);
        
        // Fill the DP table with base cases
        for (int i = 0; i < m; ++i) {
            dp[i][i] = 1;
        }
        
        // Precompute the next occurrence for each character
        std::unordered_map<char, int> last_seen;
        for (int i = m - 1; i >= 0; --i) {
            char c = filtered_chars[i];
            if (last_seen.find(c) != last_seen.end()) {
                next_occurrence[i] = last_seen[c];
            }
            last_seen[c] = i;
        }
        
        // Fill the DP table
        for (int length = 2; length <= m; ++length) {  // length of substring
            for (int start = 0; start <= m - length; ++start) {
                int end = start + length - 1;
                // Initial case: print each character separately
                dp[start][end] = dp[start + 1][end] + 1;
                // Try to find a better solution by matching characters
                char current_char = filtered_chars[start];
                int next_pos = next_occurrence[start];
                while (next_pos != -1 && next_pos <= end) {
                    dp[start][end] = std::min(dp[start][end], dp[start][next_pos - 1] + (next_pos + 1 <= end ? dp[next_pos + 1][end] : 0));
                    next_pos = next_occurrence[next_pos];
                }
            }
        }
        
        return dp[0][m - 1];
    }
};


//Ignore this part
static const auto speedup = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();

//https://leetcode.com/submissions/detail/1358710598/
```

```Python []
class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
        
        #Remove consecutive duplicates
        filtered_chars = []
        for char in s:
            if not filtered_chars or char != filtered_chars[-1]:
                filtered_chars.append(char)
        
        m = len(filtered_chars)
        
        # Initialize DP table and last occurrence tracking
        dp = [[float('inf')] * m for _ in range(m)]
        next_occurrence = [-1] * m
        
        # Fill the DP table with base cases
        for i in range(m):
            dp[i][i] = 1
        
        # Precompute the next occurrence for each character
        last_seen = {}
        for i in range(m - 1, -1, -1):
            if filtered_chars[i] in last_seen:
                next_occurrence[i] = last_seen[filtered_chars[i]]
            last_seen[filtered_chars[i]] = i
        
        # Fill the DP table
        for length in range(2, m + 1):  # length of substring
            for start in range(m - length + 1):
                end = start + length - 1
                # Initial case: print each character separately
                dp[start][end] = dp[start + 1][end] + 1
                # Try to find a better solution by matching characters
                current_char = filtered_chars[start]
                next_pos = next_occurrence[start]
                while next_pos != -1 and next_pos <= end:
                    dp[start][end] = min(dp[start][end], dp[start][next_pos - 1] + (dp[next_pos + 1][end] if next_pos + 1 <= end else 0))
                    next_pos = next_occurrence[next_pos]
        
        return dp[0][m - 1]


#Ignore this part
def main():
    import sys
    import json
    
    input_data = sys.stdin.read().strip()
    test_cases = input_data.splitlines()
    results = []
    
    for case in test_cases:
        s = json.loads(case)
        results.append(Solution().strangePrinter(s))
    
    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()
    exit(0)


#https://leetcode.com/problems/strange-printer/submissions/1358719653/
```
```Go []
// Function to compute the minimum number of turns required
func strangePrinter(s string) int {
	if len(s) == 0 {
		return 0
	}

	// Remove consecutive duplicates
	var filteredChars []rune
	for _, char := range s {
		if len(filteredChars) == 0 || char != filteredChars[len(filteredChars)-1] {
			filteredChars = append(filteredChars, char)
		}
	}

	m := len(filteredChars)
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, m)
		for j := range dp[i] {
			dp[i][j] = int(1e9)
		}
	}

	// Fill the DP table with base cases
	for i := 0; i < m; i++ {
		dp[i][i] = 1
	}

	// Precompute the next occurrence for each character
	lastSeen := make(map[rune]int)
	nextOccurrence := make([]int, m)
	for i := m - 1; i >= 0; i-- {
		char := filteredChars[i]
		if pos, found := lastSeen[char]; found {
			nextOccurrence[i] = pos
		} else {
			nextOccurrence[i] = -1
		}
		lastSeen[char] = i
	}

	// Fill the DP table
	for length := 2; length <= m; length++ {
		for start := 0; start <= m-length; start++ {
			end := start + length - 1
			dp[start][end] = dp[start+1][end] + 1
			nextPos := nextOccurrence[start]
			for nextPos != -1 && nextPos <= end {
				if nextPos+1 <= end {
					dp[start][end] = min(dp[start][end], dp[start][nextPos-1]+dp[nextPos+1][end])
				} else {
					dp[start][end] = min(dp[start][end], dp[start][nextPos-1])
				}
				nextPos = nextOccurrence[nextPos]
			}
		}
	}

	return dp[0][m-1]
}

// Helper function to find the minimum of two integers
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}


//https://leetcode.com/problems/strange-printer/submissions/1358716459/
```
```Rust []
use std::collections::HashMap;
use std::cmp::min;

impl Solution {
    pub fn strange_printer(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let mut filtered_chars = Vec::new();
        
        // Remove consecutive duplicates
        for &c in &s {
            if filtered_chars.is_empty() || c != *filtered_chars.last().unwrap() {
                filtered_chars.push(c);
            }
        }

        let m = filtered_chars.len();
        let mut dp = vec![vec![i32::MAX; m]; m];
        let mut next_occurrence = vec![None; m];
        
        // Fill the DP table with base cases
        for i in 0..m {
            dp[i][i] = 1;
        }

        // Precompute the next occurrence for each character
        let mut last_seen = HashMap::new();
        for i in (0..m).rev() {
            let c = filtered_chars[i];
            if let Some(&pos) = last_seen.get(&c) {
                next_occurrence[i] = Some(pos);
            }
            last_seen.insert(c, i);
        }

        // Fill the DP table
        for length in 2..=m {
            for start in 0..=m - length {
                let end = start + length - 1;
                dp[start][end] = dp[start + 1][end] + 1;
                if let Some(mut next_pos) = next_occurrence[start] {
                    while next_pos <= end {
                        if next_pos + 1 <= end {
                            dp[start][end] = min(dp[start][end], dp[start][next_pos - 1] + dp[next_pos + 1][end]);
                        } else {
                            dp[start][end] = min(dp[start][end], dp[start][next_pos - 1]);
                        }
                        if let Some(pos) = next_occurrence[next_pos] {
                            next_pos = pos;
                        } else {
                            break;
                        }
                    }
                }
            }
        }

        dp[0][m - 1]
    }
}


//https://leetcode.com/problems/strange-printer/submissions/1358706742/
```

```JavaScript []
/**
 * @param {string} s
 * @return {number}
 */
var strangePrinter = function(s) {
    if (s.length === 0) {
        return 0;
    }

    // Remove consecutive duplicates
    let filteredChars = [];
    for (const char of s) {
        if (filteredChars.length === 0 || char !== filteredChars[filteredChars.length - 1]) {
            filteredChars.push(char);
        }
    }

    const m = filteredChars.length;
    const dp = Array.from({ length: m }, () => Array(m).fill(Infinity));
    const nextOccurrence = Array(m).fill(-1);
    
    // Fill the DP table with base cases
    for (let i = 0; i < m; i++) {
        dp[i][i] = 1;
    }

    // Precompute the next occurrence for each character
    const lastSeen = new Map();
    for (let i = m - 1; i >= 0; i--) {
        const char = filteredChars[i];
        if (lastSeen.has(char)) {
            nextOccurrence[i] = lastSeen.get(char);
        }
        lastSeen.set(char, i);
    }

    // Fill the DP table
    for (let length = 2; length <= m; length++) {
        for (let start = 0; start <= m - length; start++) {
            const end = start + length - 1;
            dp[start][end] = dp[start + 1][end] + 1;
            let nextPos = nextOccurrence[start];
            while (nextPos !== -1 && nextPos <= end) {
                dp[start][end] = Math.min(dp[start][end], dp[start][nextPos - 1] + (nextPos + 1 <= end ? dp[nextPos + 1][end] : 0));
                nextPos = nextOccurrence[nextPos];
            }
        }
    }

    return dp[0][m - 1];
};

//https://leetcode.com/problems/strange-printer/submissions/1358704459/
```

---


### Example 1: Input `s = "aaabbb"`

#### Step-by-Step Dry Run:

1. **Initial Setup:**
   - **Filtered Characters:** We first filter the string to remove consecutive duplicates. 
     - For `s = "aaabbb"`, after filtering, we get `filteredChars = ['a', 'b']`.
   - **Length:** The length of `filteredChars` is `m = 2`.
   - **DP Table:** We initialize the DP table `dp[m][m]` where `m = 2`.
     - Initial DP table:
     ```
     dp = [
       [1, ∞],
       [∞, 1]
     ]
     ```
   - **Next Occurrence Array:** We also need to fill the `nextOccurrence` array.
     - For `filteredChars = ['a', 'b']`, we get `nextOccurrence = [-1, -1]` since there are no recurring characters in the filtered list.

2. **Filling DP Table:**

   - **Iteration for Length = 2:**
     - **Subsequence `filteredChars[0:1] = "ab"`**
     - `start = 0`, `end = 1`:
       - We calculate `dp[start][end] = dp[start + 1][end] + 1 = dp[1][1] + 1 = 1 + 1 = 2`.
       - Since there is no recurring character in this subsequence, no further minimization is needed.
       - Updated DP table:
     ```
     dp = [
       [1, 2],
       [∞, 1]
     ]
     ```

3. **Final Output:**
   - The final answer is `dp[0][1] = 2`.

#### Dry Run Table:

| Step         | Filtered Characters (`filteredChars`) | DP Table                                  | Next Occurrence Array (`nextOccurrence`) |
|--------------|---------------------------------------|-------------------------------------------|------------------------------------------|
| Initialization | ['a', 'b']                           | `dp = [[1, ∞], [∞, 1]]`                   | `nextOccurrence = [-1, -1]`              |
| Length 2, Subsequence "ab" | ['a', 'b']              | `dp = [[1, 2], [∞, 1]]`                   | `nextOccurrence = [-1, -1]`              |
| Final Output | ['a', 'b']                           | `dp = [[1, 2], [∞, 1]]`                   | `nextOccurrence = [-1, -1]`              |

- **Output:** 2

---

### Example 2: Input `s = "aba"`

#### Step-by-Step Dry Run:

1. **Initial Setup:**
   - **Filtered Characters:** After filtering, we get `filteredChars = ['a', 'b', 'a']`.
   - **Length:** The length of `filteredChars` is `m = 3`.
   - **DP Table:** We initialize the DP table `dp[m][m]` where `m = 3`.
     - Initial DP table:
     ```
     dp = [
       [1, ∞, ∞],
       [∞, 1, ∞],
       [∞, ∞, 1]
     ]
     ```
   - **Next Occurrence Array:** We fill the `nextOccurrence` array.
     - For `filteredChars = ['a', 'b', 'a']`, we get `nextOccurrence = [2, -1, -1]` (The 'a' at index 0 recurs at index 2).

2. **Filling DP Table:**

   - **Iteration for Length = 2:**
     - **Subsequence `filteredChars[0:1] = "ab"`**
     - `start = 0`, `end = 1`:
       - We calculate `dp[start][end] = dp[start + 1][end] + 1 = dp[1][1] + 1 = 1 + 1 = 2`.
       - No minimization is needed as there's no recurring character in this subsequence.
       - Updated DP table:
     ```
     dp = [
       [1, 2, ∞],
       [∞, 1, ∞],
       [∞, ∞, 1]
     ]
     ```
     - **Subsequence `filteredChars[1:2] = "ba"`**
     - `start = 1`, `end = 2`:
       - We calculate `dp[start][end] = dp[start + 1][end] + 1 = dp[2][2] + 1 = 1 + 1 = 2`.
       - No minimization is needed as there's no recurring character in this subsequence.
       - Updated DP table:
     ```
     dp = [
       [1, 2, ∞],
       [∞, 1, 2],
       [∞, ∞, 1]
     ]
     ```
  
   - **Iteration for Length = 3:**
     - **Subsequence `filteredChars[0:2] = "aba"`**
     - `start = 0`, `end = 2`:
       - We calculate `dp[start][end] = dp[start + 1][end] + 1 = dp[1][2] + 1 = 2 + 1 = 3`.
       - We check for a recurring character and find that 'a' recurs at index 2 (`nextPos = 2`).
       - We calculate `dp[start][end] = min(dp[start][end], dp[start][nextPos - 1] + dp[nextPos + 1][end]) = min(3, dp[0][1] + 1) = min(3, 2 + 0) = 2`.
       - Updated DP table:
     ```
     dp = [
       [1, 2, 2],
       [∞, 1, 2],
       [∞, ∞, 1]
     ]
     ```

3. **Final Output:**
   - The final answer is `dp[0][2] = 2`.

#### Dry Run Table:

| Step         | Filtered Characters (`filteredChars`) | DP Table                                  | Next Occurrence Array (`nextOccurrence`) |
|--------------|---------------------------------------|-------------------------------------------|------------------------------------------|
| Initialization | ['a', 'b', 'a']                     | `dp = [[1, ∞, ∞], [∞, 1, ∞], [∞, ∞, 1]]` | `nextOccurrence = [2, -1, -1]`           |
| Length 2, Subsequence "ab" | ['a', 'b', 'a']        | `dp = [[1, 2, ∞], [∞, 1, ∞], [∞, ∞, 1]]` | `nextOccurrence = [2, -1, -1]`           |
| Length 2, Subsequence "ba" | ['a', 'b', 'a']        | `dp = [[1, 2, ∞], [∞, 1, 2], [∞, ∞, 1]]` | `nextOccurrence = [2, -1, -1]`           |
| Length 3, Subsequence "aba" | ['a', 'b', 'a']       | `dp = [[1, 2, 2], [∞, 1, 2], [∞, ∞, 1]]` | `nextOccurrence = [2, -1, -1]`           |
| Final Output | ['a', 'b', 'a']                      | `dp = [[1, 2, 2], [∞, 1, 2], [∞, ∞, 1]]` | `nextOccurrence = [2, -1, -1]`           |

- **Output:** 2

---

**PS:** (`∞`) in dynamic programming (DP) tables typically represents an uninitialized or unreachable state. It means that no valid solution has been computed yet for that specific subproblem.

In the context of this problem, the `∞` values indicate that we haven't yet computed the minimum number of turns for printing certain subsequences. As we proceed through the algorithm, these `∞` values will be replaced by valid numbers as we calculate the minimum number of turns required to print the corresponding subsequences.

So, `∞` is essentially a placeholder to signify that the value has not been determined at that point in the algorithm.
