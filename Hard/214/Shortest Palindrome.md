
### Intuition
 The goal here is to transform the string `s` into a **palindrome** by adding the fewest characters possible to the **front** of the string. It’s worth mentioning that we’re only allowed to add characters at the front—not at the end or in the middle. That’s important because it shapes our entire approach. So, first, what’s a palindrome? It’s a word or phrase that reads the same forwards and backwards, like "madam" or "racecar." In this problem, the string `s` might not be a palindrome right away, but we can make it one by adding characters. For example, if we have "abcd", it’s not a palindrome yet, but by adding "dcb" in front of it, we get "dcbabcd" which is a palindrome. Why is this challenging? The tricky part is finding the **smallest** number of characters we need to add. You can’t just brute-force it by trying all possible combinations and checking whether they form a palindrome. Given that the input string can be up to 50,000 characters long, we need an efficient way to solve this.



My first instinct is this: The easiest case is when the string is already a palindrome. If the string is already symmetrical, we don't need to add anything. So if we can somehow check if the string is a palindrome, that would give us a big hint. But what if it’s not? How do we figure out which part of the string needs extra characters?

Imagine you have the string "abcd". We want to make it a palindrome. What would we add to the front of this string? One way to think about it is to **reverse** the string and check for symmetry. For "abcd", reversing it gives "dcba". Now, the question becomes: how much of this reverse string do we need to add to the front of the original string to make it a palindrome?

Let’s break this down:
- If we add "dcb" to the front of "abcd", we get "dcbabcd", which is a palindrome. But notice that we didn’t just add the entire reversed string to the front. We only added part of it—the part that **wasn’t already a matching prefix**.

This starts to give us an idea of how we might approach the problem. What if we could identify the **longest prefix of the string that is a palindrome**? Once we have that, the rest of the string can be flipped and added to the front to make the whole thing symmetrical.

### Finding the Longest Palindromic Prefix

Okay, so we’ve realized that finding the longest palindromic prefix is key. But how do we actually do that? One approach would be to start from the beginning of the string and gradually increase the size of the substring we’re checking, seeing if it’s a palindrome. Once we’ve found the largest palindromic prefix, the rest of the string can be reversed and added to the front.

That’s the **brute-force** idea. But here’s the catch: Checking every possible prefix to see if it’s a palindrome could take a lot of time. For longer strings, we'd be doing a ton of palindrome checks, and each check would involve comparing the whole string. That's going to get slow real fast, especially with the constraint that our input string could be up to 50,000 characters long! For each prefix, you’d need to go over each character and check if it matches its counterpart from the other side. With longer strings, this could become inefficient really fast. 

Now, let’s think for a moment. Do we really need to start from scratch every time we check a new prefix? There’s probably a smarter way to do this that avoids repeating work.

### Observing a Pattern

What if we started by comparing the first character with the last character? If they match, we continue inwards. If they don’t, we know that the current prefix isn’t a palindrome, and we need to try again with a shorter prefix. This is basically what you might intuitively do if you were checking a string by hand.

Let’s take a string like "aacecaaa". It looks almost like a palindrome, except there’s one small issue—the last few characters aren’t in the right position. But if we notice that the prefix "aacecaa" (ignoring the last ‘a’) is already a palindrome, then the remaining "a" at the end can just be added to the front. This gives us the palindrome "aaacecaaa".

This tells us that finding the longest palindromic prefix can really simplify the problem. Once we have that, we only need to add a few characters in front to make the whole string symmetrical.

### Making It Efficient: Hashing

So far, we’ve been thinking in terms of checking each prefix manually, but that feels a bit slow. There’s got to be a faster way to compare the string and see if it’s a palindrome. This is where **hashing** comes into play.

Hashing is a technique where we take a string and convert it into a number. The key idea is that if two strings are equal, their hashes will also be equal. By using hashes, we can check for equality between substrings much more efficiently.

Let’s say we’re building two hashes as we go through the string: 
1. One hash for the string from left to right.
2. Another hash for the reverse of the string.

If these two hashes are the same at any point, then we know the substring is a palindrome. This is because the hashes will only match if the characters in the substring are symmetric.

But how do we compute these hashes efficiently? We can use something called **rolling hashes**, which is a clever way to update the hash as we move through the string, without having to recompute it from scratch every time. It's like a way to quickly compare strings without actually comparing each character. Instead, we convert the string into a number using some clever math. We treat the string like a number in a certain base (in this case, 26 for the letters of the alphabet), and we keep updating the hash by adding the value of the next character.

The idea is that we can update this hash value really quickly as we move through the string. It's kind of like how you might calculate an average. If you know the average of 5 numbers and you want to add a 6th, you don't recalculate the whole thing, right? You just do a quick adjustment. Rolling hash works in a similar way, but for strings.

So, what if we used this rolling hash idea to compare the start of our string with its reverse? We could calculate two hashes: one going forward from the start of the string, and one going backward from the end. When these hashes match, we might have found our palindrome!

But here's where we need to be careful. Hash collisions can happen, where two different strings end up with the same hash value. It's rare, but it can happen. So we might need a way to double-check our matches.

Now, let's think about how we'd implement this. We'd need two hash values, right? One for the forward string and one for the reverse. And we'd need to update these as we move through the string.

For the forward hash, we can use a simple formula like this: For each character, multiply the current hash by some base number (let's say 26 for lowercase English letters), add the value of the current character, and take the modulus with a large prime number to keep our hash value from getting too big.

The reverse hash is a bit trickier. We need to weight each character by its position in the string. So we multiply each character value by a power of our base number before adding it to the hash.

As we go through the string, we're constantly updating these hash values and checking if they match. When they do, we've potentially found our longest palindrome substring starting from the beginning.

But here's a key insight: we don't actually need to store all these intermediate palindromes. We just need to keep track of the longest one we've found so far. That's going to save us a lot of memory!

Now, you might be wondering about the time complexity of this approach. We're going through the string once, doing constant-time operations at each step. That's linear time, O(n), which is a huge improvement over our initial brute force idea!

But what about space complexity? We're just using a few variables to keep track of our hashes and the length of our longest palindrome. That's constant space, O(1). Pretty neat, right?

There's one more thing we need to consider though. Remember those hash collisions I mentioned earlier? In practice, they're rare enough that we can often ignore them for problems like this. But if we wanted to be absolutely certain, we could do a final check on our longest palindrome substring before returning our answer.

So, to wrap this all up, what have we done here? We've taken a problem that initially seemed like it might require a lot of string comparisons, and we've turned it into a smooth, single-pass algorithm using some clever math. We're essentially "rolling" through the string, comparing the start to the reverse of the end at each step, all without actually doing explicit character comparisons.

For example, if we have the string "abc", its hash in base 26 would be something like:
```
hash = (a * 26^2 + b * 26^1 + c * 26^0) % MOD
```
where `MOD` is a large prime number that keeps the hash manageable and avoids overflow.

Now, at each step, we can compare the hash of the prefix with the hash of the reversed suffix. If they’re equal, we’ve found a palindrome.



Here’s how we tie everything together:

1. We initialize two hashes: one for the string as we read it from left to right, and one for the reverse.
2. As we move through the string, we update both hashes. Every time the two hashes match, we check if the current prefix is a palindrome.
3. Once we’ve found the longest palindromic prefix, we take the rest of the string, reverse it, and add it to the front.

By using this rolling hash technique, we can find the longest palindromic prefix efficiently in linear time. This avoids the need for a brute-force check of every possible prefix.

### Handling Edge Cases

What about edge cases? Well, if the string is already a palindrome, the algorithm will naturally detect this because the hashes will match for the entire string. If the string is empty or only has one character, there’s nothing to add, so we can just return the string as is.

Another edge case might be if there are no matching characters at all, like in the string "abcd". In that case, the longest palindromic prefix is just the first character "a", and we would need to reverse the entire remaining string ("bcd") and add it to the front.

### Why This Works

What makes this approach powerful is that we’re not wasting time checking each possible prefix manually. Instead, by leveraging hashing, we can compare the entire prefix and suffix in constant time. This means that even for large strings, the algorithm will run efficiently in linear time, O(n), where n is the length of the string.

So, to sum up the thought process: We first recognized that the key to solving the problem lies in finding the longest palindromic prefix. Then, we refined our approach from a brute-force search to a more efficient method using rolling hashes. By the end, we were able to reduce the problem to a simple comparison of two hashes, allowing us to find the shortest palindrome in optimal time.




### Code

```Java []
class Solution {
    private static final long MOD = 1000000007;
    private static final long BASE = 26;

    public String shortestPalindrome(String s) {
        if (s == null || s.length() <= 1) {
            return s;
        }

        long hash = 0;
        long reverseHash = 0;
        long power = 1;
        int len = 0;

        for (int i = 0; i < s.length(); i++) {
            hash = (hash * BASE + (s.charAt(i) - 'a' + 1)) % MOD;
            reverseHash = (reverseHash + (s.charAt(i) - 'a' + 1) * power) % MOD;
            power = (power * BASE) % MOD;

            if (hash == reverseHash) {
                len = i + 1;
            }
        }

        return new StringBuilder(s.substring(len)).reverse().toString() + s;
    }
}
//KDS

```

```C++ []
class Solution {
public:
    string shortestPalindrome(string s) {
        if (s.empty() || s.length() <= 1) {
            return s;
        }

        const long long MOD = 1000000007;
        const long long BASE = 26;

        long long hash = 0;
        long long reverseHash = 0;
        long long power = 1;
        int len = 0;

        for (int i = 0; i < s.length(); i++) {
            hash = (hash * BASE + (s[i] - 'a' + 1)) % MOD;
            reverseHash = (reverseHash + (s[i] - 'a' + 1) * power) % MOD;
            power = (power * BASE) % MOD;

            if (hash == reverseHash) {
                len = i + 1;
            }
        }

        return string(s.rbegin(), s.rbegin() + s.length() - len) + s;
    }
};
//KDS

```

```Python []
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) <= 1:
            return s

        MOD = 1000000007
        BASE = 26

        hash_val = 0
        reverse_hash = 0
        power = 1
        length = 0

        for i, char in enumerate(s):
            hash_val = (hash_val * BASE + ord(char) - ord('a') + 1) % MOD
            reverse_hash = (reverse_hash + (ord(char) - ord('a') + 1) * power) % MOD
            power = (power * BASE) % MOD

            if hash_val == reverse_hash:
                length = i + 1

        return s[length:][::-1] + s


#KDS

```

```Go []
func shortestPalindrome(s string) string {
    if len(s) <= 1 {
        return s
    }

    const MOD int64 = 1000000007
    const BASE int64 = 26

    var hash, reverseHash, power int64 = 0, 0, 1
    var length int = 0

    for i := 0; i < len(s); i++ {
        hash = (hash*BASE + int64(s[i]-'a'+1)) % MOD
        reverseHash = (reverseHash + int64(s[i]-'a'+1)*power) % MOD
        power = (power * BASE) % MOD

        if hash == reverseHash {
            length = i + 1
        }
    }

    return reverse(s[length:]) + s
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
//KDS

```

```Rust []
impl Solution {
    pub fn shortest_palindrome(s: String) -> String {
        if s.len() <= 1 {
            return s;
        }

        const MOD: i64 = 1_000_000_007;
        const BASE: i64 = 26;

        let mut hash: i64 = 0;
        let mut reverse_hash: i64 = 0;
        let mut power: i64 = 1;
        let mut length: usize = 0;

        for (i, c) in s.chars().enumerate() {
            hash = (hash * BASE + (c as i64 - 'a' as i64 + 1)) % MOD;
            reverse_hash = (reverse_hash + (c as i64 - 'a' as i64 + 1) * power) % MOD;
            power = (power * BASE) % MOD;

            if hash == reverse_hash {
                length = i + 1;
            }
        }

        let mut result = s[length..].chars().rev().collect::<String>();
        result.push_str(&s);
        result
    }
}
//KDS

```

```JavaScript []
/**
 * @param {string} s
 * @return {string}
 */
var shortestPalindrome = function(s) {
    if (s.length <= 1) {
        return s;
    }

    const MOD = 1000000007;
    const BASE = 26;

    let hash = 0;
    let reverseHash = 0;
    let power = 1;
    let length = 0;

    for (let i = 0; i < s.length; i++) {
        hash = (hash * BASE + (s.charCodeAt(i) - 'a'.charCodeAt(0) + 1)) % MOD;
        reverseHash = (reverseHash + (s.charCodeAt(i) - 'a'.charCodeAt(0) + 1) * power) % MOD;
        power = (power * BASE) % MOD;

        if (hash === reverseHash) {
            length = i + 1;
        }
    }

    return s.slice(length).split('').reverse().join('') + s;
};
//KDS

```

---
### Appraoch 2
This following code implements a solution for finding the shortest palindrome by using a **double rolling hash** to compare the original string and its reverse as you iterate over the characters. The purpose of using double hashing is to reduce the risk of **hash collisions**, where two different substrings may accidentally produce the same hash. 

### Explanation of the Code:

1. **Double Hashing for Collision Prevention**:
   - You are using **two moduli (`MOD1`, `MOD2`)** to compute hashes, ensuring that even if one hash collision occurs, it's extremely unlikely that both will collide. This improves the reliability of your palindrome detection.
   - Both forward and reverse hashes are computed simultaneously for each character in the string.

2. **Forward and Reverse Hash Comparison**:
   - At each iteration, the algorithm computes two sets of hashes: one for the string as you read it forward (`hash1`, `hash2`), and one for the reverse of the string (`reverseHash1`, `reverseHash2`).
   - If both hash values (for the forward and reverse strings) match at any position, that means the substring up to that point forms a palindrome.

3. **Tracking the Longest Palindromic Prefix**:
   - The variable `len` keeps track of the length of the longest palindromic prefix found so far. At the end of the loop, you know the longest prefix of `s` that is a palindrome.
   - The non-palindromic remainder of the string (`s.substring(len)`) is reversed and added to the front of the string to make the whole string a palindrome.

### Differences from Initial Intuition:
- **Double Hashing**: 
  - In your initial intuition, we discussed using a **single rolling hash**. Here, **double hashing** is implemented using two different moduli to minimize the risk of collisions, which could cause incorrect palindrome detection.
- **Constantly Rolling the Hashes**:
  - The hash for both the original and the reversed substrings is **updated incrementally** as you process each character, making the approach very efficient and avoiding recalculating the hash from scratch each time.
- **Reverse Hash Computation**:
  - Instead of generating the reversed string explicitly and comparing it to the original, you're building the reverse hash on the fly, which is more memory efficient.

### Pseudo-code Breakdown:

```plaintext
Input: A string `s`
Output: The shortest palindrome by adding characters to the front

Constants:
    MOD1 = 1000000007  # First large prime modulus
    MOD2 = 1000000009  # Second large prime modulus
    BASE = 26          # Base for the rolling hash (size of the alphabet)

Function shortestPalindrome(s):
    If s is null or has length <= 1, return s
    
    Initialize:
        hash1, hash2 = 0, 0  # Forward rolling hashes for MOD1 and MOD2
        reverseHash1, reverseHash2 = 0, 0  # Reverse rolling hashes for MOD1 and MOD2
        power1, power2 = 1, 1  # Powers of BASE for computing reverse hashes
        len = 0  # Length of the longest palindromic prefix
    
    Loop through each character of `s`:
        For each character at index `i`:
            # Update forward hashes
            hash1 = (hash1 * BASE + (char_value)) % MOD1
            hash2 = (hash2 * BASE + (char_value)) % MOD2

            # Update reverse hashes (reverse the role of character positions)
            reverseHash1 = (reverseHash1 + (char_value) * power1) % MOD1
            reverseHash2 = (reverseHash2 + (char_value) * power2) % MOD2

            # Update powers of BASE
            power1 = (power1 * BASE) % MOD1
            power2 = (power2 * BASE) % MOD2

            # If forward and reverse hashes match (for both MOD1 and MOD2):
            If hash1 == reverseHash1 and hash2 == reverseHash2:
                Update `len` to i + 1  # Found a longer palindromic prefix
    
    # Create the palindrome:
    Take the non-palindromic suffix (s.substring(len))
    Reverse this suffix and add it to the front of the original string
    
    Return the new palindrome
```

### Key Differences from Initial Intuition:
- **Double Hashing**: This approach uses **two hashes** (`MOD1` and `MOD2`) to prevent hash collisions, while the initial intuition only discussed a single rolling hash. Double hashing is more robust when handling larger input sizes and helps avoid rare hash collisions.
  
- **Efficiency**: The algorithm computes the reverse hash on the fly without explicitly constructing the reversed string, making the process more space-efficient. This is a minor optimization over the idea in the intuition where we discussed explicitly reversing the string.

- **Power Tracking**: The computation of `power1` and `power2` ensures that the reverse hash is correctly weighted by character position, which was not explicitly mentioned in the intuition.

### Conclusion:
This code refines the initial intuition by **adding robustness (double hashing)** and **optimizing space usage (on-the-fly reverse hashing)**, making it more reliable and efficient, especially for large input strings.


### Approach 3


```Java []
class Solution {
    public String shortestPalindrome(String s) {
        if (s.isEmpty()) return s;
        
        String rev_s = new StringBuilder(s).reverse().toString();
        String combined = s + "#" + rev_s;
        
        int[] z = calculateZ(combined);
        
        int max_prefix = 0;
        for (int i = s.length() + 1; i < z.length; ++i) {
            if (z[i] == combined.length() - i) {
                max_prefix = z[i];
                break;
            }
        }
        
        return rev_s.substring(0, s.length() - max_prefix) + s;
    }
    
    private int[] calculateZ(String s) {
        int n = s.length();
        int[] z = new int[n];
        int l = 0, r = 0;
        
        for (int i = 1; i < n; ++i) {
            if (i <= r) {
                z[i] = Math.min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i])) {
                ++z[i];
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        
        return z;
    }
}
```
```C++ []
class Solution {
public:
    string shortestPalindrome(string s) {
        if (s.empty()) return s;

        string rev_s = s;
        reverse(rev_s.begin(), rev_s.end());
        string combined = s + "#" + rev_s;

        vector<int> z = calculateZ(combined);

        int max_prefix = 0;
        for (int i = s.length() + 1; i < z.size(); ++i) {
            if (z[i] == combined.length() - i) {
                max_prefix = z[i];
                break;
            }
        }

        return rev_s.substr(0, s.length() - max_prefix) + s;
    }

private:
    vector<int> calculateZ(const string& s) {
        int n = s.length();
        vector<int> z(n, 0);
        int l = 0, r = 0;

        for (int i = 1; i < n; ++i) {
            if (i <= r) {
                z[i] = min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
                ++z[i];
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }

        return z;
    }
};
```
```Python []
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        
        z = self.calculateZ(combined)
        
        max_prefix = 0
        for i in range(len(s) + 1, len(z)):
            if z[i] == len(combined) - i:
                max_prefix = z[i]
                break
        
        return rev_s[:len(s) - max_prefix] + s
    
    def calculateZ(self, s: str) -> list[int]:
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
        
        return z
```
