### Approach 1
Alright, let’s dive deeper into this problem and really break it down piece by piece, step by step. Imagine you’re sitting down with me, and we’re going to try to figure this out together. You know, before we jump into the nitty-gritty details, it’s important to take a step back and think about **what’s really happening here**. That way, the final solution will feel like a natural conclusion instead of something we just drop out of thin air.

So, what’s the problem really asking us? It’s asking us to figure out the **k-th bit in a sequence of binary strings**, and these strings grow based on a specific rule. The rule is pretty interesting: 

- The first string, $S_1$, is just `"0"`.
- Then, every string $S_i$ for $i > 1$ is formed by taking the previous string $S_{i-1}$, adding a `"1"` to it, and then appending the **reverse** of $S_{i-1}$ but with all the bits flipped (so 0s become 1s and 1s become 0s).

Let’s pause here for a second. This is a key part of the problem: the fact that each string is made up of a combination of the previous string, a `"1"`, and the flipped and reversed version of the previous string. This gives us a recursive structure, and it’s going to be crucial in solving the problem.

### Initial Exploration: Building the Sequence
We’re told that the sequence starts with $S_1 = "0"$, and every subsequent string is built off of the previous one. Let’s look at the first few strings, step by step, to get a better feel for how they grow:

- **$S_1$:**  
  The base case is given as "0".
  
- **$S_2$:**  
  To form $S_2$, we take $S_1$ (which is "0"), add a `"1"`, and then append the reverse and flipped version of $S_1$. The reverse of "0" is still "0", and flipping "0" gives "1". So, $S_2 = 0 + 1 + 1 = "011"$.

- **$S_3$:**  
  Now, to form $S_3$, we take $S_2$ (which is "011"), add a `"1"`, and then append the reverse and flipped version of $S_2$. The reverse of "011" is "110", and flipping it gives "001". So, $S_3 = 011 + 1 + 001 = "0111001"$.

- **$S_4$:**  
  For $S_4$, we take $S_3$ (which is "0111001"), add a `"1"`, and append the reverse and flipped version of $S_3$. The reverse of "0111001" is "1001110", and flipping it gives "0110001". So, $S_4 = 0111001 + 1 + 0110001 = "011100110110001"$.

You can start to see a pattern here, right? Each string is growing larger, and it’s made up of a few key components:
1. The previous string.
2. A middle bit that’s always a `"1"`.
3. The reverse of the previous string, with all the bits flipped.

### Problem Breakdown: What Are We Really Trying to Do?
The problem is asking us to find the **k-th bit** in the string $S_n$, given two integers $n$ (the level of the string) and $k$ (the position of the bit we want to find). But here’s the catch: the strings grow **exponentially** in size. The length of $S_n$ is $2^n - 1$, which grows very quickly as $n$ increases.

For example:
- $S_1$ has 1 bit.
- $S_2$ has 3 bits.
- $S_3$ has 7 bits.
- $S_4$ has 15 bits.
- By the time you get to $S_{20}$, you’ve got over a million bits!

Clearly, if we tried to **construct** the string directly for large $n$, it would take a huge amount of time and space. So, constructing the entire string just to find one bit isn’t practical. We need a different approach—something smarter that doesn’t involve building the whole string.

### Analyzing the Structure of the Strings
Let’s take a closer look at the structure of these strings, because understanding this structure is key to solving the problem efficiently.

If we look at any string $S_n$, we notice that it has three main parts:
1. The first part is just $S_{n-1}$ (the previous string).
2. The second part is a `"1"`, which is always the middle bit.
3. The third part is the reverse and flipped version of $S_{n-1}$.

This means that the string is **symmetric** around the middle bit, with the first half being exactly $S_{n-1}$ and the second half being the flipped and reversed version of $S_{n-1}$. So, instead of thinking about the whole string, we can start thinking about where the k-th bit lies in relation to the middle.

### The Middle Bit is Key
One important observation here is that the **middle bit** of every string is always `"1"`. For example:
- The middle bit of $S_2 = "011"$ is the 2nd bit, which is "1".
- The middle bit of $S_3 = "0111001"$ is the 4th bit, which is "1".
- The middle bit of $S_4 = "011100110110001"$ is the 8th bit, which is "1".

This gives us a very important clue: if $k$ happens to be the middle bit, we can immediately return `"1"`. No further work is needed.

The middle bit is always at position $2^{n-1}$ in $S_n$. For example:
- In $S_2$, the middle bit is at position $2^1 = 2$.
- In $S_3$, the middle bit is at position $2^2 = 4$.
- In $S_4$, the middle bit is at position $2^3 = 8$.

So, if $k$ is exactly $2^{n-1}$, we can return `"1"` right away. But what if $k$ is not the middle bit? Well, then we need to look at which half of the string $k$ lies in.

### Splitting the Problem: First Half or Second Half?
If $k$ is less than $2^{n-1}$, then the k-th bit lies in the **first half** of the string, which is exactly the same as $S_{n-1}$. So in that case, the problem reduces to finding the k-th bit in $S_{n-1}$.

On the other hand, if $k$ is greater than $2^{n-1}$, then the k-th bit lies in the **second half** of the string, which is the reversed and flipped version of the first half (i.e., $S_{n-1}$). This means that the k-th bit in $S_n$ corresponds to a bit in $S_{n-1}$, but in a mirrored position.

The mirrored position is $2^n - k$, and since the second half is the **inverted** version of the first half, we need to flip the bit we get from $S_{n-1}$.

### Recursive Structure of the Problem
Now we’re starting to see the recursive structure of the problem:
1. If $k = 2^{n-1}$, return "1".
2. If $k < 2^{n-1}$, the problem reduces to finding the k-th bit in $S_{n-1}$.
3. If $k > 2^{n-1}$, find the $(2^n - k)$-th bit in $S_{n-1}$, and then flip it.

This recursive approach allows us to solve the problem without ever building the entire string. Instead, we keep reducing the problem to smaller and smaller instances of itself, until we reach the base case where $n = 1$ and the answer is simply "0".

### Edge Cases and Final Thoughts
There are a few potential pitfalls or edge cases to think about. For example, if $k$ is exactly the middle bit, it’s easy to return the wrong value if we don’t handle that case separately. Similarly, we need to be careful with the flipping operation when we’re in the second half of the string.

But overall, this recursive approach is efficient. We’re using the structure of the problem to avoid building the entire string, and instead focusing only on the parts we care about. The time complexity is much better than the brute-force approach, because each recursive step reduces the problem size by half, making it logarithmic in terms of the size of the string.

### Wrapping Up


So, to summarize:
- The problem is really about understanding the recursive structure of the strings.
- Each string is made up of the previous string, a middle bit, and a reversed and flipped version of the previous string.
- The middle bit is always "1", and if $k$ is in the first half, we just need to find the k-th bit in the previous string. If $k$ is in the second half, we mirror the position and flip the bit.
- This recursive approach allows us to efficiently find the k-th bit without constructing the entire string, even for large values of $n$.

This approach not only makes the problem manageable but also highlights the power of recursive thinking when dealing with self-similar structures like these binary strings.
### Code

```Java []
class Solution {
    public char findKthBit(int n, int k) {
        if (n == 1) return '0';
        
        int midPoint = 1 << (n - 1);
        
        if (k == midPoint) return '1';
        
        if (k < midPoint) {
            return findKthBit(n - 1, k);
        } else {
            return invert(findKthBit(n - 1, 2 * midPoint - k));
        }
    }
    
    private char invert(char c) {
        return c == '0' ? '1' : '0';
    }
}
//Kartikdevsharmaa
```
```C++ []
class Solution {
public:
    char findKthBit(int n, int k) {
        if (n == 1) return '0';
        
        int midPoint = 1 << (n - 1);
        
        if (k == midPoint) return '1';
        
        if (k < midPoint) {
            return findKthBit(n - 1, k);
        } else {
            return invert(findKthBit(n - 1, 2 * midPoint - k));
        }
    }
    
private:
    char invert(char c) {
        return c == '0' ? '1' : '0';
    }
};
//Kartikdevsharmaa
```
```Python []
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        
        mid_point = 1 << (n - 1)
        
        if k == mid_point:
            return '1'
        
        if k < mid_point:
            return self.findKthBit(n - 1, k)
        else:
            return self.invert(self.findKthBit(n - 1, 2 * mid_point - k))
    
    def invert(self, c: str) -> str:
        return '1' if c == '0' else '0'
#Kartikdevsharmaa
```
```Go []
func findKthBit(n int, k int) byte {
    if n == 1 {
        return '0'
    }
    
    midPoint := 1 << (n - 1)
    
    if k == midPoint {
        return '1'
    }
    
    if k < midPoint {
        return findKthBit(n - 1, k)
    } else {
        return invert(findKthBit(n - 1, 2*midPoint - k))
    }
}

func invert(c byte) byte {
    if c == '0' {
        return '1'
    }
    return '0'
}
//Kartikdevsharmaa
```
```Rust []
impl Solution {
    pub fn find_kth_bit(n: i32, k: i32) -> char {
        if n == 1 {
            return '0';
        }
        
        let mid_point = 1 << (n - 1);
        
        if k == mid_point {
            return '1';
        }
        
        if k < mid_point {
            Self::find_kth_bit(n - 1, k)
        } else {
            Self::invert(Self::find_kth_bit(n - 1, 2 * mid_point - k))
        }
    }
    
    fn invert(c: char) -> char {
        if c == '0' { '1' } else { '0' }
    }
}
//Kartikdevsharmaa
```
```JavaScript []
/**
 * @param {number} n
 * @param {number} k
 * @return {character}
 */
var findKthBit = function(n, k) {
    if (n === 1) return '0';
    
    const midPoint = 1 << (n - 1);
    
    if (k === midPoint) return '1';
    
    if (k < midPoint) {
        return findKthBit(n - 1, k);
    } else {
        return invert(findKthBit(n - 1, 2 * midPoint - k));
    }
};

function invert(c) {
    return c === '0' ? '1' : '0';
}
//Kartikdevsharmaa
```

### Approach 2
Alright, now let’s build on top of the intuition we just developed, but take it a step further with a slightly different approach. We already have a deep understanding of how these strings are structured and how recursion can help us efficiently find the k-th bit without generating the entire string. But the next approach introduces an important optimization: **avoiding recursion entirely** by using an iterative solution that makes the process more direct.

### Revisiting the Problem
To quickly recap the key ideas from the previous approach:
- Each string $S_n$ is constructed recursively from the previous string, a middle bit "1", and the reversed and flipped version of the previous string.
- We identified that the **middle bit** in every string $S_n$ is always "1", and the string is symmetric around this middle bit. If $k$ is in the second half of the string, it corresponds to a mirrored position in the first half, and we need to flip the bit we find in that mirrored position.

In the recursive solution, we handled this by reducing the size of the problem step by step until we reached $S_1$, the base case, where we could directly return the answer. But now we want to take a more **iterative** approach and avoid recursion altogether, which is often more efficient in terms of memory usage.

### Optimizing with an Iterative Approach

The idea behind this iterative solution is similar to the recursive one, but instead of reducing the problem size by making recursive calls, we’ll handle everything in a single while loop. Essentially, we’re still narrowing down the problem, but we’re doing it in-place, using a simple **inversion flag** to keep track of whether we need to flip the bit or not.

#### Breaking Down the Iterative Approach

Let’s walk through this new approach step by step:

1. **Initialization:**
   - We start by setting a flag called `shouldInvert` to `false`. This flag will help us keep track of whether we need to **invert** the bit at the end.
   - The idea here is that every time we step into the **second half** of the string, we’re actually looking at the flipped version of the first half. So, every time we do this, we’ll flip the value of the `shouldInvert` flag.

2. **Moving Through the Levels:**
   - Instead of reducing the problem size recursively, we reduce $n$ iteratively. Each iteration in the while loop represents moving from $S_n$ down to $S_{n-1}$, and we adjust $k$ based on whether it’s in the first or second half.
   
3. **The Middle Bit:**
   - Just like before, we calculate the **middle bit** of $S_n$. The middle bit is always at position $2^{n-1}$. This middle bit is always "1", and if $k$ equals the middle bit’s position, we can immediately return our answer.
   - If the `shouldInvert` flag is `false`, we return '1' (since the middle bit is "1"). If the flag is `true`, we return '0' (since it’s the flipped version of "1").

4. **First Half or Second Half:**
   - If $k$ is less than the middle bit, we don’t need to do anything special—we just move on to the next level $S_{n-1}$.
   - But if $k$ is greater than the middle bit, we know we’re in the second half of the string, which is the flipped and reversed version of the first half. Here’s what happens:
     - We adjust $k$ to reflect its **mirrored position** in the first half: $k = 2^n - k$.
     - We also flip the `shouldInvert` flag because the second half is the inverted version of the first half, meaning we need to invert the bit we find when we eventually reach it.

5. **Base Case:**
   - Once $n$ reaches 1, we’ve boiled the problem down to $S_1$, which is just "0". At this point, if `shouldInvert` is `false`, we return '0', and if it’s `true`, we return '1' (since the inversion flips the "0" to "1").

### Why This Approach Works

Now, let’s discuss **why** this iterative approach is efficient and effective.

- **Avoiding Recursion:** 
  In the recursive solution, each recursive call takes up space on the call stack, which can lead to increased memory usage, especially for larger values of $n$. By eliminating recursion and using a simple loop, we avoid that overhead.
  
- **Tracking Inversion with a Flag:** 
  The key insight here is that the **inversion** of the second half can be tracked with a boolean flag (`shouldInvert`). Instead of actually flipping bits during the string construction (which we never do since we don’t construct the string), we just **remember** whether we need to invert the final answer. This is a simple but very powerful optimization because it allows us to reduce the complexity of the problem while still getting the correct answer.

- **Efficiently Adjusting $k$:**
  In each iteration, if $k$ is in the second half of the string, we compute its **mirrored position** in the first half. This lets us "move" the problem into the first half, which is the same as the previous string, $S_{n-1}$. By doing this iteratively, we’re always reducing the size of the problem and ensuring that we don’t need to think about the whole string at once.

### Example Walkthrough

Let’s go through an example to see how this plays out in practice. Consider the case where $n = 4$ and $k = 11$.

1. **Initial State:**
   - We start with $n = 4$, $k = 11$, and `shouldInvert = false`.

2. **First Iteration (n = 4):**
   - The midpoint is $2^3 = 8$. Since $k = 11 > 8$, we know that $k$ lies in the second half.
   - We calculate the mirrored position of $k$: $k = 2 \times 8 - 11 = 5$.
   - We flip the `shouldInvert` flag, so now `shouldInvert = true`.
   - We move to the next level: $n = 3$.

3. **Second Iteration (n = 3):**
   - The midpoint is $2^2 = 4$. Since $k = 5 > 4$, we’re in the second half again.
   - We calculate the mirrored position: $k = 2 \times 4 - 5 = 3$.
   - We flip the `shouldInvert` flag again, so now `shouldInvert = false`.
   - Move to the next level: $n = 2$.

4. **Third Iteration (n = 2):**
   - The midpoint is $2^1 = 2$. Since $k = 3 > 2$, we’re in the second half.
   - Mirrored position: $k = 2 \times 2 - 3 = 1$.
   - Flip `shouldInvert` again, so now `shouldInvert = true`.
   - Move to the next level: $n = 1$.

5. **Final Iteration (n = 1):**
   - We’ve reached $S_1$, which is just "0". Since `shouldInvert = true`, we return '1' (the inverted version of "0").

### Final Thoughts

This iterative approach has several advantages:
- **Time Efficiency:** We never build the full string, and each iteration reduces the size of the problem, making it logarithmic in terms of time complexity.
- **Space Efficiency:** By avoiding recursion, we save memory and only use a constant amount of extra space (for variables like `shouldInvert` and `k`).
- **Clarity and Simplicity:** The logic is straightforward: adjust $k$, flip the inversion flag when necessary, and finally return the correct bit once we reduce the problem down to $S_1$.

This is a very clean and efficient solution that builds directly on the recursive approach, but takes it one step further by optimizing for both time and space!

#### Code 

```Java []
class Solution {
    public char findKthBit(int n, int k) {
        boolean shouldInvert = false;
        
        while (n > 1) {
            int midPoint = 1 << (n - 1);
            
            if (k == midPoint) {
                return shouldInvert ? '0' : '1';
            }
            
            if (k > midPoint) {
                k = 2 * midPoint - k;
                shouldInvert = !shouldInvert;
            }
            
            n--;
        }
        
        return shouldInvert ? '1' : '0';
    }
}
//Kartikdevsharmaa
```
```C++ []
class Solution {
public:
    char findKthBit(int n, int k) {
        bool shouldInvert = false;
        
        while (n > 1) {
            int midPoint = 1 << (n - 1);
            
            if (k == midPoint) {
                return shouldInvert ? '0' : '1';
            }
            
            if (k > midPoint) {
                k = 2 * midPoint - k;
                shouldInvert = !shouldInvert;
            }
            
            n--;
        }
        
        return shouldInvert ? '1' : '0';
    }
};
```
```Python []
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        should_invert = False
        
        while n > 1:
            mid_point = 1 << (n - 1)
            
            if k == mid_point:
                return '0' if should_invert else '1'
            
            if k > mid_point:
                k = 2 * mid_point - k
                should_invert = not should_invert
            
            n -= 1
        
        return '1' if should_invert else '0'
```
```Go []
func findKthBit(n int, k int) byte {
    shouldInvert := false
    
    for n > 1 {
        midPoint := 1 << (n - 1)
        
        if k == midPoint {
            if shouldInvert {
                return '0'
            }
            return '1'
        }
        
        if k > midPoint {
            k = 2*midPoint - k
            shouldInvert = !shouldInvert
        }
        
        n--
    }
    
    if shouldInvert {
        return '1'
    }
    return '0'
}
```
```Rust []
impl Solution {
    pub fn find_kth_bit(n: i32, k: i32) -> char {
        let mut n = n;
        let mut k = k;
        let mut should_invert = false;
        
        while n > 1 {
            let mid_point = 1 << (n - 1);
            
            if k == mid_point {
                return if should_invert { '0' } else { '1' };
            }
            
            if k > mid_point {
                k = 2 * mid_point - k;
                should_invert = !should_invert;
            }
            
            n -= 1;
        }
        
        if should_invert { '1' } else { '0' }
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number} k
 * @return {character}
 */
var findKthBit = function(n, k) {
    let shouldInvert = false;
    
    while (n > 1) {
        const midPoint = 1 << (n - 1);
        
        if (k === midPoint) {
            return shouldInvert ? '0' : '1';
        }
        
        if (k > midPoint) {
            k = 2 * midPoint - k;
            shouldInvert = !shouldInvert;
        }
        
        n--;
    }
    
    return shouldInvert ? '1' : '0';
};
```

### Approach 3
Alright, now let's dive into the third approach while building on everything we’ve discussed so far. This solution, though appearing quite different, is still rooted in the core ideas we've been working with—the structure of the string, the symmetry, and how flipping bits in the second half relates to mirroring in the first half. However, here we bring in some new tricks using **bitwise operations** to further optimize how we identify the correct bit. This method is both more abstract and compact, and involves a bit of number theory as well.

### Refresher on the Problem
Before we get into the new approach, let’s remind ourselves of the goal:
- We are dealing with a binary string $S_n$ that is generated recursively, with each new string $S_i$ being composed of the previous string, a "1", and the reverse/inverted version of the previous string.
- Our task is to find the $k$-th bit in $S_n$, but instead of generating the entire string (which becomes impossibly large as $n$ grows), we need an efficient way to determine the bit at position $k$.

The previous approaches relied heavily on recursion and iteration to break the problem down, tracking inversions as we moved between the first and second halves of the string. But this new approach uses **bit manipulation** to directly calculate the result in a more mathematical way, focusing on properties of numbers.

### Core Insights in the Third Approach

In this approach, we’re going to think of the problem in terms of **patterns in the binary representation** of the number $k$ and use bitwise operations to efficiently extract the information we need. Here’s how the thinking goes:

1. **Binary Representation of $k$:**
   - The position $k$ is an integer, and integers can be represented as binary numbers.
   - Instead of viewing the problem as moving through levels of recursive string construction, we can look at the **set bits** (i.e., the 1's) in the binary representation of $k$ to understand the position of $k$ in the recursive structure of the string.

2. **Rightmost Set Bit:**
   - One key observation is that the **rightmost set bit** in $k$ (i.e., the least significant bit that is 1) can tell us a lot about the symmetry of the string around $k$.
   - Using the operation `k & -k`, we can isolate this rightmost set bit. This is a common bitwise trick that allows us to quickly find which power of two the position $k$ is closest to.

3. **Odd or Even Set Bits Before $k$:**
   - Another observation is that whether $k$ lies in the "flipped" part of the string depends on whether the number of set bits before $k$ is odd or even.
   - By checking the number of bits to the left of the rightmost set bit, we can determine whether $k$ is in the first or second half of its current mirrored segment. If this number is odd, we know that we’re in the "flipped" portion of the string, and the bit will be inverted.

4. **Odd or Even $k$:**
   - Finally, we can determine whether $k$ itself is odd or even using the simple condition `k & 1`. This helps us handle edge cases where the position $k$ may be right on the boundary between mirrored segments.

5. **Combining These Conditions:**
   - The last step is to combine these two conditions—whether the number of set bits is odd and whether $k$ is odd—and use them to decide whether the $k$-th bit is flipped or not.
   - This is done with an XOR operation, which is a natural fit for determining whether two conditions combine to form a flip. If either condition (odd set bits or odd $k$) results in a flip, we invert the bit; otherwise, we don’t.

### Breaking Down the Approach

Now that we have the core ideas in mind, let’s walk through the approach step by step:

1. **Isolating the Rightmost Set Bit:**
   - We calculate the **rightmost set bit** of $k$ using the expression `k & -k`. This gives us a power of two that represents the smallest bit in $k$ that is set to 1.
   - This helps us understand the current "segment" of the string we’re working with.

2. **Counting Set Bits Before $k$:**
   - By dividing $k$ by this rightmost set bit and then shifting the result right (`>> 1`), we effectively count the number of bits to the left of this set bit.
   - We then check whether this count is odd or even using another bitwise trick: `(k / rightmostSetBit) >> 1 & 1`. If this expression equals 1, we know the number of set bits is odd, meaning $k$ lies in the flipped portion of the string.

3. **Checking if $k$ is Odd:**
   - We also check whether $k$ is odd using the simple condition `k & 1`. This is a quick way to determine whether $k$ is on the boundary of a mirrored segment.

4. **XOR to Determine the Final Bit:**
   - Finally, we combine these two conditions—whether the number of set bits is odd and whether $k$ is odd—using the XOR operation. If either one of these conditions is true, we flip the bit; otherwise, we leave it as is.
   - We convert the result to a character by adding `'0'` to the result (either 0 or 1).

### Why This Works

This solution is clever because it condenses the entire recursive structure of the problem into a few bitwise operations. By focusing on the **binary representation of $k$** and using properties of numbers like set bits and powers of two, we avoid having to explicitly handle the symmetry and inversion that we dealt with in previous approaches.

The bitwise operations let us quickly determine whether $k$ is in the flipped portion of the string and whether it should be inverted, without needing to recursively walk through the construction of the string.

### Example Walkthrough

Let’s run through an example with $n = 4$ and $k = 11$:

1. **Rightmost Set Bit:**
   - $k = 11$ in binary is `1011`.
   - The rightmost set bit is `k & -k = 1` (the least significant bit that is set to 1).

2. **Counting Set Bits:**
   - Dividing $k$ by the rightmost set bit gives `11 / 1 = 11`, which in binary is `1011`.
   - Shifting this value right by one bit gives `101`, which means there are **three set bits** to the left of the rightmost set bit (so the number of set bits before $k$ is odd).

3. **Checking if $k$ is Odd:**
   - $k = 11$ is odd (`k & 1 = 1`), so we know $k$ is on the boundary of a mirrored segment.

4. **Final XOR Check:**
   - We XOR the two conditions: the number of set bits is odd, and $k$ is odd. XORing these two values gives `1 ^ 1 = 0`, meaning the bit at position $k$ is not inverted.
   - Therefore, the result is `'0'`.

### Final Thoughts

This approach is a more **mathematical and abstract** way to tackle the problem, but it’s extremely efficient. By leveraging bitwise operations, we avoid the need for recursion or iteration and instead make use of the **binary representation** of the position $k$ to determine the answer directly.

The key insights here involve:
- Using the **rightmost set bit** to understand the current segment.
- Counting set bits to figure out whether we’re in the flipped part of the string.
- Using XOR to combine these conditions and determine the final bit.

This solution is both elegant and highly efficient, operating in constant time $O(1)$ for each query—perfect for large inputs.

### Code
```Java []
class Solution {
    public char findKthBit(int n, int k) {
        // Calculate the position of the rightmost set bit
        int rightmostSetBit = k & -k;
        
        // Determine if the number of set bits before k is odd
        boolean isOddSetBits = ((k / rightmostSetBit) >> 1 & 1) == 1;
        
        // Determine if k is odd
        boolean isKOdd = (k & 1) == 1;
        
        // XOR the above conditions and convert to char
        return (char)((isOddSetBits ^ !isKOdd ? 1 : 0) + '0');
    }
}
//kartikdevsharmaa
```
```C++ []
class Solution {
public:
    char findKthBit(int n, int k) {
        // Calculate the position of the rightmost set bit
        int rightmostSetBit = k & -k;
        
        // Determine if the number of set bits before k is odd
        bool isOddSetBits = ((k / rightmostSetBit) >> 1 & 1) == 1;
        
        // Determine if k is odd
        bool isKOdd = (k & 1) == 1;
        
        // XOR the above conditions and convert to char
        return (isOddSetBits ^ !isKOdd ? '1' : '0');
    }
};
//Kartikdevsharmaa
```
```Python []
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Calculate the position of the rightmost set bit
        rightmost_set_bit = k & -k
        
        # Determine if the number of set bits before k is odd
        is_odd_set_bits = ((k // rightmost_set_bit) >> 1 & 1) == 1
        
        # Determine if k is odd
        is_k_odd = (k & 1) == 1
        
        # XOR the above conditions and convert to char
        return '1' if is_odd_set_bits ^ (not is_k_odd) else '0'
#Kartikdevsharmaa
```
```Go []
func findKthBit(n int, k int) byte {
    // Calculate the position of the rightmost set bit
    rightmostSetBit := k & -k
    
    // Determine if the number of set bits before k is odd
    isOddSetBits := ((k / rightmostSetBit) >> 1 & 1) == 1
    
    // Determine if k is odd
    isKOdd := (k & 1) == 1
    
    // XOR the above conditions and convert to byte
    if isOddSetBits != isKOdd {
        return '0'
    }
    return '1'
}
```
```Rust []
impl Solution {
    pub fn find_kth_bit(n: i32, k: i32) -> char {
        // Calculate the position of the rightmost set bit
        let rightmost_set_bit = k & -k;
        
        // Determine if the number of set bits before k is odd
        let is_odd_set_bits = ((k / rightmost_set_bit) >> 1 & 1) == 1;
        
        // Determine if k is odd
        let is_k_odd = (k & 1) == 1;
        
        // XOR the above conditions and convert to char
        if is_odd_set_bits ^ !is_k_odd { '1' } else { '0' }
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number} k
 * @return {character}
 */
var findKthBit = function(n, k) {
    // Calculate the position of the rightmost set bit
    const rightmostSetBit = k & -k;
    
    // Determine if the number of set bits before k is odd
    const isOddSetBits = ((k / rightmostSetBit >> 1) & 1) === 1;
    
    // Determine if k is odd
    const isKOdd = (k & 1) === 1;
    
    // XOR the above conditions and convert to char
    return String.fromCharCode((isOddSetBits ^ !isKOdd ? 1 : 0) + 48);
};
```
