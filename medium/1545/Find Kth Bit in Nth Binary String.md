```Java []
class Solution {
    public char findKthBit(int n, int k) {

        if (n == 1) return '0';

        int mid = (1 << (n - 1)) - 1; // 2^(n-1) - 1
        
        if (k <= mid) {
            return findKthBit(n - 1, k);
        } else if (k == mid + 1) {

            return '1';
        } else {
            return findKthBit(n - 1, (1 << n) - k) == '0' ? '1' : '0';
        }
    }
}

//https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/submissions/1371157989/

```
```C++ []
class Solution {
public:
    char findKthBit(int n, int k) {
        if (n == 1) return '0';

        int mid = (1 << (n - 1)) - 1; // 2^(n-1) - 1
        
        if (k <= mid) {
            return findKthBit(n - 1, k);
        } else if (k == mid + 1) {
            return '1';
        } else {
            return findKthBit(n - 1, (1 << n) - k) == '0' ? '1' : '0';
        }
    }
};


//https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/submissions/1371159488/

```
```Python []
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        mid = (1 << (n - 1)) - 1  
        
        if k <= mid:
            return self.findKthBit(n - 1, k)
        elif k == mid + 1:
            return '1'
        else:
            return '1' if self.findKthBit(n - 1, (1 << n) - k) == '0' else '0'

#https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/submissions/1371161345/

```
```Go []
func findKthBit(n int, k int) byte {
    if n == 1 {
        return '0'
    }

    mid := (1 << (n - 1)) - 1 // 2^(n-1) - 1
    
    if k <= mid {
        return findKthBit(n-1, k)
    } else if k == mid+1 {
        return '1'
    } else {
        if findKthBit(n-1, (1<<n)-k) == '0' {
            return '1'
        }
        return '0'
    }
}

//https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/submissions/1371154997/

```
```Rust []
impl Solution {
    pub fn find_kth_bit(n: i32, k: i32) -> char {
        if n == 1 {
            return '0';
        }

        let mid = (1 << (n - 1)) - 1; // 2^(n-1) - 1
        
        if k <= mid {
            return Self::find_kth_bit(n - 1, k);
        } else if k == mid + 1 {
            return '1';
        } else {
            return if Self::find_kth_bit(n - 1, (1 << n) - k) == '0' {
                '1'
            } else {
                '0'
            };
        }
    }
}

//https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/submissions/1371163134/


```
```JavaScript []
/**
 * @param {number} n
 * @param {number} k
 * @return {character}
 */
var findKthBit = function(n, k) {
    if (n === 1) return '0';

    const mid = (1 << (n - 1)) - 1; 
    
    if (k <= mid) {

        return findKthBit(n - 1, k);
    } else if (k === mid + 1) {

        return '1';
    } else {

        return findKthBit(n - 1, (1 << n) - k) === '0' ? '1' : '0';
    }
};

//https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/submissions/1371163443/


```
