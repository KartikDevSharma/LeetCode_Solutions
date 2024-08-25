

# Code
```java []
class Solution {
    public int getLucky(String inputString, int transformCount) {
        int transformedValue = convertAndSum(inputString);
        
        for (int i = 0; i < transformCount - 1 && transformedValue >= 10; i++) {
            transformedValue = sumDigits(transformedValue);
        }
        
        return transformedValue;
    }
    
    private int convertAndSum(String str) {
        int sum = 0;
        for (char c : str.toCharArray()) {
            int letterValue = c - 'a' + 1;
            sum += (letterValue < 10) ? letterValue : (letterValue / 10 + letterValue % 10);
        }
        return sum;
    }
    
    private int sumDigits(int number) {
        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }
}
```
```C++ []
class Solution {
public:
    int getLucky(string inputString, int transformCount) {
        int transformedValue = convertAndSum(inputString);
        
        for (int i = 0; i < transformCount - 1 && transformedValue >= 10; i++) {
            transformedValue = sumDigits(transformedValue);
        }
        
        return transformedValue;
    }
    
private:
    int convertAndSum(const string& str) {
        int sum = 0;
        for (char c : str) {
            int letterValue = c - 'a' + 1;
            sum += (letterValue < 10) ? letterValue : (letterValue / 10 + letterValue % 10);
        }
        return sum;
    }
    
    int sumDigits(int number) {
        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }
};

//https://leetcode.com/problems/sum-of-digits-of-string-after-convert/submissions/1366992321/
```
```Python []
class Solution:
    def getLucky(self, inputString: str, transformCount: int) -> int:
        transformedValue = self.convertAndSum(inputString)
        
        for _ in range(transformCount - 1):
            if transformedValue < 10:
                break
            transformedValue = self.sumDigits(transformedValue)
        
        return transformedValue
    
    def convertAndSum(self, s: str) -> int:
        return sum(self.digitSum(ord(c) - ord('a') + 1) for c in s)
    
    def digitSum(self, n: int) -> int:
        return n if n < 10 else n // 10 + n % 10
    
    def sumDigits(self, number: int) -> int:
        return sum(int(digit) for digit in str(number))
```
```Go []
func getLucky(inputString string, transformCount int) int {
    transformedValue := convertAndSum(inputString)
    
    for i := 0; i < transformCount-1 && transformedValue >= 10; i++ {
        transformedValue = sumDigits(transformedValue)
    }
    
    return transformedValue
}

func convertAndSum(s string) int {
    sum := 0
    for _, c := range s {
        letterValue := int(c - 'a' + 1)
        if letterValue < 10 {
            sum += letterValue
        } else {
            sum += letterValue/10 + letterValue%10
        }
    }
    return sum
}

func sumDigits(number int) int {
    sum := 0
    for number > 0 {
        sum += number % 10
        number /= 10
    }
    return sum
}
```
```Rust []
impl Solution {
    pub fn get_lucky(input_string: String, transform_count: i32) -> i32 {
        let mut transformed_value = Self::convert_and_sum(&input_string);
        
        for _ in 0..transform_count-1 {
            if transformed_value < 10 {
                break;
            }
            transformed_value = Self::sum_digits(transformed_value);
        }
        
        transformed_value
    }
    
    fn convert_and_sum(s: &str) -> i32 {
        s.chars().map(|c| {
            let letter_value = (c as i32) - ('a' as i32) + 1;
            if letter_value < 10 {
                letter_value
            } else {
                letter_value / 10 + letter_value % 10
            }
        }).sum()
    }
    
    fn sum_digits(mut number: i32) -> i32 {
        let mut sum = 0;
        while number > 0 {
            sum += number % 10;
            number /= 10;
        }
        sum
    }
}
```
```JavaScript []
/**
 * @param {string} inputString
 * @param {number} transformCount
 * @return {number}
 */
var getLucky = function(inputString, transformCount) {
    let transformedValue = convertAndSum(inputString);
    
    for (let i = 0; i < transformCount - 1 && transformedValue >= 10; i++) {
        transformedValue = sumDigits(transformedValue);
    }
    
    return transformedValue;
};

function convertAndSum(str) {
    return str.split('').reduce((sum, char) => {
        const letterValue = char.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
        return sum + (letterValue < 10 ? letterValue : Math.floor(letterValue / 10) + letterValue % 10);
    }, 0);
}

function sumDigits(number) {
    let sum = 0;
    while (number > 0) {
        sum += number % 10;
        number = Math.floor(number / 10);
    }
    return sum;
}
```
