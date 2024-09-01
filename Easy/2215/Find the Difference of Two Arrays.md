```Java []
class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        final int VALUE_RANGE = 2001;
        final int MIN_VALUE = -1000;
        
        boolean[] presentInNums1 = new boolean[VALUE_RANGE];
        boolean[] presentInNums2 = new boolean[VALUE_RANGE];
        
        for (int num : nums1) presentInNums1[num - MIN_VALUE] = true;
        for (int num : nums2) presentInNums2[num - MIN_VALUE] = true;
        
        List<List<Integer>> uniqueElements = Arrays.asList(new ArrayList<>(), new ArrayList<>());
        
        for (int i = 0; i < VALUE_RANGE; i++) {
            if (presentInNums1[i] && !presentInNums2[i]) uniqueElements.get(0).add(i + MIN_VALUE);
            if (presentInNums2[i] && !presentInNums1[i]) uniqueElements.get(1).add(i + MIN_VALUE);
        }
        
        return uniqueElements;
    }
}
```
```C++ []
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        constexpr int VALUE_RANGE = 2001;
        constexpr int MIN_VALUE = -1000;
        
        array<bool, VALUE_RANGE> presentInNums1{}, presentInNums2{};
        
        for (int num : nums1) presentInNums1[num - MIN_VALUE] = true;
        for (int num : nums2) presentInNums2[num - MIN_VALUE] = true;
        
        vector<vector<int>> uniqueElements(2);
        uniqueElements[0].reserve(nums1.size());
        uniqueElements[1].reserve(nums2.size());
        
        for (int i = 0; i < VALUE_RANGE; ++i) {
            if (presentInNums1[i] && !presentInNums2[i]) uniqueElements[0].push_back(i + MIN_VALUE);
            if (presentInNums2[i] && !presentInNums1[i]) uniqueElements[1].push_back(i + MIN_VALUE);
        }
        
        return uniqueElements;
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
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        VALUE_RANGE = 2001
        MIN_VALUE = -1000
        
        present_in_nums1 = [False] * VALUE_RANGE
        present_in_nums2 = [False] * VALUE_RANGE
        
        for num in nums1:
            present_in_nums1[num - MIN_VALUE] = True
        for num in nums2:
            present_in_nums2[num - MIN_VALUE] = True
        
        unique_elements = [[], []]
        
        for i in range(VALUE_RANGE):
            if present_in_nums1[i] and not present_in_nums2[i]:
                unique_elements[0].append(i + MIN_VALUE)
            if present_in_nums2[i] and not present_in_nums1[i]:
                unique_elements[1].append(i + MIN_VALUE)
        
        return unique_elements

def format_output(result):
    return '[' + ','.join(str(row).replace(' ', '') for row in result) + ']'

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    num_test_cases = len(lines) // 2
    results = []
    
    for i in range(num_test_cases):
        nums1 = json.loads(lines[i*2])
        nums2 = json.loads(lines[i*2 + 1])
        result = Solution().findDifference(nums1, nums2)
        formatted_result = format_output(result)
        results.append(formatted_result)
    
    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    sys.exit(0)
```
```Go []
func findDifference(nums1 []int, nums2 []int) [][]int {
    const VALUE_RANGE = 2001
    const MIN_VALUE = -1000
    
    presentInNums1 := make([]bool, VALUE_RANGE)
    presentInNums2 := make([]bool, VALUE_RANGE)
    
    for _, num := range nums1 {
        presentInNums1[num - MIN_VALUE] = true
    }
    for _, num := range nums2 {
        presentInNums2[num - MIN_VALUE] = true
    }
    
    uniqueElements := make([][]int, 2)
    
    for i := 0; i < VALUE_RANGE; i++ {
        if presentInNums1[i] && !presentInNums2[i] {
            uniqueElements[0] = append(uniqueElements[0], i + MIN_VALUE)
        }
        if presentInNums2[i] && !presentInNums1[i] {
            uniqueElements[1] = append(uniqueElements[1], i + MIN_VALUE)
        }
    }
    
    return uniqueElements
}
```
```Rust []
impl Solution {
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> {
        const VALUE_RANGE: usize = 2001;
        const MIN_VALUE: i32 = -1000;
        
        let mut present_in_nums1 = [false; VALUE_RANGE];
        let mut present_in_nums2 = [false; VALUE_RANGE];
        
        nums1.iter().for_each(|&num| present_in_nums1[(num - MIN_VALUE) as usize] = true);
        nums2.iter().for_each(|&num| present_in_nums2[(num - MIN_VALUE) as usize] = true);
        
        let mut unique_elements = vec![Vec::new(), Vec::new()];
        
        for i in 0..VALUE_RANGE {
            if present_in_nums1[i] && !present_in_nums2[i] {
                unique_elements[0].push(i as i32 + MIN_VALUE);
            }
            if present_in_nums2[i] && !present_in_nums1[i] {
                unique_elements[1].push(i as i32 + MIN_VALUE);
            }
        }
        
        unique_elements
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    const VALUE_RANGE = 2001;
    const MIN_VALUE = -1000;
    
    const presentInNums1 = new Array(VALUE_RANGE).fill(false);
    const presentInNums2 = new Array(VALUE_RANGE).fill(false);
    
    nums1.forEach(num => presentInNums1[num - MIN_VALUE] = true);
    nums2.forEach(num => presentInNums2[num - MIN_VALUE] = true);
    
    const uniqueElements = [[], []];
    
    for (let i = 0; i < VALUE_RANGE; i++) {
        if (presentInNums1[i] && !presentInNums2[i]) uniqueElements[0].push(i + MIN_VALUE);
        if (presentInNums2[i] && !presentInNums1[i]) uniqueElements[1].push(i + MIN_VALUE);
    }
    
    return uniqueElements;
};
```
