
### Complexity
- **Time complexity:$O(n)$**

> For Finding minNum and maxNum: O(n) For Creating and populating the frequency array: O(n) and in the sliding window operation it might appear to be O(r) (r is range) at first but, it's actually O(n) in the worst case because the total number of operations (incrementing windowEnd, incrementing windowStart, updating currentCount, etc.) is bounded by the number of elements in the original array.
- **Space complexity: $O(n)$**
>The frequency array requires space proportional to the range [minNum, maxNum], which in the worst case can be O(n).


# Code
```Java []
//5-ms
class Solution {
    public int maxFrequency(int[] nums, int k) {
        int minNum = Integer.MAX_VALUE;
        int maxNum = 0;
        for (int num : nums) {
            minNum = Math.min(minNum, num);
            maxNum = Math.max(maxNum, num);
        }
        int range = maxNum - minNum + 1;
        int[] frequency = new int[range];
        
        for (int num : nums) {
            frequency[num - minNum]++;
        }
        int windowStart = 0, operationsUsed = 0, maxFreq = 0, currentCount = 0, windowStartCount = frequency[0];
        for (int windowEnd = 0; windowEnd < range; ++windowEnd) {
            operationsUsed += currentCount;
            currentCount += frequency[windowEnd];
            while (operationsUsed > k) {
                while (windowStartCount == 0) windowStartCount = frequency[++windowStart];
                operationsUsed -= windowEnd - windowStart;
                windowStartCount--;
                currentCount--;
            }
            maxFreq = Math.max(maxFreq, currentCount);
        }
        return maxFreq;
    }
}

//https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/1365038981/
```
```C++ []
//50-ms
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        int minNum = *min_element(nums.begin(), nums.end());
        int maxNum = *max_element(nums.begin(), nums.end());
        int range = maxNum - minNum + 1;
        vector<int> frequency(range, 0);
        
        for (int num : nums) {
            frequency[num - minNum]++;
        }
        
        int windowStart = 0, operationsUsed = 0, maxFreq = 0, currentCount = 0, windowStartCount = frequency[0];
        for (int windowEnd = 0; windowEnd < range; ++windowEnd) {
            operationsUsed += currentCount;
            currentCount += frequency[windowEnd];
            while (operationsUsed > k) {
                while (windowStartCount == 0) windowStartCount = frequency[++windowStart];
                operationsUsed -= windowEnd - windowStart;
                windowStartCount--;
                currentCount--;
            }
            maxFreq = max(maxFreq, currentCount);
        }
        return maxFreq;
    }
};
static const int speedup = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();


//https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/1365045529/
```
```Python []
#200-ms
class Solution:
    def maxFrequency(self, nums, k):
        min_num = min(nums)
        max_num = max(nums)
        range_size = max_num - min_num + 1
        frequency = [0] * range_size
        for num in nums:
            frequency[num - min_num] += 1
        
        window_start = operations_used = max_freq = current_count = 0
        window_start_count = frequency[0]
        for window_end in range(range_size):
            operations_used += current_count
            current_count += frequency[window_end]
            while operations_used > k:
                while window_start_count == 0:
                    window_start += 1
                    window_start_count = frequency[window_start]
                operations_used -= window_end - window_start
                window_start_count -= 1
                current_count -= 1
            max_freq = max(max_freq, current_count)
        return max_freq

with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(Solution().maxFrequency(nums, next(inputs)), file=f)
exit(0)


#https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/1365057533/
```
```Go []
//100-ms
func maxFrequency(nums []int, k int) int {
    minNum, maxNum := nums[0], nums[0]
    for _, num := range nums {
        if num < minNum {
            minNum = num
        }
        if num > maxNum {
            maxNum = num
        }
    }
    
    rangeSize := maxNum - minNum + 1
    frequency := make([]int, rangeSize)
    
    for _, num := range nums {
        frequency[num-minNum]++
    }
    
    windowStart, operationsUsed, maxFreq, currentCount := 0, 0, 0, 0
    windowStartCount := frequency[0]
    
    for windowEnd := 0; windowEnd < rangeSize; windowEnd++ {
        operationsUsed += currentCount
        currentCount += frequency[windowEnd]
        for operationsUsed > k {
            for windowStartCount == 0 {
                windowStart++
                windowStartCount = frequency[windowStart]
            }
            operationsUsed -= windowEnd - windowStart
            windowStartCount--
            currentCount--
        }
        if currentCount > maxFreq {
            maxFreq = currentCount
        }
    }
    return maxFreq
}

func notmain() {
    scanner := bufio.NewScanner(os.Stdin)
    writer := bufio.NewWriter(os.Stdout)
    defer writer.Flush()

    for scanner.Scan() {
        var nums []int
        json.Unmarshal([]byte(scanner.Text()), &nums)

        scanner.Scan()
        var k int
        json.Unmarshal([]byte(scanner.Text()), &k)

        result := maxFrequency(nums, k)
        fmt.Fprintln(writer, result)
    }
}


//https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/1365061200/
```
```JavaScript []
//85-ms
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxFrequency = function(nums, k) {
    const minNum = Math.min(...nums);
    const maxNum = Math.max(...nums);
    const range = maxNum - minNum + 1;
    const frequency = new Array(range).fill(0);
    
    for (const num of nums) {
        frequency[num - minNum]++;
    }
    
    let windowStart = 0, operationsUsed = 0, maxFreq = 0, currentCount = 0, windowStartCount = frequency[0];
    for (let windowEnd = 0; windowEnd < range; ++windowEnd) {
        operationsUsed += currentCount;
        currentCount += frequency[windowEnd];
        while (operationsUsed > k) {
            while (windowStartCount === 0) windowStartCount = frequency[++windowStart];
            operationsUsed -= windowEnd - windowStart;
            windowStartCount--;
            currentCount--;
        }
        maxFreq = Math.max(maxFreq, currentCount);
    }
    return maxFreq;
};




//https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/1365068928/
```
```rust []
impl Solution {
    pub fn max_frequency(nums: Vec<i32>, k: i32) -> i32 {
        let min_num = *nums.iter().min().unwrap();
        let max_num = *nums.iter().max().unwrap();
        let range = (max_num - min_num + 1) as usize;
        let mut frequency = vec![0; range];
        
        for &num in &nums {
            frequency[(num - min_num) as usize] += 1;
        }
        
        let mut window_start = 0;
        let mut operations_used = 0i64;  // Changed to i64 to avoid overflow
        let mut max_freq = 0;
        let mut current_count = 0;
        let mut window_start_count = frequency[0];
        
        for window_end in 0..range {
            operations_used += current_count as i64;
            current_count += frequency[window_end];
            while operations_used > k as i64 {
                while window_start_count == 0 {
                    window_start += 1;
                    window_start_count = frequency[window_start];
                }
                operations_used -= (window_end - window_start) as i64;
                window_start_count -= 1;
                current_count -= 1;
            }
            max_freq = max_freq.max(current_count);
        }
        max_freq
    }
}

//https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/1365037885/
```
