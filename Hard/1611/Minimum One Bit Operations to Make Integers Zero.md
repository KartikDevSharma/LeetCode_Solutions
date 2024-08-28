```Java []
class Solution {
    public int minimumOneBitOperations(int n) {
        int result = n;
        for (int shift = 16; shift > 0; shift /= 2) {
            result ^= result >> shift;
        }
        return result;
    }
}

//https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/submissions/1371165501/
```
```C++ []
class Solution {
public:
    int minimumOneBitOperations(int n) {
        int result = n;
        for (int shift = 16; shift > 0; shift /= 2) {
            result ^= result >> shift;
        }
        return result;
    }
};

//https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/submissions/1371166935/
```
```Python []
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        result = n
        shift = 16
        while shift > 0:
            result ^= result >> shift
            shift //= 2
        return result

```
```Go []
func  minimumOneBitOperations(n int) int {
    result := n
    for shift := 16; shift > 0; shift /= 2 {
        result ^= result >> shift
    }
    return result
}

//https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/submissions/1371168529/

```
```Rust []
impl Solution {
    pub fn minimum_one_bit_operations(n: i32) -> i32 {
        let mut result = n;
        let mut shift = 16;
        while shift > 0 {
            result ^= result >> shift;
            shift /= 2;
        }
        result
    }
}


//https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/submissions/1371169036/
```
