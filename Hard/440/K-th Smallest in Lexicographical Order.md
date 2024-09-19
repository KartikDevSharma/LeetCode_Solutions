```Java []

class Solution {
    public int findKthNumber(int n, int k) {
        int curr = 1;
        k--;
        while (k > 0) {
            long steps = getSteps(n, curr);
            if (steps <= k) {
                k -= steps;
                curr++;
            } else {
                curr *= 10;
                k--;
            }
        }
        return curr;
    }

    private long getSteps(long n, long curr) {
        long steps = 0;
        long next = curr + 1;
        while (curr <= n) {
            steps += Math.min(n + 1, next) - curr;
            if (steps > Integer.MAX_VALUE) break;  // Early termination
            curr *= 10;
            next *= 10;
        }
        return steps;
    }
}
```
```C++ []
class Solution {
public:
    int findKthNumber(int n, int k) {
        int curr = 1;
        while (k > 1) {
            int count = getCount(n, curr);
            if (count < k) {
                k -= count;
                curr++;
            } else {
                k--;
                curr *= 10;
            }
        }
        return curr;
    }

private:
    int getCount(long long n, long long prefix) {
        long long curr = prefix;
        long long next = curr + 1;
        int count = 0;
        
        while (curr <= n) {
            count += (int)min(n + 1LL, next) - curr;
            curr *= 10;
            next *= 10;
        }
        
        return count;
    }
};

```
```Python []
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        while k > 1:
            count = self.getCount(n, curr)
            if count < k:
                k -= count
                curr += 1
            else:
                k -= 1
                curr *= 10
        return curr

    def getCount(self, n: int, prefix: int) -> int:
        curr = prefix
        next = curr + 1
        count = 0
        
        while curr <= n:
            count += min(n + 1, next) - curr
            curr *= 10
            next *= 10
        
        return count

```
```Go []
func findKthNumber(n int, k int) int {
    curr := 1
    for k > 1 {
        count := getCount(n, curr)
        if count < k {
            k -= count
            curr++
        } else {
            k--
            curr *= 10
        }
    }
    return curr
}

func getCount(n int, prefix int) int {
    curr := int64(prefix)
    next := curr + 1
    count := 0
    
    for curr <= int64(n) {
        count += int(min(int64(n) + 1, next) - curr)
        curr *= 10
        next *= 10
    }
    
    return count
}

func min(a, b int64) int64 {
    if a < b {
        return a
    }
    return b
}

```
```Rust []

impl Solution {
    pub fn find_kth_number(n: i32, mut k: i32) -> i32 {
        let mut curr = 1;
        while k > 1 {
            let count = Self::get_count(n as i64, curr as i64);
            if count < k {
                k -= count;
                curr += 1;
            } else {
                k -= 1;
                curr *= 10;
            }
        }
        curr
    }

    fn get_count(n: i64, prefix: i64) -> i32 {
        let mut curr = prefix;
        let mut next = curr + 1;
        let mut count = 0;
        
        while curr <= n {
            count += (std::cmp::min(n + 1, next) - curr) as i32;
            curr *= 10;
            next *= 10;
        }
        
        count
    }
}
```

```JavaScript []
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findKthNumber = function(n, k) {
    let curr = 1;
    while (k > 1) {
        let count = getCount(n, curr);
        if (count < k) {
            k -= count;
            curr++;
        } else {
            k--;
            curr *= 10;
        }
    }
    return curr;
};

/**
 * @param {number} n
 * @param {number} prefix
 * @return {number}
 */
function getCount(n, prefix) {
    let curr = prefix;
    let next = curr + 1;
    let count = 0;
    
    while (curr <= n) {
        count += Math.min(n + 1, next) - curr;
        curr *= 10;
        next *= 10;
    }
    
    return count;
}

```
