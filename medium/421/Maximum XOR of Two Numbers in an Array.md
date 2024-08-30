```Java []
class Solution {
    public int findMaximumXOR(int[] nums) {
        int maxNum = findMaxNumber(nums);
        int msbPosition = findMostSignificantBitPosition(maxNum);
        
        return buildMaximumXOR(nums, msbPosition);
    }
    
    private int findMaxNumber(int[] nums) {
        int max = 0;
        for (int num : nums) {
            max = Math.max(max, num);
        }
        return max;
    }
    
    private int findMostSignificantBitPosition(int num) {
        for (int i = 31; i >= 0; i--) {
            if ((num & (1 << i)) != 0) {
                return i;
            }
        }
        return 0;
    }
    
    private int buildMaximumXOR(int[] nums, int msbPosition) {
        int result = 0;
        int prefixMask = 0;
        Set<Integer> prefixes = new HashSet<>();
        
        for (int i = msbPosition; i >= 0; i--) {
            prefixMask |= (1 << i);
            
            int candidateResult = result | (1 << i);
            prefixes.clear();
            
            for (int num : nums) {
                int prefix = num & prefixMask;
                if (prefixes.contains(candidateResult ^ prefix)) {
                    result = candidateResult;
                    break;
                }
                prefixes.add(prefix);
            }
        }
        
        return result;
    }
}


//Stolen From Kartikdevsharmaa
//https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/submissions/1373351209/

```
```C++ []
class Solution {
public:
    int findMaximumXOR(std::vector<int>& nums) {
        int maxNum = *std::max_element(nums.begin(), nums.end());
        int msbPosition = findMostSignificantBitPosition(maxNum);
        
        return buildMaximumXOR(nums, msbPosition);
    }
    
private:
    int findMostSignificantBitPosition(int num) {
        for (int i = 31; i >= 0; --i) {
            if ((num & (1 << i)) != 0) {
                return i;
            }
        }
        return 0;
    }
    
    int buildMaximumXOR(const std::vector<int>& nums, int msbPosition) {
        int result = 0;
        int prefixMask = 0;
        std::unordered_set<int> prefixes;
        
        for (int i = msbPosition; i >= 0; --i) {
            prefixMask |= (1 << i);
            
            int candidateResult = result | (1 << i);
            prefixes.clear();
            
            for (int num : nums) {
                int prefix = num & prefixMask;
                if (prefixes.count(candidateResult ^ prefix)) {
                    result = candidateResult;
                    break;
                }
                prefixes.insert(prefix);
            }
        }
        
        return result;
    }
};

static const auto pplwilovrlk = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();

//Stolen From Kartikdevsharmaa
//https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/submissions/1373356090/

```
```Python []
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def find_most_significant_bit_position(num: int) -> int:
            for i in range(31, -1, -1):
                if num & (1 << i):
                    return i
            return 0

        def build_maximum_xor(nums: List[int], msb_position: int) -> int:
            result = 0
            prefix_mask = 0
            
            for i in range(msb_position, -1, -1):
                prefix_mask |= (1 << i)
                
                candidate_result = result | (1 << i)
                prefixes = set()
                
                for num in nums:
                    prefix = num & prefix_mask
                    if candidate_result ^ prefix in prefixes:
                        result = candidate_result
                        break
                    prefixes.add(prefix)
            
            return result

        max_num = max(nums)
        msb_position = find_most_significant_bit_position(max_num)
        
        return build_maximum_xor(nums, msb_position)

def main():
    input_data = sys.stdin.read().strip()
    test_cases = input_data.splitlines()
    results = []

    for case in test_cases:
        nums = json.loads(case)
        results.append(Solution().findMaximumXOR(nums))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()
    exit(0)

#Stolen From Kartikdevsharmaa        
#https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/submissions/1373341712/

```
```Go []
func findMaximumXOR(nums []int) int {
    findMaxNumber := func(nums []int) int {
        max := 0
        for _, num := range nums {
            if num > max {
                max = num
            }
        }
        return max
    }

    findMostSignificantBitPosition := func(num int) int {
        for i := 31; i >= 0; i-- {
            if (num & (1 << i)) != 0 {
                return i
            }
        }
        return 0
    }

    buildMaximumXOR := func(nums []int, msbPosition int) int {
        result := 0
        prefixMask := 0
        prefixes := make(map[int]bool)

        for i := msbPosition; i >= 0; i-- {
            prefixMask |= (1 << i)
            
            candidateResult := result | (1 << i)
            for k := range prefixes {
                delete(prefixes, k)
            }
            
            for _, num := range nums {
                prefix := num & prefixMask
                if prefixes[candidateResult ^ prefix] {
                    result = candidateResult
                    break
                }
                prefixes[prefix] = true
            }
        }
        
        return result
    }

    maxNum := findMaxNumber(nums)
    msbPosition := findMostSignificantBitPosition(maxNum)
    
    return buildMaximumXOR(nums, msbPosition)
}

func pplovrlkmain() {
    scanner := bufio.NewScanner(os.Stdin)
    var results []int

    for scanner.Scan() {
        line := scanner.Text()
        var nums []int
        json.Unmarshal([]byte(line), &nums)
        results = append(results, findMaximumXOR(nums))
    }

    file, _ := os.Create("user.out")
    defer file.Close()

    for _, result := range results {
        fmt.Fprintln(file, result)
    }
}

//Stolen From Kartikdevsharmaa
//https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/submissions/1373344625/

```
```Rust []
impl Solution {
    pub fn find_maximum_xor(nums: Vec<i32>) -> i32 {
        let max_num = *nums.iter().max().unwrap();
        let msb_position = Self::find_most_significant_bit_position(max_num);
        
        Self::build_maximum_xor(&nums, msb_position)
    }
    
    fn find_most_significant_bit_position(num: i32) -> i32 {
        for i in (0..=31).rev() {
            if (num & (1 << i)) != 0 {
                return i;
            }
        }
        0
    }
    
    fn build_maximum_xor(nums: &Vec<i32>, msb_position: i32) -> i32 {
        let mut result = 0;
        let mut prefix_mask = 0;
        let mut prefixes = HashSet::new();
        
        for i in (0..=msb_position).rev() {
            prefix_mask |= 1 << i;
            
            let candidate_result = result | (1 << i);
            prefixes.clear();
            
            for &num in nums {
                let prefix = num & prefix_mask;
                if prefixes.contains(&(candidate_result ^ prefix)) {
                    result = candidate_result;
                    break;
                }
                prefixes.insert(prefix);
            }
        }
        
        result
    }
}

fn pplovrlkmain() -> io::Result<()> {
    let stdin = io::stdin();
    let mut results = Vec::new();

    for line in stdin.lock().lines() {
        let line = line?;
        let nums: Vec<i32> = serde_json::from_str(&line)?;
        results.push(Solution::find_maximum_xor(nums));
    }

    let mut file = File::create("user.out")?;
    for result in results {
        writeln!(file, "{}", result)?;
    }

    Ok(())
}
use std::collections::HashSet;
use std::fs::File;

//Stolen From Kartikdevsharmaa
//https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/submissions/1373347712/

```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaximumXOR = function(nums) {
    const findMaxNumber = (nums) => Math.max(...nums);
    
    const findMostSignificantBitPosition = (num) => {
        for (let i = 31; i >= 0; i--) {
            if ((num & (1 << i)) !== 0) {
                return i;
            }
        }
        return 0;
    };
    
    const buildMaximumXOR = (nums, msbPosition) => {
        let result = 0;
        let prefixMask = 0;
        
        for (let i = msbPosition; i >= 0; i--) {
            prefixMask |= (1 << i);
            
            const candidateResult = result | (1 << i);
            const prefixes = new Set();
            
            for (const num of nums) {
                const prefix = num & prefixMask;
                if (prefixes.has(candidateResult ^ prefix)) {
                    result = candidateResult;
                    break;
                }
                prefixes.add(prefix);
            }
        }
        
        return result;
    };

    const maxNum = findMaxNumber(nums);
    const msbPosition = findMostSignificantBitPosition(maxNum);
    
    return buildMaximumXOR(nums, msbPosition);
};


//Stolen From Kartikdevsharmaa
//https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/submissions/1373358671/

```
