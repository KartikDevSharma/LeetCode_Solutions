# Overview of the Problem:
*The problem asks us to find the length of the longest substring without repeating characters in a given string. A substring is a contiguous sequence of characters within a string, while a subsequence can skip characters but maintain order. The key challenge is to identify the longest such substring that doesn't have any character appearing more than once.*

# 1. Brute Force
### Intuition:
The intuition behind the brute force approach is to consider all possible substrings of the given string and check each one for uniqueness of characters. By doing this exhaustively, we can be sure to find the longest substring without repeating characters.

1. We start by considering each character as a potential starting point for our substring.
2. For each starting point, we extend the substring by adding characters one by one.
3. At each step, we check if the current substring has all unique characters.
4. If it does, we update our record of the maximum length found so far.
5. We continue this process for all possible starting points and ending points.

This approach guarantees that we will examine every possible substring, ensuring we don't miss the longest one without repeating characters.

### Approach:
Let's break down the approach step by step:

1. Outer Loop:
   We use an outer loop to iterate through all possible starting positions in the string. This loop variable, `start`, represents the beginning of our current substring under consideration.

2. Inner Loop:
   For each starting position, we have an inner loop that extends the substring by moving the end pointer (`end`) from the starting position to the end of the string.

3. Uniqueness Check:
   For each substring defined by `start` and `end`, we check if it contains all unique characters. This is done by the `hasUniqueCharacters` method.

4. Maximum Length Update:
   If a substring is found to have all unique characters, we calculate its length (`end - start + 1`) and update our `maxLength` if this substring is longer than any we've seen before.

5. Unique Character Checking:
   The `hasUniqueCharacters` method uses a HashSet to keep track of characters we've seen. If we encounter a character already in the set, we know we have a repeat, and the substring is not valid.

6. Result:
   After checking all possible substrings, the `maxLength` variable will contain the length of the longest substring without repeating characters.

Now, let's look at a more detailed pseudo-code representation of this approach:

**Pseudo Code:**

```
function lengthOfLongestSubstring(s):
    maxLength = 0
    n = length of s
    
    for start from 0 to n-1:
        for end from start to n-1:
            if hasUniqueCharacters(s, start, end):
                currentLength = end - start + 1
                maxLength = max(maxLength, currentLength)
    
    return maxLength

function hasUniqueCharacters(s, start, end):
    charSet = empty hash set
    
    for i from start to end:
        if s[i] is in charSet:
            return false
        add s[i] to charSet
    
    return true
```

### Complexity Analysis:

**Time Complexity:**
The time complexity of this solution is O(n^3), where n is the length of the input string. Here's why:

1. The outer loop runs n times (for each starting position).
2. For each starting position, the inner loop can run up to n times (extending to the end of the string).
3. For each substring, we call `hasUniqueCharacters`, which iterates through the substring, taking up to n operations in the worst case.

This gives us n * n * n = n^3 operations in the worst case.

**Space Complexity:**
The space complexity is O(min(m, n)), where n is the length of the string and m is the size of the character set:

1. We use a HashSet in `hasUniqueCharacters` to store the characters we've seen.
2. In the worst case, this set could contain all unique characters in the string.
3. However, it's bounded by the size of the possible character set (e.g., if we're only using lowercase English letters, this would be at most 26).




# Code
Java
```Java []
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        int n = s.length();

        for (int start = 0; start < n; start++) {
            for (int end = start; end < n; end++) {
                if (hasUniqueCharacters(s, start, end)) {
                    maxLength = Math.max(maxLength, end - start + 1);
                }
            }
        }

        return maxLength;
    }

    private boolean hasUniqueCharacters(String s, int start, int end) {
        Set<Character> charSet = new HashSet<>();

        for (int i = start; i <= end; i++) {
            if (charSet.contains(s.charAt(i))) {
                return false;
            }
            charSet.add(s.charAt(i));
        }

        return true;
    }
}
```
C++
```C++ []
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLength = 0;
        int n = s.length();

        for (int start = 0; start < n; start++) {
            for (int end = start; end < n; end++) {
                if (hasUniqueCharacters(s, start, end)) {
                    maxLength = max(maxLength, end - start + 1);
                }
            }
        }

        return maxLength;
    }

private:
    bool hasUniqueCharacters(const string& s, int start, int end) {
        unordered_set<char> charSet;

        for (int i = start; i <= end; i++) {
            if (charSet.count(s[i]) > 0) {
                return false;
            }
            charSet.insert(s[i]);
        }

        return true;
    }
};
```
Python
```Python []
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        n = len(s)

        for start in range(n):
            for end in range(start, n):
                if self.has_unique_characters(s, start, end):
                    max_length = max(max_length, end - start + 1)

        return max_length

    def has_unique_characters(self, s: str, start: int, end: int) -> bool:
        char_set = set()

        for i in range(start, end + 1):
            if s[i] in char_set:
                return False
            char_set.add(s[i])

        return True
```
Go
```Go []
func lengthOfLongestSubstring(s string) int {
    maxLength := 0
    n := len(s)

    for start := 0; start < n; start++ {
        for end := start; end < n; end++ {
            if hasUniqueCharacters(s, start, end) {
                if end-start+1 > maxLength {
                    maxLength = end - start + 1
                }
            }
        }
    }

    return maxLength
}

func hasUniqueCharacters(s string, start, end int) bool {
    charSet := make(map[byte]bool)

    for i := start; i <= end; i++ {
        if charSet[s[i]] {
            return false
        }
        charSet[s[i]] = true
    }

    return true
}

```
Rust
```Rust []
use std::collections::HashSet;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let s_bytes = s.as_bytes();
        let n = s_bytes.len();
        let mut max_length = 0;

        for start in 0..n {
            for end in start..n {
                if Self::has_unique_characters(&s_bytes, start, end) {
                    max_length = max_length.max(end - start + 1);
                }
            }
        }

        max_length as i32
    }

    fn has_unique_characters(s: &[u8], start: usize, end: usize) -> bool {
        let mut char_set = HashSet::new();

        for i in start..=end {
            if !char_set.insert(&s[i]) {
                return false;
            }
        }

        true
    }
}
```
JavaScript
```JavaScript []
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let maxLength = 0;
    const n = s.length;

    for (let start = 0; start < n; start++) {
        for (let end = start; end < n; end++) {
            if (hasUniqueCharacters(s, start, end)) {
                maxLength = Math.max(maxLength, end - start + 1);
            }
        }
    }

    return maxLength;
};

function hasUniqueCharacters(s, start, end) {
    const charSet = new Set();

    for (let i = start; i <= end; i++) {
        if (charSet.has(s[i])) {
            return false;
        }
        charSet.add(s[i]);
    }

    return true;
}
```

---
# 2. Sliding Window Approach

## Intuition

The core intuition behind this approach is to maintain a "window" of characters that are all unique. As we move through the string, we expand this window when we encounter new characters and contract it when we find repeating characters.

Imagine you're reading a book and want to find the longest sequence of words where no word repeats. You might start by placing your left hand at the beginning of a sentence and your right hand a few words ahead. As you move your right hand forward (expanding the window), you keep track of each new word. If you encounter a word you've already seen, you move your left hand forward (contracting the window) until that repeated word is no longer in your current sequence. This process of expanding and contracting continues until you've covered the entire book.

In our case, instead of words, we're dealing with individual characters in a string. The goal is to find the longest sequence of characters where each character appears only once.

## Approach

Let's break down the approach into simple steps:

1. **Initialize a sliding window**: We use two pointers, `windowStart` and `windowEnd`, to define our current window. Initially, both point to the start of the string.

2. **Use a HashMap for efficient lookups**: We use a HashMap to keep track of characters we've seen and their most recent positions. This allows us to quickly check if a character is already in our current window.

3. **Expand the window**: We move the `windowEnd` pointer forward, adding each new character to our HashMap.

4. **Handle repeating characters**: If we encounter a character that's already in our HashMap (i.e., it's repeating), we need to update our `windowStart`. We move it to the position just after the previous occurrence of the repeating character.

5. **Update the maximum length**: After each step, we calculate the length of our current window and update our `maxLength` if necessary.

6. **Repeat**: We continue this process until we've processed all characters in the string.

This approach allows us to efficiently find the longest substring without repeating characters in a single pass through the string.

**Pseudo Code**


```
function lengthOfLongestSubstring(s):
    Initialize an empty HashMap charMap
    Set maxLength to 0
    Set windowStart to 0

    For windowEnd from 0 to length of s - 1:
        Get the current character at windowEnd

        If the current character is already in charMap:
            Update windowStart to max(windowStart, previous position of current character + 1)

        Update the position of the current character in charMap

        Calculate current window length (windowEnd - windowStart + 1)
        Update maxLength if current window length is greater

    Return maxLength
```

This pseudo code outlines the main steps of our algorithm. It shows how we iterate through the string, handle repeating characters, and keep track of the maximum length.

### Dry Run

Let's do a dry run of the algorithm with the input string "abcabcbb". We'll use a table to show the state of our variables at each step.

| Step | windowEnd | Current Char | charMap | windowStart | maxLength | Explanation |
|------|-----------|--------------|---------|-------------|-----------|-------------|
| 0 | 0 | 'a' | {} | 0 | 0 | Initial state |
| 1 | 0 | 'a' | {a:0} | 0 | 1 | Add 'a' to charMap, update maxLength |
| 2 | 1 | 'b' | {a:0, b:1} | 0 | 2 | Add 'b' to charMap, update maxLength |
| 3 | 2 | 'c' | {a:0, b:1, c:2} | 0 | 3 | Add 'c' to charMap, update maxLength |
| 4 | 3 | 'a' | {a:3, b:1, c:2} | 1 | 3 | 'a' repeats, move windowStart to 1 |
| 5 | 4 | 'b' | {a:3, b:4, c:2} | 2 | 3 | 'b' repeats, move windowStart to 2 |
| 6 | 5 | 'c' | {a:3, b:4, c:5} | 3 | 3 | 'c' repeats, move windowStart to 3 |
| 7 | 6 | 'b' | {a:3, b:6, c:5} | 4 | 3 | 'b' repeats, move windowStart to 4 |
| 8 | 7 | 'b' | {a:3, b:7, c:5} | 7 | 3 | 'b' repeats, move windowStart to 7 |

Final result: The longest substring without repeating characters has a length of 3.

Let's break down each step:

1. We start with an empty `charMap`, `windowStart` at 0, and `maxLength` at 0.

2. We encounter 'a'. It's not in `charMap`, so we add it. Our current window is "a", length 1.

3. We encounter 'b'. It's not in `charMap`, so we add it. Our current window is "ab", length 2.

4. We encounter 'c'. It's not in `charMap`, so we add it. Our current window is "abc", length 3.

5. We encounter 'a' again. It's in `charMap` at position 0. We move `windowStart` to 1 (max(0, 0+1)). Our current window is "bca".

6. We encounter 'b' again. It's in `charMap` at position 1. We move `windowStart` to 2 (max(1, 1+1)). Our current window is "cab".

7. We encounter 'c' again. It's in `charMap` at position 2. We move `windowStart` to 3 (max(2, 2+1)). Our current window is "abc".

8. We encounter 'b' again. It's in `charMap` at position 4. We move `windowStart` to 5 (max(3, 4+1)). Our current window is "b".

9. We encounter the last 'b'. It's in `charMap` at position 6. We move `windowStart` to 7 (max(5, 6+1)). Our current window is "b".

Throughout this process, the maximum length we found was 3, corresponding to the substrings "abc" or "cab".

## Complexity Analysis

### Time Complexity: O(n)

- We iterate through the string exactly once, where n is the length of the string.
- For each character, we perform constant time operations:
  - Checking if the character is in the HashMap: O(1) on average
  - Updating the HashMap: O(1) on average
  - Updating `windowStart` and `maxLength`: O(1)
- Therefore, the overall time complexity is O(n), where n is the length of the input string.

### Space Complexity: O(min(m, n))

- We use a HashMap to store characters and their indices.
- In the worst case, the HashMap could store all characters in the string if they are all unique.
- However, the size of the HashMap is bounded by the size of the character set (let's call it m) and the length of the string (n).
- Therefore, the space complexity is O(min(m, n)).
  - For example, if we're dealing with ASCII characters, m would be 128.
  - If we're dealing with extended ASCII, m would be 256.
  - For Unicode characters, m could be much larger, but still constant.


### Code
Java
```Java []
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> charMap = new HashMap<>();
        int maxLength = 0;
        int windowStart = 0;

        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            char currentChar = s.charAt(windowEnd);

            if (charMap.containsKey(currentChar)) {
                windowStart = Math.max(windowStart, charMap.get(currentChar) + 1);
            }

            charMap.put(currentChar, windowEnd);
            maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
        }

        return maxLength;
    }
}
```
C++
```C++ []
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> charMap;
        int maxLength = 0;
        int windowStart = 0;

        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            char currentChar = s[windowEnd];

            if (charMap.find(currentChar) != charMap.end()) {
                windowStart = max(windowStart, charMap[currentChar] + 1);
            }

            charMap[currentChar] = windowEnd;
            maxLength = max(maxLength, windowEnd - windowStart + 1);
        }

        return maxLength;
    }
};
```
Python
```Python []
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        window_start = 0

        for window_end in range(len(s)):
            current_char = s[window_end]

            if current_char in char_map:
                window_start = max(window_start, char_map[current_char] + 1)

            char_map[current_char] = window_end
            max_length = max(max_length, window_end - window_start + 1)

        return max_length
```
Go
```Go []
func lengthOfLongestSubstring(s string) int {
    charMap := make(map[byte]int)
    maxLength := 0
    windowStart := 0

    for windowEnd := 0; windowEnd < len(s); windowEnd++ {
        currentChar := s[windowEnd]

        if index, found := charMap[currentChar]; found {
            if index + 1 > windowStart {
                windowStart = index + 1
            }
        }

        charMap[currentChar] = windowEnd
        if windowEnd - windowStart + 1 > maxLength {
            maxLength = windowEnd - windowStart + 1
        }
    }

    return maxLength
}

```
Rust
```Rust []
use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut char_map = HashMap::new();
        let mut max_length = 0;
        let mut window_start = 0;

        for (window_end, current_char) in s.chars().enumerate() {
            if let Some(&index) = char_map.get(&current_char) {
                window_start = window_start.max(index + 1);
            }

            char_map.insert(current_char, window_end);
            max_length = max_length.max(window_end - window_start + 1);
        }

        max_length as i32
    }
}
```
JavaScript
```JavaScript []
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const charMap = new Map();
    let maxLength = 0;
    let windowStart = 0;

    for (let windowEnd = 0; windowEnd < s.length; windowEnd++) {
        const currentChar = s[windowEnd];

        if (charMap.has(currentChar)) {
            windowStart = Math.max(windowStart, charMap.get(currentChar) + 1);
        }

        charMap.set(currentChar, windowEnd);
        maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
    }

    return maxLength;
};
```
### Why is this efficient?

1. **Single Pass**: We only need to go through the string once, which is optimal for this problem.

2. **Constant Time Lookups**: By using a HashMap, we can check for repeating characters and update our window in constant time.

3. **Space Efficient**: We only store each character once in our HashMap, keeping our space usage minimal.

4. **Adapts to Input**: The algorithm naturally adapts to the complexity of the input. For strings with few repeating characters, it will tend towards O(n) space usage. For strings with many repeats, it will use less space.

---


# 3. Optimized Sliding Window Approach

## Comparison

Let's briefly recap the two approaches we've discussed earlier:

1. **Brute Force Approach**: This method involves checking all possible substrings of the given string. While straightforward, it's inefficient with a time complexity of O(n^3) for a string of length n.

2. **Basic Sliding Window Approach**: This improves upon the brute force method by maintaining a window of unique characters and expanding/contracting it as needed. It typically uses a HashSet to track unique characters and has a time complexity of O(n).



## Intuition

The optimized sliding window approach builds upon the basic sliding window method but introduces a key optimization: instead of using a HashSet, it uses an integer array to keep track of character positions. This change allows for even faster lookups and more efficient window adjustments.

The core intuition remains similar to the basic sliding window approach:
- We maintain a window of unique characters.
- We expand this window when we encounter new characters.
- We contract it when we find repeating characters.

However, the way we handle repeating characters and adjust our window is more efficient in this optimized version.

## Approach

Let's understand the approach step by step:

1. **Character Index Array**:
   Instead of using a HashSet or HashMap, we use an integer array `charIndex` of size 128 (assuming ASCII characters). Each index in this array corresponds to a character's ASCII value, and the value stored is the last seen position of that character in the string.

   ```java
   int[] charIndex = new int[128];
   Arrays.fill(charIndex, -1);
   ```

   This array serves two purposes:
   - It tells us if we've seen a character before (if its value is not -1).
   - It gives us the last position where we saw that character.

2. **Sliding Window Pointers**:
   We use two pointers:
   - `windowStart`: The start of our current substring without repeating characters.
   - `windowEnd`: The end of our current substring, which we'll iterate through the string.

3. **Iteration and Window Adjustment**:
   As we move `windowEnd` through the string:
   
   ```java
   for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
       char currentChar = s.charAt(windowEnd);
   ```

   We check if we've seen the current character before and if it's within our current window:

   ```java
   if (charIndex[currentChar] >= windowStart) {
       windowStart = charIndex[currentChar] + 1;
   }
   ```

   If the character is repeating within the current window, we move `windowStart` to just after the last occurrence of this character. This is more efficient than the basic sliding window approach, where we might need to move the start pointer multiple times to remove all occurrences of the repeating character.

4. **Updating Character Positions**:
   We always update the last seen position of the current character:

   ```java
   charIndex[currentChar] = windowEnd;
   ```

5. **Updating Maximum Length**:
   After each iteration, we update our `maxLength` if the current window size is larger:

   ```java
   maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
   ```
### Pseudo-code


```
function lengthOfLongestSubstring(s):
    Initialize charIndex array of size 128 with all values set to -1
    Set maxLength to 0
    Set windowStart to 0

    For windowEnd from 0 to length of s - 1:
        Get currentChar at index windowEnd in s
        
        If charIndex[currentChar] is greater than or equal to windowStart:
            Update windowStart to charIndex[currentChar] + 1
        
        Update charIndex[currentChar] to windowEnd
        Update maxLength to maximum of maxLength and (windowEnd - windowStart + 1)

    Return maxLength
```

### Dry Run
To truly understand how this algorithm works, let's do a dry run with an example string: **"abcabcbb"**



| Step | windowEnd | currentChar | charIndex[currentChar] | windowStart | maxLength | charIndex Array (relevant parts)                |
|------|-----------|-------------|------------------------|-------------|-----------|--------------------------------------------------|
| 0    | 0         | 'a'         | -1                     | 0           | 1         | a:0                                              |
| 1    | 1         | 'b'         | -1                     | 0           | 2         | a:0, b:1                                         |
| 2    | 2         | 'c'         | -1                     | 0           | 3         | a:0, b:1, c:2                                    |
| 3    | 3         | 'a'         | 0                      | 1           | 3         | a:3, b:1, c:2                                    |
| 4    | 4         | 'b'         | 1                      | 2           | 3         | a:3, b:4, c:2                                    |
| 5    | 5         | 'c'         | 2                      | 3           | 3         | a:3, b:4, c:5                                    |
| 6    | 6         | 'b'         | 4                      | 5           | 3         | a:3, b:6, c:5                                    |
| 7    | 7         | 'b'         | 6                      | 7           | 3         | a:3, b:7, c:5                                    |

Let's go through each step:

1. We start with 'a'. It's not seen before, so we add it to charIndex and set maxLength to 1.
2. We see 'b'. It's new, so we extend our window and update maxLength to 2.
3. We see 'c'. It's new, so we extend our window and update maxLength to 3.
4. We see 'a' again. It was last seen at index 0, which is within our current window (0 to 3). So we move windowStart to 1 (0 + 1) and update 'a' in charIndex.
5. We see 'b' again. It was last seen at index 1, which is within our current window (1 to 4). So we move windowStart to 2 and update 'b' in charIndex.
6. We see 'c' again. It was last seen at index 2, which is within our current window (2 to 5). So we move windowStart to 3 and update 'c' in charIndex.
7. We see 'b' again. It was last seen at index 4, which is within our current window (3 to 6). So we move windowStart to 5 and update 'b' in charIndex.
8. We see 'b' again. It was last seen at index 6, which is within our current window (5 to 7). So we move windowStart to 7 and update 'b' in charIndex.

Throughout this process, maxLength remains 3, which is our final answer.

### Improvements Over Previous Approaches

1. **Compared to Brute Force**:
   - Time Complexity: O(n) vs O(n^3)
   - We avoid generating and checking all possible substrings.
   - We only need to iterate through the string once.

2. **Compared to Basic Sliding Window**:
   - More efficient space usage: We use a fixed-size array instead of a potentially large HashSet or HashMap.
   - Faster lookups: Checking if a character exists and getting its last position is O(1) with direct array access, compared to HashSet/HashMap operations which, while typically O(1), have some overhead.
   - More efficient window adjustment: We can jump the `windowStart` directly to the correct position instead of potentially making multiple adjustments.

## Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the string.
  We only iterate through the string once with the `windowEnd` pointer. All operations inside the loop (checking and updating `charIndex`, updating `maxLength`) are O(1).

- **Space Complexity**: O(1)
  We use a fixed-size array `charIndex` of size 128, which is constant regardless of the input size. This is an improvement over the basic sliding window approach, which might use O(min(m,n)) space for its HashSet/HashMap, where m is the size of the character set.






### Code
Java
```Java []
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] charIndex = new int[128];
        Arrays.fill(charIndex, -1);
        int maxLength = 0;
        int windowStart = 0;

        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            char currentChar = s.charAt(windowEnd);
            
            if (charIndex[currentChar] >= windowStart) {
                windowStart = charIndex[currentChar] + 1;
            }

            charIndex[currentChar] = windowEnd;
            maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
        }

        return maxLength;
    }
}
```
C++
```C++ []
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> charIndex(128, -1);
        int maxLength = 0;
        int windowStart = 0;

        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            char currentChar = s[windowEnd];
            
            if (charIndex[currentChar] >= windowStart) {
                windowStart = charIndex[currentChar] + 1;
            }

            charIndex[currentChar] = windowEnd;
            maxLength = max(maxLength, windowEnd - windowStart + 1);
        }

        return maxLength;
    }
};
```
Python
```Python []
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = [-1] * 128
        max_length = 0
        window_start = 0

        for window_end, current_char in enumerate(s):
            if char_index[ord(current_char)] >= window_start:
                window_start = char_index[ord(current_char)] + 1

            char_index[ord(current_char)] = window_end
            max_length = max(max_length, window_end - window_start + 1)

        return max_length
```
Go
```Go []
func lengthOfLongestSubstring(s string) int {
    charIndex := make([]int, 128)
    for i := range charIndex {
        charIndex[i] = -1
    }
    maxLength := 0
    windowStart := 0

    for windowEnd := 0; windowEnd < len(s); windowEnd++ {
        currentChar := s[windowEnd]
        
        if charIndex[currentChar] >= windowStart {
            windowStart = charIndex[currentChar] + 1
        }

        charIndex[currentChar] = windowEnd
        if windowEnd - windowStart + 1 > maxLength {
            maxLength = windowEnd - windowStart + 1
        }
    }

    return maxLength
}

```
Rust
```Rust []
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut char_index = [-1; 128];
        let mut max_length = 0;
        let mut window_start = 0;

        for (window_end, current_char) in s.bytes().enumerate() {
            let char_idx = current_char as usize;
            
            if char_index[char_idx] >= window_start {
                window_start = char_index[char_idx] + 1;
            }

            char_index[char_idx] = window_end as i32;
            max_length = max_length.max(window_end as i32 - window_start + 1);
        }

        max_length
    }
}
```
JavaScript
```JavaScript []
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const charIndex = new Array(128).fill(-1);
    let maxLength = 0;
    let windowStart = 0;

    for (let windowEnd = 0; windowEnd < s.length; windowEnd++) {
        const currentChar = s.charCodeAt(windowEnd);
        
        if (charIndex[currentChar] >= windowStart) {
            windowStart = charIndex[currentChar] + 1;
        }

        charIndex[currentChar] = windowEnd;
        maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
    }

    return maxLength;
};
```
## Key Insights

1. **Efficient Character Tracking**: 
   By using an array indexed by ASCII values, we achieve O(1) lookups and updates for character positions. This is faster than using a HashSet or HashMap in practice.

2. **Smart Window Adjustment**: 
   When we encounter a repeating character, we can move the `windowStart` directly to the correct position, potentially skipping multiple adjustments that might be necessary in the basic sliding window approach.

3. **Constant Space**: 
   The use of a fixed-size array means our space complexity is O(1), which is optimal for this problem.

4. **Single Pass**: 
   Like the basic sliding window approach, this method only requires a single pass through the string, making it efficient for large inputs.

5. **No Substring Storage**: 
   We only keep track of the length of the longest substring, not the substring itself, which saves memory.

---
