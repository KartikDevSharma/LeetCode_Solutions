```Java []
class Solution {
    public int maxWidthRamp(int[] nums) {
        int n = nums.length;
        int[] suffixMax = new int[n];
        suffixMax[n - 1] = nums[n - 1];
        
        // Build suffix max array
        for (int i = n - 2; i >= 0; i--) {
            suffixMax[i] = Math.max(nums[i], suffixMax[i + 1]);
        }
        
        int maxWidth = 0;
        int i = 0, j = 0;
        
        // Two-pointer approach
        while (j < n) {
            if (nums[i] <= suffixMax[j]) {
                maxWidth = Math.max(maxWidth, j - i);
                j++;
            } else {
                i++;
            }
        }
        
        return maxWidth;
    }
}
//KDS
```
```Python []
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        suffix_max = [0] * n
        suffix_max[-1] = nums[-1]
        
      
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(nums[i], suffix_max[i + 1])
        
        max_width = 0
        i = j = 0
        
       
        while j < n:
            if nums[i] <= suffix_max[j]:
                max_width = max(max_width, j - i)
                j += 1
            else:
                i += 1
        
        return max_width

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines)
    results = []

    for i in range(num_test_cases):
        nums = json.loads(lines[i])
        
        result = Solution().maxWidthRamp(nums)
        results.append(str(result))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)
```
```C++ []
class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        int n = nums.size();
        vector<int> suffixMax(n);
        suffixMax[n - 1] = nums[n - 1];
        
        for (int i = n - 2; i >= 0; i--) {
            suffixMax[i] = max(nums[i], suffixMax[i + 1]);
        }
        
        int maxWidth = 0;
        int i = 0, j = 0;
        
       
        while (j < n) {
            if (nums[i] <= suffixMax[j]) {
                maxWidth = max(maxWidth, j - i);
                j++;
            } else {
                i++;
            }
        }
        
        return maxWidth;
    }
};


```
