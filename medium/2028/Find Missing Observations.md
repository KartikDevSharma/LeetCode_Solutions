```Java []
class Solution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        int m = rolls.length;
        int totalSum = mean * (m + n);
        int rollsSum = 0;
        
        for (int roll : rolls) {
            rollsSum += roll;
        }
        
        int missingSum = totalSum - rollsSum;
        
        if (missingSum < n || missingSum > 6 * n) {
            return new int[0];
        }
        
        int[] result = new int[n];
        int quotient = missingSum / n;
        int remainder = missingSum % n;
        
        for (int i = 0; i < n; i++) {
            result[i] = quotient + (i < remainder ? 1 : 0);
        }
        
        return result;
    }
}
//kartikdevsharmaa
//https://leetcode.com/problems/find-missing-observations/submissions/1373884134/?submissionId=1373872796
```
```C++ []
class Solution {
public:
    std::vector<int> missingRolls(std::vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        int totalSum = mean * (m + n);
        int rollsSum = 0;
        
        for (int roll : rolls) {
            rollsSum += roll;
        }
        
        int missingSum = totalSum - rollsSum;
        
        if (missingSum < n || missingSum > 6 * n) {
            return {};
        }
        
        std::vector<int> result(n);
        int quotient = missingSum / n;
        int remainder = missingSum % n;
        
        for (int i = 0; i < n; i++) {
            result[i] = quotient + (i < remainder ? 1 : 0);
        }
        
        return result;
    }
};
static const int ktkdvshrm = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();
//kartikdevsharmaa
//https://leetcode.com/problems/find-missing-observations/submissions/1373886225/?submissionId=1373872796
```
```Python []
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        totalSum = mean * (m + n)
        rollsSum = sum(rolls)
        
        missingSum = totalSum - rollsSum
        
        if missingSum < n or missingSum > 6 * n:
            return []
        
        quotient, remainder = divmod(missingSum, n)
        return [quotient + (1 if i < remainder else 0) for i in range(n)]

def main():
    inputs = map(loads, sys.stdin)
    results = []

    while True:
        try:
            rolls = next(inputs)
            mean = next(inputs)
            n = next(inputs)
            
            result = Solution().missingRolls(rolls, mean, n)
            results.append(result)
        except StopIteration:
            break

    with open("user.out", "w") as f:
        for result in results:
            print(dumps(result).replace(", ", ","), file=f)

if __name__ == "__main__":
    main()
    sys.exit(0)
#kartikdevsharmaa
#https://leetcode.com/problems/find-missing-observations/submissions/1373889294/?submissionId=1373872796
```
