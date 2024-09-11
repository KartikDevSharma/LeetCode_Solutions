```Java []
class Solution {
    public int getXORSum(int[] arr1, int[] arr2) {
        return xorArray(arr1) & xorArray(arr2);
    }

    private int xorArray(int[] arr) {
        int xor = 0;
        for (int num : arr) {
            xor ^= num;
        }
        return xor;
    }
}
//Kartikdevsharmaa

```
```C++ []
class Solution {
public:
    int getXORSum(vector<int>& arr1, vector<int>& arr2) {
        return xorArray(arr1) & xorArray(arr2);
    }

private:
    int xorArray(vector<int>& arr) {
        int xorResult = 0;
        for (int num : arr) {
            xorResult ^= num;
        }
        return xorResult;
    }
};
//Kartikdevsharmaa
```

```Python []
class Solution:
    def getXORSum(self, arr1, arr2):
        return self.xorArray(arr1) & self.xorArray(arr2)
    
    def xorArray(self, arr):
        xor = 0
        for num in arr:
            xor ^= num
        return xor

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines) // 2
    results = []

    for i in range(num_test_cases):
        arr1 = json.loads(lines[i*2])
        arr2 = json.loads(lines[i*2 + 1])
        
        result = Solution().getXORSum(arr1, arr2)
        results.append(str(result))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)


# kartikdevsharmaa
```
