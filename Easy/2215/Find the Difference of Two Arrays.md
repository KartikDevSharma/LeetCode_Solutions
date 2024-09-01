#### Intuition

First understand that we're dealing with a comparison problem and We need to identify elements that exist in one array but not the other and we need to do this in both directions It's like we're playing a game of "spot the difference" between two sets of numbers. We're told that the arrays can have up to 1000 elements each and the values in these arrays range from -1000 to 1000. This information is important because it tells us about the "universe" we're working in. We're not dealing with an infinite range of numbers, but a finite, manageable set. 
Now, let's think about how one might approach this problem intuitively. The most straightforward way would be to take each element from the first array and check if it exists in the second array. If it doesn't we've found a unique element. Then we'd do the same for the second array. It is simple but would be time-consuming especially for larger arrays.

So can we could somehow "mark" the presence of numbers, Imagine we had a giant board with 2001 slots (representing all possible values from -1000 to 1000) we could go through each array and put a flag in the corresponding slot for each number we encounter. After doing this for both arrays we'd have a visual representation of which numbers appear in which array. This is basically what our approach will do but instead of a physical board we use boolean arrays. It's like creating a fingerprint for each array where each 'true' value in our boolean array represents the presence of a number. Instead of repeatedly searching through arrays we're making a single pass through each array to mark the numbers and then a single pass through our "board" to identify the differences. This method takes advantage of the fact that we know the range of possible values beforehand. 

Consider the potential errors we avoid with this method We don't have to worry about duplicate values in the original arrays because each number regardless of how many times it appears it will only be marked once in our boolean array. This inherently handles the requirement for distinct integers in our output. Moreover, this approach handles edge cases we can transform the problem from a comparison of arbitrary integers to a comparison of fixed positions in boolean arrays. This transformation is what allows us to achieve a linear time complexity.

#### Appraoch







---

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

---

Approach 2
#### Intuition
In our previous solution we used boolean arrays to create a sort of "fingerprint" for each input array While that approach was efficient it had a fixed memory overhead regardless of the input size. What if we could find a way to adapt our solution to be more flexible, especially for cases where the range of numbers might be much larger or unknown?

This appraoch we will use hash sets since we're still trying to efficiently mark the presence of numbers, but now we're doing it in a way that scales with the input size rather than the range of possible values.
We still need a way to quickly check if a number exists in an array. Hash sets provide this capability with average O(1) time complexity for both insertion and lookup operations. Remember, we need to find distinct integers. Hash sets automatically handle this for us by only storing unique values. Unlike our previous approach with boolean arrays, hash sets can handle any range of integer values without requiring us to know the range beforehand. While hash sets do have some overhead, they only grow as large as the number of unique elements in our input arrays, which could be significantly smaller than the full range of possible values.


We start by creating two hash sets, one for each input array. As we populate these sets, we're effectively creating a compressed representation of each array that only contains unique values. This step alone solves part of our problem - identifying distinct integers. Next, we need to find the elements that are in one set but not the other. This is where the power of sets really shines. Set operations like difference or containment checks are typically very efficient. We iterate through the first set, checking for each element if it's not in the second set. If an element passes this test, we've found a number unique to the first array. We do the same process in reverse for the second set.


- Duplicates in the original arrays are automatically dealt with by the sets.
- The order of elements in the original arrays doesn't matter, aligning with the problem's statement that the output order is not important.
- It works equally well for dense or sparse distributions of numbers within the given range.

One might ask, "Why not just use the sets as our final answer?" The reason is that we need to return our result as lists, not sets. This final conversion step ensures we meet the problem's output requirements.

What we did basically is we changed our thought process from "find elements not in the other array" to "find elements not in the other set," which is a more efficient operation. This solution might use more memory than our boolean array approach for small ranges of numbers, but it scales much better for larger or unknown ranges. 


```Java []

public class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        
        for (int num : nums1) set1.add(num);
        for (int num : nums2) set2.add(num);
        
        List<Integer> uniqueToNums1 = new ArrayList<>();
        List<Integer> uniqueToNums2 = new ArrayList<>();
        
        for (int num : set1) {
            if (!set2.contains(num)) uniqueToNums1.add(num);
        }
        
        for (int num : set2) {
            if (!set1.contains(num)) uniqueToNums2.add(num);
        }
        
        return Arrays.asList(uniqueToNums1, uniqueToNums2);
    }
}
```
```C++ []
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1(nums1.begin(), nums1.end());
        unordered_set<int> set2(nums2.begin(), nums2.end());
        
        vector<int> uniqueToNums1;
        vector<int> uniqueToNums2;
        
        for (int num : set1) {
            if (set2.find(num) == set2.end()) {
                uniqueToNums1.push_back(num);
            }
        }
        
        for (int num : set2) {
            if (set1.find(num) == set1.end()) {
                uniqueToNums2.push_back(num);
            }
        }
        
        return {uniqueToNums1, uniqueToNums2};
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
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        uniqueToNums1 = [num for num in set1 if num not in set2]
        uniqueToNums2 = [num for num in set2 if num not in set1]
        
        return [uniqueToNums1, uniqueToNums2]
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

---

#### Approach 3


```Java []
class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        long[] bitSet1 = new long[32];  // Can handle numbers from -1000 to 1000
        long[] bitSet2 = new long[32];
        List<List<Integer>> result = Arrays.asList(new ArrayList<>(), new ArrayList<>());

        for (int num : nums1) {
            int idx = (num + 1000) / 64;
            long bit = 1L << ((num + 1000) % 64);
            bitSet1[idx] |= bit;
        }

        for (int num : nums2) {
            int idx = (num + 1000) / 64;
            long bit = 1L << ((num + 1000) % 64);
            bitSet2[idx] |= bit;
        }

        for (int i = 0; i < 32; i++) {
            long uniqueToNums1 = bitSet1[i] & ~bitSet2[i];
            long uniqueToNums2 = bitSet2[i] & ~bitSet1[i];

            for (int j = 0; j < 64; j++) {
                if ((uniqueToNums1 & (1L << j)) != 0) {
                    result.get(0).add(i * 64 + j - 1000);
                }
                if ((uniqueToNums2 & (1L << j)) != 0) {
                    result.get(1).add(i * 64 + j - 1000);
                }
            }
        }

        return result;
    }
}
```
```C++ []
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        const int BIT_SIZE = 64;
        const int OFFSET = 1000;
        const int ARRAY_SIZE = 32;
        
        bitset<ARRAY_SIZE * BIT_SIZE> bitSet1, bitSet2;
        
        // Fill bitset for nums1
        for (int num : nums1) {
            int idx = (num + OFFSET) / BIT_SIZE;
            int bit = (num + OFFSET) % BIT_SIZE;
            bitSet1.set(idx * BIT_SIZE + bit);
        }
        
        // Fill bitset for nums2
        for (int num : nums2) {
            int idx = (num + OFFSET) / BIT_SIZE;
            int bit = (num + OFFSET) % BIT_SIZE;
            bitSet2.set(idx * BIT_SIZE + bit);
        }
        
        vector<int> uniqueToNums1, uniqueToNums2;
        
        // Check unique elements for nums1
        for (int i = 0; i < ARRAY_SIZE * BIT_SIZE; ++i) {
            if (bitSet1[i] && !bitSet2[i]) {
                uniqueToNums1.push_back(i - OFFSET);
            }
        }
        
        // Check unique elements for nums2
        for (int i = 0; i < ARRAY_SIZE * BIT_SIZE; ++i) {
            if (bitSet2[i] && !bitSet1[i]) {
                uniqueToNums2.push_back(i - OFFSET);
            }
        }
        
        return {uniqueToNums1, uniqueToNums2};
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
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        BIT_SIZE = 64
        OFFSET = 1000
        ARRAY_SIZE = 32
        
        bitSet1 = [0] * ARRAY_SIZE
        bitSet2 = [0] * ARRAY_SIZE
        
        # Fill bitset for nums1
        for num in nums1:
            idx = (num + OFFSET) // BIT_SIZE
            bit = (num + OFFSET) % BIT_SIZE
            bitSet1[idx] |= (1 << bit)
        
        # Fill bitset for nums2
        for num in nums2:
            idx = (num + OFFSET) // BIT_SIZE
            bit = (num + OFFSET) % BIT_SIZE
            bitSet2[idx] |= (1 << bit)
        
        uniqueToNums1 = []
        uniqueToNums2 = []
        
        # Check unique elements for nums1
        for i in range(ARRAY_SIZE):
            uniqueToNums1Bits = bitSet1[i] & ~bitSet2[i]
            for j in range(BIT_SIZE):
                if uniqueToNums1Bits & (1 << j):
                    uniqueToNums1.append(i * BIT_SIZE + j - OFFSET)
        
        # Check unique elements for nums2
        for i in range(ARRAY_SIZE):
            uniqueToNums2Bits = bitSet2[i] & ~bitSet1[i]
            for j in range(BIT_SIZE):
                if uniqueToNums2Bits & (1 << j):
                    uniqueToNums2.append(i * BIT_SIZE + j - OFFSET)
        
        return [uniqueToNums1, uniqueToNums2]

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
