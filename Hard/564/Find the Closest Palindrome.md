
# Intuition



First, we need to understand what the problem is asking. Lets say we are Given a string representation of a number, we're asked to find the closest palindrome to that number, excluding the number itself. If there's a tie (two palindromes equally close), we should return the smaller one. The "closest" is defined by the smallest absolute difference between the given number and the palindrome.

The constraints are very important to consider:
1. The input string length is between 1 and 18 characters.
2. The input consists only of digits.
3. There are no leading zeros.
4. The number represented is between 1 and  $10 ^{18}$ - 1

By just looking at these constraints  we can tell that we're dealing with potentially very large numbers, which also explains why the input is given as a string. We'll use long integers in our calculations since we need to be careful about integer overflow.

Now, let's think about palindromes. What makes a number a palindrome? It reads the same forwards and backwards. For example, 12321 is a palindrome. This structure tell us that we can focus on the left half of the number (which we'll call the "palindrome root") and use it to generate the full palindrome.

 for a palindrome like 12321, the next larger palindrome is 12421, and the next smaller is 12221. This pattern holds for both odd and even-length palindromes. This means that we can generate candidate palindromes by using left half of the number

My First approach had some limitations it was failing a lot of edge cases. It was handling several special cases separately, which made my code more complex plus It also wasn't considering all possible nearest palindromes in some cases.

So in this approach, I'll consider five candidate palindromes:

1. The palindrome formed by decrementing the left half of the number.
2. The palindrome formed by the left half of the number as is.
3. The palindrome formed by incrementing the left half of the number.
4. The number with all 9's that has one digit less than the input.
5. The number with all 0's and 1's at the ends that has one digit more than the input.

Why these five candidates? Let's think about it:

1-3: These cover the cases where the nearest palindrome is close to the original number. By considering the current left half and its incremented and decremented versions, we cover a range of nearby palindromes.

4: This covers cases where the nearest palindrome might be a "9" palindrome just below our number. For example, if our number is 1000, the nearest smaller palindrome is 999.

5: This covers cases where the nearest palindrome might be just above our number with an additional digit. For example, if our number is 999, the nearest larger palindrome is 1001.

Since we are considering these five candidates, we are making sure that we don't miss any potential nearest palindromes, regardless of  what the input number's structure is.

Another thing to note here is that we can generate palindromes by manipulating just the left half of the number. This is because the right half is always a mirror of the left half (with a possible middle digit for odd-length palindromes).

Now we need to generate these palindromes, compare them to find the closest one, and handle all the edge cases correctly. We need to be careful about numbers at the boundaries (like 1, 10, 11, etc.) and make sure our solution works for all possible inputs within the given constraints.


# Approach


1. Convert the input string to a long integer:
   ```
   number = parse_long(numberStr)
   ```

2. Handle special cases for small numbers:
   ```
   if number <= 10:
       return string(number - 1)
   if number == 11:
       return "9"
   ```
   These cases are handled separately because they don't follow the general pattern.

3. Calculate the length of the input number and extract the left half:
   ```
   length = length(numberStr)
   leftHalf = parse_long(numberStr.substring(0, (length + 1) / 2))
   ```
   We use (length + 1) / 2 to handle both odd and even length numbers correctly.

4. Generate the five candidate palindromes:
   ```
   candidates = new array of size 5
   candidates[0] = generatePalindrome(leftHalf - 1, length % 2 == 0)
   candidates[1] = generatePalindrome(leftHalf, length % 2 == 0)
   candidates[2] = generatePalindrome(leftHalf + 1, length % 2 == 0)
   candidates[3] = 10^(length - 1) - 1
   candidates[4] = 10^length + 1
   ```
   The generatePalindrome function (which we'll define later) creates a palindrome from the left half.

5. Find the nearest palindrome:
   ```
   nearestPalindrome = 0
   minDifference = MAX_LONG_VALUE
   for each candidate in candidates:
       if candidate == number:
           continue
       difference = abs(candidate - number)
       if difference < minDifference OR (difference == minDifference AND candidate < nearestPalindrome):
           minDifference = difference
           nearestPalindrome = candidate
   ```
   This loop compares each candidate to the original number, keeping track of the closest palindrome. If there's a tie, it chooses the smaller one.

6. Return the result:
   ```
   return string(nearestPalindrome)
   ```

Now, let's define the generatePalindrome function:

```
function generatePalindrome(leftHalf, isEvenLength):
    palindrome = leftHalf
    if not isEvenLength:
        leftHalf = leftHalf / 10
    while leftHalf > 0:
        palindrome = palindrome * 10 + leftHalf % 10
        leftHalf = leftHalf / 10
    return palindrome
```

This function works as follows:
- It starts with the left half of the palindrome.
- If the length is odd, it removes the last digit of the left half (which will be the middle digit of the palindrome).
- It then mirrors the remaining digits to create the right half of the palindrome.

The key to this approach is considering all possible nearest palindromes efficiently. By generating just five candidates, we cover all cases:

1. The palindrome formed by decrementing the left half covers cases where the nearest palindrome is slightly smaller.
2. The palindrome formed by the left half as-is covers cases where the nearest palindrome is very close to the original number.
3. The palindrome formed by incrementing the left half covers cases where the nearest palindrome is slightly larger.
4. The all-9s number with one less digit covers cases like 1000, where 999 is the nearest palindrome.
5. The number with 1 and trailing 0s with one more digit covers cases like 999, where 1001 is the nearest palindrome.

It works for both odd and even length numbers and correctly handles edge cases at the boundaries of the input range.

# Complexity
- Time complexity: O(log n), where n is the input number. This is because we're primarily working with the digits of the number, and the number of digits is logarithmic in the value of the number. The generatePalindrome function runs in O(log n) time, and we call it a constant number of times.

- Space complexity: O(log n). We're using a constant amount of extra space (the candidates array is always size 5), but we need O(log n) space to store the string representation of the number and the result.

# Code
Java
```Java []
class Solution {
    public String nearestPalindromic(String numberStr) {
        long number = Long.parseLong(numberStr);
        if (number <= 10) return String.valueOf(number - 1);
        if (number == 11) return "9";

        int length = numberStr.length();
        long leftHalf = Long.parseLong(numberStr.substring(0, (length + 1) / 2));
        
        long[] palindromeCandidates = new long[5];
        palindromeCandidates[0] = generatePalindromeFromLeft(leftHalf - 1, length % 2 == 0);
        palindromeCandidates[1] = generatePalindromeFromLeft(leftHalf, length % 2 == 0);
        palindromeCandidates[2] = generatePalindromeFromLeft(leftHalf + 1, length % 2 == 0);
        palindromeCandidates[3] = (long)Math.pow(10, length - 1) - 1;
        palindromeCandidates[4] = (long)Math.pow(10, length) + 1;

        long nearestPalindrome = 0;
        long minDifference = Long.MAX_VALUE;

        for (long candidate : palindromeCandidates) {
            if (candidate == number) continue;
            long difference = Math.abs(candidate - number);
            if (difference < minDifference || (difference == minDifference && candidate < nearestPalindrome)) {
                minDifference = difference;
                nearestPalindrome = candidate;
            }
        }

        return String.valueOf(nearestPalindrome);
    }

    private long generatePalindromeFromLeft(long leftHalf, boolean isEvenLength) {
        long palindrome = leftHalf;
        if (!isEvenLength) leftHalf /= 10;
        while (leftHalf > 0) {
            palindrome = palindrome * 10 + leftHalf % 10;
            leftHalf /= 10;
        }
        return palindrome;
    }
}
```
# You don't wanna read this 

Certainly! Let's delve into a mathematical explanation to justify why the approach works and why it effectively identifies the closest palindrome. This will involve analyzing the structure of palindromes, the properties of numbers, and how the algorithm logically narrows down the closest candidates.

### **1. Palindrome Structure and Reflection**

A palindrome is a number that reads the same forward and backward. For any given number `n` with `d` digits, we can divide `n` into two halves:
- **Left Half (`L`)**: The first ${\lceil\frac{d}{2} \rceil}$ digits.
- **Right Half (`R`)**: The remaining $\lfloor\frac{d}{2} \rfloor$ digits, which are the mirror image of the left half.

Mathematically, if `n` is a palindrome, then:
$n = L \times 10^{\lfloor \frac{d}{2} \rfloor} + \text{reverse}(L)$
where `reverse(L)` is the reverse of the left half.

### **2. Key Observations About Palindromes**

1. **Generation of Palindromes from Left Half**:
   - The closest palindrome to any given number `n` can be derived by altering the left half `L` slightly and reflecting it.
   - For a given `L`, there are three key palindromes:
     - **Equal Palindrome**: Reflect `L` as it is.
     - **Higher Palindrome**: Increment `L` by 1, then reflect.
     - **Lower Palindrome**: Decrement `L` by 1, then reflect.

2. **Boundary Conditions**:
   - For numbers like `999`, the closest palindromes can jump to a different order of magnitude (e.g., `1001`). This is why we include the edge cases of $10^d + 1$ and $10^{d-1} - 1$.
   - Similarly, numbers like `1000` may have their closest palindrome in the lower order (e.g., `999`).

### **3. Proof of Optimality in Candidate Selection**

#### **Generating Palindromes:**
- **Equal Palindrome**: Let's denote the original number as `n` and its left half as `L`. The palindrome generated by reflecting `L` without modification is:

  $P_{equal}$ = $L \times 10^{\lfloor \frac{d}{2} \rfloor} + \text{reverse}(L)$
  This palindrome has the same order of magnitude as `n` and is typically close to `n`.

- **Higher Palindrome**: Incrementing the left half by 1 and reflecting it gives us:

  $P_{high}$ = $(L + 1) \times 10^{\lfloor \frac{d}{2} \rfloor} + \text{reverse}(L + 1)$
  This palindrome is slightly larger than `n`, and it might be the closest if `n` is just below a midpoint between two palindromes.

- **Lower Palindrome**: Decrementing the left half by 1 and reflecting it gives:
  
  $P_{low}$ = $(L - 1) \times 10^{\lfloor \frac{d}{2} \rfloor} + \text{reverse}(L - 1)$
  This palindrome is slightly smaller than `n`, and it might be the closest if `n` is just above a midpoint between two palindromes.

#### **Edge Cases**:
- **Smallest and Largest Possible Palindromes**: To ensure the closest palindrome is captured, consider:
  - **Smallest Candidate**: $10^{d-1} - 1$ (e.g., `999` for three digits).
  - **Largest Candidate**: $10^d + 1$ (e.g., `1001` for three digits).

These are particularly relevant when the number `n` is at the boundary of a digit length (e.g., transitioning from `999` to `1000`).

### **4. Proving Minimum Distance**

Given the palindromes generated $P_{equal}$, $P_{high}$, $P_{low}$, and edge cases, we need to show that the closest palindrome to `n` is always among these.

**Mathematically**, the closest palindrome $P_{min}$ is defined as:

$P_{min}$ = $min_{all P} |n - P|$

where `P` is any possible palindrome. 

By generating palindromes as described:
1. **Distance Calculation**: For each generated palindrome `P`, calculate the absolute difference $| n - P|$
2. **Comparison**: Compare these distances:
   - If $| n - P_{low}|$ $<=$ $| n - P_{high}|$ and  $| n - P_{low}|$ $<=$  $| n - P_{equal}|$, then $P_{low}$ is the closest.
   - If there is a tie (i.e., multiple palindromes are at the same distance), choose the smallest one, which is straightforward to identify.

**Why Only These Candidates?**
- Any palindrome significantly different from these would require a larger change to `L`, either by increasing or decreasing it more than by 1. Such changes would yield a palindrome with a much larger distance from `n`, proving that such candidates cannot be closer.



Thus, the approach works because:
- **It considers all structurally relevant palindromes** by manipulating the left half of the number.
- **It handles edge cases** by including boundary palindromes at digit transitions.
- **It ensures the closest palindrome is identified** by minimizing the absolute difference and choosing the smaller one in case of a tie.

Mathematically, this covers all possible closest palindromes, ensuring the solution is both optimal and efficient.
