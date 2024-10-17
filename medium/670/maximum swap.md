```Java []
class Solution {
    public int maximumSwap(int num) {
        char[] digits = Integer.toString(num).toCharArray();
        int[] lastIndex = new int[10];
        
        // Store the last occurrence of each digit
        for (int i = 0; i < digits.length; i++) {
            lastIndex[digits[i] - '0'] = i;
        }
        
        // Find the first digit that can be swapped for a larger one
        for (int i = 0; i < digits.length; i++) {
            for (int d = 9; d > digits[i] - '0'; d--) {
                if (lastIndex[d] > i) {
                    // Swap the digits
                    char temp = digits[i];
                    digits[i] = digits[lastIndex[d]];
                    digits[lastIndex[d]] = temp;
                    return Integer.parseInt(new String(digits));
                }
            }
        }
        
        // No swap needed
        return num;
    }
}
//KDS

```
```C++ []
class Solution {
public:
    int maximumSwap(int num) {
        string digits = to_string(num);
        vector<int> lastIndex(10, -1);
        
        // Store the last occurrence of each digit
        for (int i = 0; i < digits.length(); i++) {
            lastIndex[digits[i] - '0'] = i;
        }
        
        // Find the first digit that can be swapped for a larger one
        for (int i = 0; i < digits.length(); i++) {
            for (int d = 9; d > digits[i] - '0'; d--) {
                if (lastIndex[d] > i) {
                    // Swap the digits
                    swap(digits[i], digits[lastIndex[d]]);
                    return stoi(digits);
                }
            }
        }
        
        // No swap needed
        return num;
    }
};
```

```Python []
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last_index = {int(d): i for i, d in enumerate(digits)}
        
        for i, d in enumerate(digits):
            for larger in range(9, int(d), -1):
                if larger in last_index and last_index[larger] > i:
                    # Swap the digits
                    digits[i], digits[last_index[larger]] = digits[last_index[larger]], digits[i]
                    return int(''.join(digits))
        
        # No swap needed
        return num
```
