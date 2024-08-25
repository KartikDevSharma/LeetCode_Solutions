JAVA
```Java []
class Solution {
    public int getLucky(String inputString, int transformCount) {
        int digitSum = 0;
        for (char character : inputString.toCharArray()) {
            int charValue = character - 'a' + 1;
            digitSum += charValue / 10 + charValue % 10;
        }
        
        while (--transformCount > 0 && digitSum > 9) {
            int newSum = 0;
            while (digitSum > 0) {
                newSum += digitSum % 10;
                digitSum /= 10;
            }
            digitSum = newSum;
        }
        
        return digitSum;
    }
}


//https://leetcode.com/problems/sum-of-digits-of-string-after-convert/submissions/1368063858/

```
C++
```C++ []
class Solution {
public:
    int getLucky(string inputString, int transformCount) {
        int digitSum = 0;
        for (char character : inputString) {
            int charValue = character - 'a' + 1;
            digitSum += charValue / 10 + charValue % 10;
        }
        
        while (--transformCount > 0 && digitSum > 9) {
            int newSum = 0;
            while (digitSum > 0) {
                newSum += digitSum % 10;
                digitSum /= 10;
            }
            digitSum = newSum;
        }
        
        return digitSum;
    }
};


//https://leetcode.com/problems/sum-of-digits-of-string-after-convert/submissions/1368057720/

```
Python
```python []
class Solution:
    def getLucky(self, input_string: str, transform_count: int) -> int:
        digit_sum = sum(sum(divmod(ord(char) - ord('a') + 1, 10)) for char in input_string)
        
        while transform_count > 1 and digit_sum > 9:
            digit_sum = sum(int(digit) for digit in str(digit_sum))
            transform_count -= 1
        
        return digit_sum


//https://leetcode.com/problems/sum-of-digits-of-string-after-convert/submissions/1368066905/
```
Go
```Go []
func getLucky(inputString string, transformCount int) int {
    digitSum := 0
    for _, character := range inputString {
        charValue := int(character - 'a' + 1)
        digitSum += charValue/10 + charValue%10
    }
    
    for transformCount > 1 && digitSum > 9 {
        newSum := 0
        for digitSum > 0 {
            newSum += digitSum % 10
            digitSum /= 10
        }
        digitSum = newSum
        transformCount--
    }
    
    return digitSum
}


//https://leetcode.com/problems/sum-of-digits-of-string-after-convert/submissions/1368058664/

```
Rust
```Rust []
impl Solution {
    pub fn get_lucky(input_string: String, mut transform_count: i32) -> i32 {
        let mut digit_sum = input_string.chars()
            .map(|c| {
                let char_value = (c as u8 - b'a' + 1) as i32;
                char_value / 10 + char_value % 10
            })
            .sum();
        
        while transform_count > 1 && digit_sum > 9 {
            let mut new_sum = 0;
            while digit_sum > 0 {
                new_sum += digit_sum % 10;
                digit_sum /= 10;
            }
            digit_sum = new_sum;
            transform_count -= 1;
        }
        
        digit_sum
    }
}

//https://leetcode.com/problems/sum-of-digits-of-string-after-convert/submissions/1368059014/

```
JavaScript
```JavaScript []
/**
 * @param {string} inputString
 * @param {number} transformCount
 * @return {number}
 */
var getLucky = function(inputString, transformCount) {
    let digitSum = 0;
    for (let character of inputString) {
        let charValue = character.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
        digitSum += Math.floor(charValue / 10) + charValue % 10;
    }
    
    while (--transformCount > 0 && digitSum > 9) {
        let newSum = 0;
        while (digitSum > 0) {
            newSum += digitSum % 10;
            digitSum = Math.floor(digitSum / 10);
        }
        digitSum = newSum;
    }
    
    return digitSum;
};

//https://leetcode.com/problems/sum-of-digits-of-string-after-convert/submissions/1368059156/

```
