```Java []
class Solution {
    public long findMaximumScore(List<Integer> nums) {
        long maxSoFar = 0;
        long totalScore = 0;
        
        for (int i = 0; i < nums.size() - 1; i++) {
            maxSoFar = Math.max(maxSoFar, nums.get(i));
            totalScore += maxSoFar;
        }
        
        return totalScore;
    }
}
```
```C++ []
class Solution {
public:
    long long findMaximumScore(vector<int>& nums) {
        long long maxSoFar = 0;
        long long totalScore = 0;
        
        for (int i = 0; i < nums.size() - 1; i++) {
            maxSoFar = max(maxSoFar, (long long)nums[i]);
            totalScore += maxSoFar;
        }
        
        return totalScore;
    }
};
static const auto kds = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();
```

```Python []
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        max_so_far = 0
        total_score = 0
        
        for num in nums[:-1]: 
            max_so_far = max(max_so_far, num)
            total_score += max_so_far
        
        return total_score

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines)
    results = []

    for i in range(num_test_cases):
        nums = json.loads(lines[i])
        
        result = Solution().findMaximumScore(nums)
        results.append(str(result))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)
```

