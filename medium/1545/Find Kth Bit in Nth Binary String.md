### Approach 1

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

```
```Python []

```
```Go []

```
```Rust []

```
```JavaScript []

```

### Approach 3

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
