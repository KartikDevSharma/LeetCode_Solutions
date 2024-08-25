JAVA
```Java []
class Solution {
    private int index;
    private char[] tokens;

    public int calculate(String s) {
        index = 0;
        tokens = s.toCharArray();
        return evaluateExpression();
    }

    private int evaluateExpression() {
        int result = 0, number = 0;
        int sign = 1;

        for (; index < tokens.length; index++) {
            char token = tokens[index];

            switch (token) {
                case ' ':
                    continue;
                case '(':
                    index++;
                    number = evaluateExpression();
                    break;
                case ')':
                    return result + sign * number;
                case '+':
                case '-':
                    result += sign * number;
                    number = 0;
                    sign = (token == '+') ? 1 : -1;
                    break;
                default:
                    number = number * 10 + (token - '0');
            }
        }

        return result + sign * number;
    }
}
```
C++
```C++ []
class Solution {
private:
    int index;
    string tokens;

    int evaluateExpression() {
        int result = 0, number = 0;
        int sign = 1;

        for (; index < tokens.length(); ++index) {
            char token = tokens[index];

            switch (token) {
                case ' ':
                    continue;
                case '(':
                    ++index;
                    number = evaluateExpression();
                    break;
                case ')':
                    return result + sign * number;
                case '+':
                case '-':
                    result += sign * number;
                    number = 0;
                    sign = (token == '+') ? 1 : -1;
                    break;
                default:
                    number = number * 10 + (token - '0');
            }
        }

        return result + sign * number;
    }

public:
    int calculate(string s) {
        index = 0;
        tokens = s;
        return evaluateExpression();
    }
};
```
PYTHON
```Python []
class Solution:
    def calculate(self, s: str) -> int:
        self.index = 0
        self.tokens = s
        return self.evaluate_expression()

    def evaluate_expression(self) -> int:
        result, number = 0, 0
        sign = 1

        while self.index < len(self.tokens):
            token = self.tokens[self.index]
            self.index += 1

            if token == ' ':
                continue
            elif token == '(':
                number = self.evaluate_expression()
            elif token == ')':
                return result + sign * number
            elif token in ('+', '-'):
                result += sign * number
                number = 0
                sign = 1 if token == '+' else -1
            else:
                number = number * 10 + int(token)

        return result + sign * number
```
GO
```Go []
func calculate(s string) int {
    var index int
    var evaluateExpression func() int

    evaluateExpression = func() int {
        result, number := 0, 0
        sign := 1

        for index < len(s) {
            token := s[index]
            index++

            switch token {
            case ' ':
                continue
            case '(':
                number = evaluateExpression()
            case ')':
                return result + sign*number
            case '+', '-':
                result += sign * number
                number = 0
                if token == '+' {
                    sign = 1
                } else {
                    sign = -1
                }
            default:
                number = number*10 + int(token-'0')
            }
        }

        return result + sign*number
    }

    return evaluateExpression()
}
```
RUST
```Rust []
impl Solution {
    pub fn calculate(s: String) -> i32 {
        let mut index = 0;
        let tokens: Vec<char> = s.chars().collect();

        fn evaluate_expression(tokens: &[char], index: &mut usize) -> i32 {
            let mut result = 0;
            let mut number = 0;
            let mut sign = 1;

            while *index < tokens.len() {
                let token = tokens[*index];
                *index += 1;

                match token {
                    ' ' => continue,
                    '(' => number = evaluate_expression(tokens, index),
                    ')' => return result + sign * number,
                    '+' | '-' => {
                        result += sign * number;
                        number = 0;
                        sign = if token == '+' { 1 } else { -1 };
                    }
                    _ => number = number * 10 + token.to_digit(10).unwrap() as i32,
                }
            }

            result + sign * number
        }

        evaluate_expression(&tokens, &mut index)
    }
}
```
JAVASCRIPT
```JavaScript []
/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    let index = 0;

    function evaluateExpression() {
        let result = 0;
        let number = 0;
        let sign = 1;

        while (index < s.length) {
            const token = s[index++];

            switch (token) {
                case ' ':
                    continue;
                case '(':
                    number = evaluateExpression();
                    break;
                case ')':
                    return result + sign * number;
                case '+':
                case '-':
                    result += sign * number;
                    number = 0;
                    sign = token === '+' ? 1 : -1;
                    break;
                default:
                    number = number * 10 + (token.charCodeAt(0) - '0'.charCodeAt(0));
            }
        }

        return result + sign * number;
    }

    return evaluateExpression();
};
```
