```Java []
class Solution {
    public int minimumDifference(int[] array, int target) {
        int arrayLength = array.length;
        int startIndex = -1;
        int currentResult = Math.abs(array[0] - target);
        int orAccumulator = 0;

        for (int endIndex = 0; endIndex < arrayLength; ++endIndex) {
            orAccumulator |= array[endIndex];
            
            if (orAccumulator > target) {
                orAccumulator = 0;
                startIndex = endIndex;
                while ((orAccumulator | array[startIndex]) <= target) {
                    orAccumulator |= array[startIndex--];
                }
            }
            
            if (startIndex != endIndex) {
                currentResult = Math.min(currentResult, Math.abs(orAccumulator - target));
            }
            
            if (startIndex >= 0) {
                currentResult = Math.min(currentResult, Math.abs(target - (orAccumulator | array[startIndex])));
            }
        }

        return currentResult;
    }
}
//Kartikdevsharmaa
```

```C++ []
class Solution {
public:
    int minimumDifference(std::vector<int>& array, int target) {
        int arrayLength = array.size();
        int startIndex = -1;
        int currentResult = std::abs(array[0] - target);
        int orAccumulator = 0;

        for (int endIndex = 0; endIndex < arrayLength; ++endIndex) {
            orAccumulator |= array[endIndex];
            
            if (orAccumulator > target) {
                orAccumulator = 0;
                startIndex = endIndex;
                while ((orAccumulator | array[startIndex]) <= target) {
                    orAccumulator |= array[startIndex--];
                }
            }
            
            if (startIndex != endIndex) {
                currentResult = std::min(currentResult, std::abs(orAccumulator - target));
            }
            
            if (startIndex >= 0) {
                currentResult = std::min(currentResult, std::abs(target - (orAccumulator | array[startIndex])));
            }
        }

        return currentResult;
    }
};
static const int KDS = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();
//Kartikdevsharmaa
```

```Python []
class Solution:
    def minimumDifference(self, array, target):
        array_length = len(array)
        start_index = -1
        current_result = abs(array[0] - target)
        or_accumulator = 0

        for end_index in range(array_length):
            or_accumulator |= array[end_index]
            
            if or_accumulator > target:
                or_accumulator = 0
                start_index = end_index
                while (or_accumulator | array[start_index]) <= target:
                    or_accumulator |= array[start_index]
                    start_index -= 1
            
            if start_index != end_index:
                current_result = min(current_result, abs(or_accumulator - target))
            
            if start_index >= 0:
                current_result = min(current_result, abs(target - (or_accumulator | array[start_index])))
        
        return current_result

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines) // 2
    results = []

    for i in range(num_test_cases):
        array = json.loads(lines[i*2])
        target = int(lines[i*2 + 1])
        
        result = Solution().minimumDifference(array, target)
        results.append(str(result))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)

#kartikdevsharmaa

```
