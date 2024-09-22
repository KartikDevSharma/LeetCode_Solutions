```Java []
class Solution {
    public boolean canArrange(int[] arr, int k) {
        int[] freq = new int[k];
        
        for (int num : arr) {
            freq[((num % k) + k) % k]++;
        }
        
        if (freq[0] % 2 != 0) return false;
        
        for (int i = 1; i <= k / 2; i++) {
            if (freq[i] != freq[k - i]) return false;
        }
        
        return true;
    }
}
//KDS

```
```C++ []
class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> freq(k, 0);
        
        for (int num : arr) {
            freq[(num % k + k) % k]++;
        }
        
        if (freq[0] % 2 != 0) return false;
        
        for (int i = 1; i <= k / 2; i++) {
            if (freq[i] != freq[k - i]) return false;
        }
        
        return true;
    }
};
static const int KDS = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();
//KDS

```
```Python []
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k
        
        for num in arr:
            freq[(num % k + k) % k] += 1
        
        if freq[0] % 2 != 0:
            return False
        
        for i in range(1, k // 2 + 1):
            if freq[i] != freq[k - i]:
                return False
        
        return True


```
```Go []
func canArrange(arr []int, k int) bool {
    freq := make([]int, k)
    
    for _, num := range arr {
        freq[((num % k) + k) % k]++
    }
    
    if freq[0] % 2 != 0 {
        return false
    }
    
    for i := 1; i <= k / 2; i++ {
        if freq[i] != freq[k - i] {
            return false
        }
    }
    
    return true
}

```
```Rust []
impl Solution {
    pub fn can_arrange(arr: Vec<i32>, k: i32) -> bool {
        let mut freq = vec![0; k as usize];
        
        for num in arr {
            freq[((num % k + k) % k) as usize] += 1;
        }
        
        if freq[0] % 2 != 0 {
            return false;
        }
        
        for i in 1..=k / 2 {
            if freq[i as usize] != freq[(k - i) as usize] {
                return false;
            }
        }
        
        true
    }
}

```
```JavaScript []
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {boolean}
 */
var canArrange = function(arr, k) {
    const freq = new Array(k).fill(0);
    
    for (const num of arr) {
        freq[((num % k) + k) % k]++;
    }
    
    if (freq[0] % 2 !== 0) return false;
    
    for (let i = 1; i <= k / 2; i++) {
        if (freq[i] !== freq[k - i]) return false;
    }
    
    return true;
};
//KDS

```
