# Intuition
This problem is pretty wild when you first look at it. The printer can only spit out the same character over and over, but it can go back and overwrite stuff it's already printed. Our job is to figure out how to use this printer to make any given string with the fewest number of "turns" possible.

Now, when we say "turns," we're not talking about each individual keystroke. A turn is basically every time we switch to printing a different character. This is key, because it means we can print a group of the same letter in one go, and that counts as just one turn.

Say we want to print "aba". You might think, that's easy. Three turns - print 'a', then 'b', then 'a' again." But, we can do better we can print "aaa" in one turn, and then go back and print a "b" in the middle, see just two turns instead of three.

Now For longer strings, it's not always obvious what the best strategy is. Should we print a bunch of one letter and then go back and fill in the others? Or is it better to do it in chunks? It's like a puzzle where you have to think several steps ahead.

Now, when we see a problem asking for the "minimum" number of something, it often points to using dynamic programming. Why? Because we're dealing with an optimization problem that has optimal substructure (the best solution for the whole string depends on the best solutions for parts of the string) and overlapping subproblems (we might need to calculate the same thing multiple times for different parts of the string).In this case, we'd be looking at how to optimally print smaller parts of the string, and then use that info to figure out the best way for the whole string.

It's not so easy for sure. Even once you get what the problem's asking, coming up with a solution isn't straightforward. You've got to think about how to represent the state of the string at each step, how to make decisions about when to overwrite versus when to start fresh, and how to keep track of all the possibilities without getting bogged down.

If you're new to dynamic programming, don't sweat it if this doesn't click right away, happens to all us. It's a tough concept that takes practice. The key is to start by really understanding the problem, then think about how you can break it down into smaller, similar problems. From there, it's about finding patterns and building up your solution step by step.
Now I hope you understand the problem statement so I was thinking about how to minimize the number of turns needed to print a given string. The properties of the printer is being able to print sequences of the same character and overwrite existing characters - as mentioned before this made me realize that this wasn't a straightforward printing process.
The first idea I had was to simplify the input string by removing consecutive duplicate characters. This doesn't change the minimum number of turns needed, but it significantly reduces the problem size, which can lead to significant performance improvements, identifying opportunities where we could save turns by printing characters that appear later in the string simultaneously with earlier occurrences. This led me to the idea of a dynamic programming (DP) approach, where I could build up the solution by solving smaller subproblems.

The important thing here is that if the first and last characters of a substring match, I can print them together in a single turn, saving one turn. This means a DP solution where I would need to quickly identify these potential matching characters.

To further optimize the DP process, I thought about precomputing the next occurrence of each character in the string. This would allow me to jump directly to potential matches without having to scan the entire string repeatedly, streamlining the DP algorithm and avoiding redundant computations.

So, byy removing consecutive duplicates, identifying matching characters, and using precomputed next occurrences, I believed I could develop an efficient dynamic programming solution to this problem.



# Approach

Let's break down the approach step by step:

1. **Preprocessing the Input**
   Removing consecutive duplicate characters:

   ```
   function removeConsecutiveDuplicates(s):
       result = empty list
       for each character c in s:
           if result is empty or c != last element in result:
               add c to result
       return result
   ```

   Consecutive identical characters can always be printed in a single turn, so they don't affect our minimum turn count. It also potentially reduces the size of our problem, making subsequent steps more efficient.

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

   This precomputation allows us to jump to the next matching character without searching through the entire string each time we need to find a match.

4. **Filling the DP Table**
    We fill the DP table in a bottom-up manner:

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

This DP approach allows us to quickly find matching characters. By precomputing the next occurrences, we avoid unnecessary iterations and comparisons.



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
Java
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



```
C++
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





```
Python
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






```
C#
```C# []
public class Solution {
    public int StrangePrinter(string s) {
        if (string.IsNullOrEmpty(s)) return 0;
        
        // Remove consecutive duplicates
        var filteredChars = new List<char>();
        foreach (var c in s) {
            if (filteredChars.Count == 0 || c != filteredChars[filteredChars.Count - 1]) {
                filteredChars.Add(c);
            }
        }
        
        int m = filteredChars.Count;
        var dp = new int[m, m];
        for (int i = 0; i < m; ++i) {
            dp[i, i] = 1;
        }
        
        // Precompute the next occurrence for each character
        var lastSeen = new Dictionary<char, int>();
        var nextOccurrence = new int[m];
        Array.Fill(nextOccurrence, -1);
        for (int i = m - 1; i >= 0; --i) {
            char c = filteredChars[i];
            if (lastSeen.ContainsKey(c)) {
                nextOccurrence[i] = lastSeen[c];
            }
            lastSeen[c] = i;
        }
        
        // Fill the DP table
        for (int length = 2; length <= m; ++length) {
            for (int start = 0; start <= m - length; ++start) {
                int end = start + length - 1;
                // Initial case: print each character separately
                dp[start, end] = dp[start + 1, end] + 1;
                // Try to find a better solution by matching characters
                char currentChar = filteredChars[start];
                int nextPos = nextOccurrence[start];
                while (nextPos != -1 && nextPos <= end) {
                    dp[start, end] = Math.Min(dp[start, end], dp[start, nextPos - 1] + (nextPos + 1 <= end ? dp[nextPos + 1, end] : 0));
                    nextPos = nextOccurrence[nextPos];
                }
            }
        }
        
        return dp[0, m - 1];
    }
}


```
Kotlin
```Kotlin []
class Solution {
    fun strangePrinter(s: String): Int {
        if (s.isEmpty()) return 0
        
        // Remove consecutive duplicates
        val filteredChars = mutableListOf<Char>()
        for (c in s) {
            if (filteredChars.isEmpty() || c != filteredChars.last()) {
                filteredChars.add(c)
            }
        }
        
        val m = filteredChars.size
        val dp = Array(m) { IntArray(m) }
        for (i in 0 until m) {
            dp[i][i] = 1
        }
        
        // Precompute the next occurrence for each character
        val lastSeen = mutableMapOf<Char, Int>()
        val nextOccurrence = IntArray(m) { -1 }
        for (i in m - 1 downTo 0) {
            val c = filteredChars[i]
            nextOccurrence[i] = lastSeen[c] ?: -1
            lastSeen[c] = i
        }
        
        // Fill the DP table
        for (length in 2..m) {
            for (start in 0..m - length) {
                val end = start + length - 1
                // Initial case: print each character separately
                dp[start][end] = dp[start + 1][end] + 1
                // Try to find a better solution by matching characters
                val currentChar = filteredChars[start]
                var nextPos = nextOccurrence[start]
                while (nextPos != -1 && nextPos <= end) {
                    dp[start][end] = minOf(dp[start][end], dp[start][nextPos - 1] + if (nextPos + 1 <= end) dp[nextPos + 1][end] else 0)
                    nextPos = nextOccurrence[nextPos]
                }
            }
        }
        
        return dp[0][m - 1]
    }
}


```
Go
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



```
Rust
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



```
JavaScript
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


```
```TypeScript []
function strangePrinter(s: string): number {
    if (!s) return 0;

    // Remove consecutive duplicates
    const filteredChars: string[] = [];
    for (const c of s) {
        if (filteredChars.length === 0 || c !== filteredChars[filteredChars.length - 1]) {
            filteredChars.push(c);
        }
    }

    const m = filteredChars.length;
    const dp: number[][] = Array.from({ length: m }, () => Array(m).fill(Infinity));
    for (let i = 0; i < m; ++i) {
        dp[i][i] = 1;
    }

    // Precompute the next occurrence for each character
    const lastSeen: Map<string, number> = new Map();
    const nextOccurrence: number[] = Array(m).fill(-1);
    for (let i = m - 1; i >= 0; --i) {
        const c = filteredChars[i];
        nextOccurrence[i] = lastSeen.get(c) ?? -1;
        lastSeen.set(c, i);
    }

    // Fill the DP table
    for (let length = 2; length <= m; ++length) {
        for (let start = 0; start <= m - length; ++start) {
            const end = start + length - 1;
            // Initial case: print each character separately
            dp[start][end] = dp[start + 1][end] + 1;
            // Try to find a better solution by matching characters
            const currentChar = filteredChars[start];
            let nextPos = nextOccurrence[start];
            while (nextPos !== -1 && nextPos <= end) {
                dp[start][end] = Math.min(dp[start][end], dp[start][nextPos - 1] + (nextPos + 1 <= end ? dp[nextPos + 1][end] : 0));
                nextPos = nextOccurrence[nextPos];
            }
        }
    }

    return dp[0][m - 1];
}


```

---




---

