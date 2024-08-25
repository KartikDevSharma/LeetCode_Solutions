

# Complexity
- Time complexity:$O(n)$


- Space complexity:$O(1)$


# Code
```Java []
public class Solution {
       private static final int MAX_THRESHOLD = 1000000000;

       public int maxProduct(int[] nums) {
           long maxProduct = Integer.MIN_VALUE;
           maxProduct = Math.max(maxProduct, scanArray(nums, true));
           maxProduct = Math.max(maxProduct, scanArray(nums, false));
           return (int) maxProduct;
       }

       private long scanArray(int[] nums, boolean leftToRight) {
           long currentProduct = 1;
           long maxProduct = Integer.MIN_VALUE;
           
           for (int i = 0; i < nums.length; i++) {
               int index = leftToRight ? i : nums.length - 1 - i;
               
               if (nums[index] == 0) {
                   maxProduct = Math.max(maxProduct, 0);
                   currentProduct = 1;
                   continue;
               }
               
               currentProduct *= nums[index];
               maxProduct = Math.max(maxProduct, currentProduct);
               
               if (maxProduct >= MAX_THRESHOLD) {
                   return maxProduct;
               }
           }
           
           return maxProduct;
       }
   }



//https://leetcode.com/problems/maximum-product-subarray/submissions/1365422942/
```
```cpp []
class Solution {
   private:
       static const int MAX_THRESHOLD = 1000000000;

       long long scanArray(vector<int>& nums, bool leftToRight) {
           long long currentProduct = 1;
           long long maxProduct = INT_MIN;
           
           for (int i = 0; i < nums.size(); i++) {
               int index = leftToRight ? i : nums.size() - 1 - i;
               
               if (nums[index] == 0) {
                   maxProduct = max(maxProduct, 0LL);
                   currentProduct = 1;
                   continue;
               }
               
               currentProduct *= nums[index];
               maxProduct = max(maxProduct, currentProduct);
               
               if (maxProduct >= MAX_THRESHOLD) {
                   return maxProduct;
               }
           }
           
           return maxProduct;
       }

   public:
       int maxProduct(vector<int>& nums) {
           long long maxProduct = INT_MIN;
           maxProduct = max(maxProduct, scanArray(nums, true));
           maxProduct = max(maxProduct, scanArray(nums, false));
           return static_cast<int>(maxProduct);
       }
   };

static const int speedup = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();


////https://leetcode.com/problems/maximum-product-subarray/submissions/1365426384/
```

```Python []
class Solution:
    MAX_THRESHOLD = 1000000000

    def maxProduct(self, nums: List[int]) -> int:
        max_product = float('-inf')
        max_product = max(max_product, self.scanArray(nums, True))
        max_product = max(max_product, self.scanArray(nums, False))
        return int(max_product)

    def scanArray(self, nums: List[int], left_to_right: bool) -> int:
        current_product = 1
        max_product = float('-inf')
        
        for i in range(len(nums)):
            index = i if left_to_right else len(nums) - 1 - i
            
            if nums[index] == 0:
                max_product = max(max_product, 0)
                current_product = 1
                continue
            
            current_product *= nums[index]
            max_product = max(max_product, current_product)
            
            if max_product >= self.MAX_THRESHOLD:
                return max_product
        
        return max_product

with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(Solution().maxProduct(nums), file=f)

exit(0)



#https://leetcode.com/problems/maximum-product-subarray/submissions/1365433653/
```

```Go []

const MAX_THRESHOLD = 1000000000

func maxProduct(nums []int) int {
	maxProduct := int64(-1 << 31)
	maxProduct = max64(maxProduct, scanArray(nums, true))
	maxProduct = max64(maxProduct, scanArray(nums, false))
	return int(maxProduct)
}

func scanArray(nums []int, leftToRight bool) int64 {
	currentProduct := int64(1)
	maxProduct := int64(-1 << 31)
	for i := 0; i < len(nums); i++ {
		index := i
		if !leftToRight {
			index = len(nums) - 1 - i
		}
		if nums[index] == 0 {
			maxProduct = max64(maxProduct, 0)
			currentProduct = 1
			continue
		}
		currentProduct *= int64(nums[index])
		maxProduct = max64(maxProduct, currentProduct)
		if maxProduct >= MAX_THRESHOLD {
			return maxProduct
		}
	}
	return maxProduct
}

func max64(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func notmain() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	var n int
	if scanner.Scan() {
		n, _ = strconv.Atoi(scanner.Text())
	}

	nums := make([]int, n)
	for i := 0; i < n; i++ {
		if scanner.Scan() {
			nums[i], _ = strconv.Atoi(scanner.Text())
		}
	}

	result := maxProduct(nums)
	fmt.Println(result)
}



//https://leetcode.com/problems/maximum-product-subarray/submissions/1365439702/
```
```Rust []
const MAX_THRESHOLD: i64 = 1_000_000_000;

impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut max_product = i32::MIN as i64;
        max_product = max_product.max(Self::scan_array(&nums, true));
        max_product = max_product.max(Self::scan_array(&nums, false));
        max_product as i32
    }
    
    fn scan_array(nums: &Vec<i32>, left_to_right: bool) -> i64 {
        let mut current_product = 1i64;
        let mut max_product = i32::MIN as i64;
        for i in 0..nums.len() {
            let index = if left_to_right { i } else { nums.len() - 1 - i };
            if nums[index] == 0 {
                max_product = max_product.max(0);
                current_product = 1;
                continue;
            }
            current_product *= nums[index] as i64;
            max_product = max_product.max(current_product);
            if max_product >= MAX_THRESHOLD {
                return max_product;
            }
        }
        max_product
    }
}
https://leetcode.com/problems/maximum-product-subarray/submissions/1365436968/

```

```JavaScript []
const MAX_THRESHOLD = 1000000000;

var maxProduct = function(nums) {
    let maxProduct = Number.MIN_SAFE_INTEGER;
    maxProduct = Math.max(maxProduct, scanArray(nums, true));
    maxProduct = Math.max(maxProduct, scanArray(nums, false));
    return maxProduct;
};

function scanArray(nums, leftToRight) {
    let currentProduct = 1;
    let maxProduct = Number.MIN_SAFE_INTEGER;
    for (let i = 0; i < nums.length; i++) {
        const index = leftToRight ? i : nums.length - 1 - i;
        if (nums[index] === 0) {
            maxProduct = Math.max(maxProduct, 0);
            currentProduct = 1;
            continue;
        }
        currentProduct *= nums[index];
        maxProduct = Math.max(maxProduct, currentProduct);
        if (maxProduct >= MAX_THRESHOLD) {
            return maxProduct;
        }
    }
    return maxProduct;
}

```
