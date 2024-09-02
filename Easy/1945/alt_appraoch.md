```java []
class Solution {
    public int getLucky(String s, int k) {
        int result = 0;
        
        // Convert and sum in one pass
        for (char c : s.toCharArray()) {
            int value = c - 'a' + 1;
            result += (value > 9) ? (value % 10 + value / 10) : value;
        }
        
        // Perform transformations
        while (--k > 0 && result > 9) {
            result = sumDigits(result);
        }
        
        return result;
    }
    
    private int sumDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
```

```cpp
class Solution {
public:
    int getLucky(string s, int k) {
        int result = 0;
        
        // Convert and sum in one pass
        for (char c : s) {
            int value = c - 'a' + 1;
            result += (value > 9) ? (value % 10 + value / 10) : value;
        }
        
        // Perform transformations
        while (--k > 0 && result > 9) {
            result = sumDigits(result);
        }
        
        return result;
    }
    
private:
    int sumDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
};

```



```python
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result = sum(sum(int(d) for d in str(ord(c) - ord('a') + 1)) for c in s)
        
        while k > 1 and result > 9:
            result = sum(int(d) for d in str(result))
            k -= 1
        
        return result

```



```go
func getLucky(s string, k int) int {
    result := 0
    
    // Convert and sum in one pass
    for _, c := range s {
        value := int(c - 'a' + 1)
        if value > 9 {
            result += value%10 + value/10
        } else {
            result += value
        }
    }
    
    // Perform transformations
    for k > 1 && result > 9 {
        result = sumDigits(result)
        k--
    }
    
    return result
}

func sumDigits(num int) int {
    sum := 0
    for num > 0 {
        sum += num % 10
        num /= 10
    }
    return sum
}

```





```rust
impl Solution {
    pub fn get_lucky(s: String, mut k: i32) -> i32 {
        let mut result: i32 = s.chars().map(|c| {
            let value = (c as u8 - b'a' + 1) as i32;
            if value > 9 { value % 10 + value / 10 } else { value }
        }).sum();
        
        while k > 1 && result > 9 {
            result = Self::sum_digits(result);
            k -= 1;
        }
        
        result
    }
    
    fn sum_digits(mut num: i32) -> i32 {
        let mut sum = 0;
        while num > 0 {
            sum += num % 10;
            num /= 10;
        }
        sum
    }
}

```





```csharp
public class Solution {
    public int GetLucky(string s, int k) {
        int result = s.Sum(c => {
            int value = c - 'a' + 1;
            return value > 9 ? value % 10 + value / 10 : value;
        });
        
        while (--k > 0 && result > 9) {
            result = SumDigits(result);
        }
        
        return result;
    }
    
    private int SumDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

```





```kotlin
class Solution {
    fun getLucky(s: String, k: Int): Int {
        var result = s.sumOf { c ->
            val value = c - 'a' + 1
            if (value > 9) value % 10 + value / 10 else value
        }
        
        var remainingK = k
        while (--remainingK > 0 && result > 9) {
            result = sumDigits(result)
        }
        
        return result
    }
    
    private fun sumDigits(num: Int): Int {
        var sum = 0
        var n = num
        while (n > 0) {
            sum += n % 10
            n /= 10
        }
        return sum
    }
}

```





```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var getLucky = function(s, k) {
    let result = [...s].reduce((sum, c) => {
        let value = c.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
        return sum + (value > 9 ? Math.floor(value / 10) + value % 10 : value);
    }, 0);
    
    while (--k > 0 && result > 9) {
        result = sumDigits(result);
    }
    
    return result;
};

function sumDigits(num) {
    let sum = 0;
    while (num > 0) {
        sum += num % 10;
        num = Math.floor(num / 10);
    }
    return sum;
}

```





```typescript
function getLucky(s: string, k: number): number {
    let result: number = s.split('').reduce((sum, c) => {
        const value: number = c.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
        return sum + (value > 9 ? Math.floor(value / 10) + value % 10 : value);
    }, 0);
    
    while (--k > 0 && result > 9) {
        result = sumDigits(result);
    }
    
    return result;
}

function sumDigits(num: number): number {
    let sum: number = 0;
    while (num > 0) {
        sum += num % 10;
        num = Math.floor(num / 10);
    }
    return sum;
}

```

