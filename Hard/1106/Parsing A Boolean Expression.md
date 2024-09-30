```Java []
class Solution {
    private int index;

    public boolean parseBoolExpr(String expression) {
        index = 0;
        return parseExpression(expression);
    }

    private boolean parseExpression(String expr) {
        char c = expr.charAt(index++);
        switch (c) {
            case 't': return true;
            case 'f': return false;
            case '!': 
                index++; // Skip '('
                boolean result = parseExpression(expr);
                index++; // Skip ')'
                return !result;
            case '&': return parseAndOr(expr, true);
            case '|': return parseAndOr(expr, false);
            default: throw new IllegalArgumentException("Unexpected character: " + c);
        }
    }

    private boolean parseAndOr(String expr, boolean isAnd) {
        index++; // Skip '('
        boolean result = isAnd;
        while (true) {
            boolean value = parseExpression(expr);
            result = isAnd ? (result && value) : (result || value);
            if (expr.charAt(index) == ')') {
                index++;
                return result;
            }
            index++; // Skip ','
        }
    }
}
//KDS
```

```C++ []
class Solution {
private:
    int index;

public:
    bool parseBoolExpr(string expression) {
        index = 0;
        return parseExpression(expression);
    }

private:
    bool parseExpression(const string& expr) {
        char c = expr[index++];
        switch (c) {
            case 't': return true;
            case 'f': return false;
            case '!': {
                index++; // Skip '('
                bool result = parseExpression(expr);
                index++; // Skip ')'
                return !result;
            }
            case '&': return parseAndOr(expr, true);
            case '|': return parseAndOr(expr, false);
            default: throw invalid_argument("Unexpected character: " + c);
        }
    }

    bool parseAndOr(const string& expr, bool isAnd) {
        index++; // Skip '('
        bool result = isAnd;
        while (true) {
            bool value = parseExpression(expr);
            result = isAnd ? (result && value) : (result || value);
            if (expr[index] == ')') {
                index++;
                return result;
            }
            index++; // Skip ','
        }
    }
};
//KDS
```
```Python []
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        self.index = 0
        return self.parse_expression(expression)

    def parse_expression(self, expr: str) -> bool:
        c = expr[self.index]
        self.index += 1
        
        if c == 't':
            return True
        elif c == 'f':
            return False
        elif c == '!':
            self.index += 1  # Skip '('
            result = self.parse_expression(expr)
            self.index += 1  # Skip ')'
            return not result
        elif c == '&':
            return self.parse_and_or(expr, is_and=True)
        elif c == '|':
            return self.parse_and_or(expr, is_and=False)
        else:
            raise ValueError(f"Unexpected character: {c}")

    def parse_and_or(self, expr: str, is_and: bool) -> bool:
        self.index += 1  # Skip '('
        result = is_and
        
        while True:
            value = self.parse_expression(expr)
            result = result and value if is_and else result or value
            if expr[self.index] == ')':
                self.index += 1
                return result
            self.index += 1  # Skip ','


#KDS

```
