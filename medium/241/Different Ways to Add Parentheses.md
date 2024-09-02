**Top Down**
```java []
class Solution {
    private List<Integer>[][] memo;
    private char[] expression;

    public List<Integer> diffWaysToCompute(String inputExpression) {
        expression = inputExpression.toCharArray();
        int length = expression.length;
        memo = new List[length][length];
        return evaluateExpression(0, length - 1);
    }

    private List<Integer> evaluateExpression(int startIndex, int endIndex) {
        if (memo[startIndex][endIndex] != null) {
            return memo[startIndex][endIndex];
        }

        List<Integer> results = new ArrayList<>();
        
        boolean containsOperator = false;
        for (int i = startIndex; i <= endIndex; i++) {
            if (expression[i] == '+' || expression[i] == '-' || expression[i] == '*') {
                containsOperator = true;
                List<Integer> leftResults = evaluateExpression(startIndex, i - 1);
                List<Integer> rightResults = evaluateExpression(i + 1, endIndex);

                for (int leftValue : leftResults) {
                    for (int rightValue : rightResults) {
                        switch (expression[i]) {
                            case '+': results.add(leftValue + rightValue); break;
                            case '-': results.add(leftValue - rightValue); break;
                            case '*': results.add(leftValue * rightValue); break;
                        }
                    }
                }
            }
        }

        if (!containsOperator) {
            results.add(Integer.parseInt(new String(expression, startIndex, endIndex - startIndex + 1)));
        }

        memo[startIndex][endIndex] = results;
        return results;
    }
}

//https://leetcode.com/problems/different-ways-to-add-parentheses/submissions/1369987816/
```



```cpp []
class Solution {
private:
    vector<vector<vector<int>>> memo;
    string expression;

    vector<int> evaluateExpression(int startIndex, int endIndex) {
        if (!memo[startIndex][endIndex].empty()) {
            return memo[startIndex][endIndex];
        }

        vector<int> results;
        
        bool containsOperator = false;
        for (int i = startIndex; i <= endIndex; i++) {
            if (expression[i] == '+' || expression[i] == '-' || expression[i] == '*') {
                containsOperator = true;
                vector<int> leftResults = evaluateExpression(startIndex, i - 1);
                vector<int> rightResults = evaluateExpression(i + 1, endIndex);

                for (int leftValue : leftResults) {
                    for (int rightValue : rightResults) {
                        switch (expression[i]) {
                            case '+': results.push_back(leftValue + rightValue); break;
                            case '-': results.push_back(leftValue - rightValue); break;
                            case '*': results.push_back(leftValue * rightValue); break;
                        }
                    }
                }
            }
        }

        if (!containsOperator) {
            results.push_back(stoi(expression.substr(startIndex, endIndex - startIndex + 1)));
        }

        memo[startIndex][endIndex] = results;
        return results;
    }

public:
    vector<int> diffWaysToCompute(string inputExpression) {
        expression = inputExpression;
        int length = expression.length();
        memo.resize(length, vector<vector<int>>(length));
        return evaluateExpression(0, length - 1);
    }
};


//https://leetcode.com/problems/different-ways-to-add-parentheses/submissions/1369988079/
```


```python []
class Solution:
    def diffWaysToCompute(self, inputExpression: str) -> List[int]:
        memo = {}
        
        def evaluateExpression(startIndex: int, endIndex: int) -> List[int]:
            if (startIndex, endIndex) in memo:
                return memo[(startIndex, endIndex)]
            
            results = []
            containsOperator = False
            
            for i in range(startIndex, endIndex + 1):
                if inputExpression[i] in '+-*':
                    containsOperator = True
                    leftResults = evaluateExpression(startIndex, i - 1)
                    rightResults = evaluateExpression(i + 1, endIndex)
                    
                    for leftValue in leftResults:
                        for rightValue in rightResults:
                            if inputExpression[i] == '+':
                                results.append(leftValue + rightValue)
                            elif inputExpression[i] == '-':
                                results.append(leftValue - rightValue)
                            elif inputExpression[i] == '*':
                                results.append(leftValue * rightValue)
            
            if not containsOperator:
                results.append(int(inputExpression[startIndex:endIndex+1]))
            
            memo[(startIndex, endIndex)] = results
            return results
        
        return evaluateExpression(0, len(inputExpression) - 1)
```



```go []
func diffWaysToCompute(inputExpression string) []int {
    memo := make(map[string][]int)
    
    var evaluateExpression func(startIndex, endIndex int) []int
    evaluateExpression = func(startIndex, endIndex int) []int {
        key := fmt.Sprintf("%d,%d", startIndex, endIndex)
        if results, ok := memo[key]; ok {
            return results
        }
        
        var results []int
        containsOperator := false
        
        for i := startIndex; i <= endIndex; i++ {
            if inputExpression[i] == '+' || inputExpression[i] == '-' || inputExpression[i] == '*' {
                containsOperator = true
                leftResults := evaluateExpression(startIndex, i-1)
                rightResults := evaluateExpression(i+1, endIndex)
                
                for _, leftValue := range leftResults {
                    for _, rightValue := range rightResults {
                        switch inputExpression[i] {
                        case '+':
                            results = append(results, leftValue + rightValue)
                        case '-':
                            results = append(results, leftValue - rightValue)
                        case '*':
                            results = append(results, leftValue * rightValue)
                        }
                    }
                }
            }
        }
        
        if !containsOperator {
            value, _ := strconv.Atoi(inputExpression[startIndex:endIndex+1])
            results = append(results, value)
        }
        
        memo[key] = results
        return results
    }
    
    return evaluateExpression(0, len(inputExpression)-1)
}
```



```rust []
use std::collections::HashMap;

impl Solution {
    pub fn diff_ways_to_compute(input_expression: String) -> Vec<i32> {
        let mut memo: HashMap<(usize, usize), Vec<i32>> = HashMap::new();
        
        fn evaluate_expression(start_index: usize, end_index: usize, input_expression: &str, memo: &mut HashMap<(usize, usize), Vec<i32>>) -> Vec<i32> {
            if let Some(results) = memo.get(&(start_index, end_index)) {
                return results.clone();
            }
            
            let mut results = Vec::new();
            let mut contains_operator = false;
            
            for i in start_index..=end_index {
                if ['+', '-', '*'].contains(&input_expression.chars().nth(i).unwrap()) {
                    contains_operator = true;
                    let left_results = evaluate_expression(start_index, i - 1, input_expression, memo);
                    let right_results = evaluate_expression(i + 1, end_index, input_expression, memo);
                    
                    for &left_value in &left_results {
                        for &right_value in &right_results {
                            match input_expression.chars().nth(i).unwrap() {
                                '+' => results.push(left_value + right_value),
                                '-' => results.push(left_value - right_value),
                                '*' => results.push(left_value * right_value),
                                _ => unreachable!(),
                            }
                        }
                    }
                }
            }
            
            if !contains_operator {
                results.push(input_expression[start_index..=end_index].parse().unwrap());
            }
            
            memo.insert((start_index, end_index), results.clone());
            results
        }
        
        evaluate_expression(0, input_expression.len() - 1, &input_expression, &mut memo)
    }
}


//https://leetcode.com/problems/different-ways-to-add-parentheses/submissions/1369986687/
```



```javascript []
/**
 * @param {string} inputExpression
 * @return {number[]}
 */
var diffWaysToCompute = function(inputExpression) {
    const memo = new Map();
    
    function evaluateExpression(startIndex, endIndex) {
        const key = `${startIndex},${endIndex}`;
        if (memo.has(key)) {
            return memo.get(key);
        }
        
        const results = [];
        let containsOperator = false;
        
        for (let i = startIndex; i <= endIndex; i++) {
            if (['+', '-', '*'].includes(inputExpression[i])) {
                containsOperator = true;
                const leftResults = evaluateExpression(startIndex, i - 1);
                const rightResults = evaluateExpression(i + 1, endIndex);
                
                for (const leftValue of leftResults) {
                    for (const rightValue of rightResults) {
                        switch (inputExpression[i]) {
                            case '+': results.push(leftValue + rightValue); break;
                            case '-': results.push(leftValue - rightValue); break;
                            case '*': results.push(leftValue * rightValue); break;
                        }
                    }
                }
            }
        }
        
        if (!containsOperator) {
            results.push(parseInt(inputExpression.slice(startIndex, endIndex + 1)));
        }
        
        memo.set(key, results);
        return results;
    }
    
    return evaluateExpression(0, inputExpression.length - 1);
};


//https://leetcode.com/problems/different-ways-to-add-parentheses/submissions/1369986407/
```


**Bottom Up**
```Java []
class Solution {
    public List<Integer> diffWaysToCompute(String expression) {
        int length = expression.length();
        List<Integer>[][] table = new ArrayList[length][length];
        List<Integer> numbers = new ArrayList<>();
        List<Character> operators = new ArrayList<>();
        
        // Parse the expression
        int currentNumber = 0;
        for (char c : expression.toCharArray()) {
            if (Character.isDigit(c)) {
                currentNumber = currentNumber * 10 + (c - '0');
            } else {
                numbers.add(currentNumber);
                currentNumber = 0;
                operators.add(c);
            }
        }
        numbers.add(currentNumber);
        
        // Initialize base cases (single numbers)
        for (int i = 0; i < numbers.size(); i++) {
            table[i][i] = new ArrayList<>();
            table[i][i].add(numbers.get(i));
        }
        
        // Fill the table
        for (int len = 2; len <= numbers.size(); len++) {
            for (int startIndex = 0; startIndex + len <= numbers.size(); startIndex++) {
                int endIndex = startIndex + len - 1;
                table[startIndex][endIndex] = new ArrayList<>();
                for (int splitIndex = startIndex; splitIndex < endIndex; splitIndex++) {
                    char op = operators.get(splitIndex);
                    for (int leftValue : table[startIndex][splitIndex]) {
                        for (int rightValue : table[splitIndex+1][endIndex]) {
                            switch(op) {
                                case '+': table[startIndex][endIndex].add(leftValue + rightValue); break;
                                case '-': table[startIndex][endIndex].add(leftValue - rightValue); break;
                                case '*': table[startIndex][endIndex].add(leftValue * rightValue); break;
                            }
                        }
                    }
                }
            }
        }
        
        return table[0][numbers.size()-1];
    }
}
```
```C++ []
class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        int length = expression.length();
        vector<vector<vector<int>>> table(length, vector<vector<int>>(length));
        vector<int> numbers;
        vector<char> operators;
        
        // Parse the expression
        int currentNumber = 0;
        for (char c : expression) {
            if (isdigit(c)) {
                currentNumber = currentNumber * 10 + (c - '0');
            } else {
                numbers.push_back(currentNumber);
                currentNumber = 0;
                operators.push_back(c);
            }
        }
        numbers.push_back(currentNumber);
        
        // Initialize base cases (single numbers)
        for (int i = 0; i < numbers.size(); i++) {
            table[i][i] = {numbers[i]};
        }
        
        // Fill the table table
        for (int len = 2; len <= numbers.size(); len++) {
            for (int startIndex = 0; startIndex + len <= numbers.size(); startIndex++) {
                int endIndex = startIndex + len - 1;
                for (int splitIndex = startIndex; splitIndex < endIndex; splitIndex++) {
                    char op = operators[splitIndex];
                    for (int leftValue : table[startIndex][splitIndex]) {
                        for (int rightValue : table[splitIndex+1][endIndex]) {
                            switch(op) {
                                case '+': table[startIndex][endIndex].push_back(leftValue + rightValue); break;
                                case '-': table[startIndex][endIndex].push_back(leftValue - rightValue); break;
                                case '*': table[startIndex][endIndex].push_back(leftValue * rightValue); break;
                            }
                        }
                    }
                }
            }
        }
        
        return table[0][numbers.size()-1];
    }
};
```
```Python []
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        length = len(expression)
        table = [[[] for _ in range(length)] for _ in range(length)]
        numbers = []
        operators = []
        
        # Parse the expression
        current_number = 0
        for c in expression:
            if c.isdigit():
                current_number = current_number * 10 + int(c)
            else:
                numbers.append(current_number)
                current_number = 0
                operators.append(c)
        numbers.append(current_number)
        
        # Initialize base cases (single numbers)
        for i in range(len(numbers)):
            table[i][i] = [numbers[i]]
        
        # Fill the table table
        for length in range(2, len(numbers) + 1):
            for start_index in range(len(numbers) - length + 1):
                end_index = start_index + length - 1
                for split_index in range(start_index, end_index):
                    op = operators[split_index]
                    for left_value in table[start_index][split_index]:
                        for right_value in table[split_index + 1][end_index]:
                            if op == '+':
                                table[start_index][end_index].append(left_value + right_value)
                            elif op == '-':
                                table[start_index][end_index].append(left_value - right_value)
                            elif op == '*':
                                table[start_index][end_index].append(left_value * right_value)
        
        return table[0][len(numbers) - 1]
```
```Go []
func diffWaysToCompute(expression string) []int {
    length := len(expression)
    table := make([][][]int, length)
    for i := range table {
        table[i] = make([][]int, length)
    }
    
    numbers := []int{}
    operators := []byte{}
    
    // Parse the expression
    currentNumber := 0
    for i := 0; i < length; i++ {
        if expression[i] >= '0' && expression[i] <= '9' {
            currentNumber = currentNumber*10 + int(expression[i]-'0')
        } else {
            numbers = append(numbers, currentNumber)
            currentNumber = 0
            operators = append(operators, expression[i])
        }
    }
    numbers = append(numbers, currentNumber)
    
    // Initialize base cases (single numbers)
    for i := 0; i < len(numbers); i++ {
        table[i][i] = []int{numbers[i]}
    }
    
    // Fill the table table
    for l := 2; l <= len(numbers); l++ {
        for startIndex := 0; startIndex+l <= len(numbers); startIndex++ {
            endIndex := startIndex + l - 1
            for splitIndex := startIndex; splitIndex < endIndex; splitIndex++ {
                op := operators[splitIndex]
                for _, leftValue := range table[startIndex][splitIndex] {
                    for _, rightValue := range table[splitIndex+1][endIndex] {
                        var result int
                        switch op {
                        case '+':
                            result = leftValue + rightValue
                        case '-':
                            result = leftValue - rightValue
                        case '*':
                            result = leftValue * rightValue
                        }
                        table[startIndex][endIndex] = append(table[startIndex][endIndex], result)
                    }
                }
            }
        }
    }
    
    return table[0][len(numbers)-1]
}
```
```Rust []
impl Solution {
    pub fn diff_ways_to_compute(expression: String) -> Vec<i32> {
        let length = expression.len();
        let mut table = vec![vec![Vec::new(); length]; length];
        let mut numbers = Vec::new();
        let mut operators = Vec::new();
        
        // Parse the expression
        let mut current_number = 0;
        for c in expression.chars() {
            if c.is_digit(10) {
                current_number = current_number * 10 + c.to_digit(10).unwrap() as i32;
            } else {
                numbers.push(current_number);
                current_number = 0;
                operators.push(c);
            }
        }
        numbers.push(current_number);
        
        // Initialize base cases (single numbers)
        for i in 0..numbers.len() {
            table[i][i] = vec![numbers[i]];
        }
        
        // Fill the table
        for len in 2..=numbers.len() {
            for start_index in 0..=numbers.len() - len {
                let end_index = start_index + len - 1;
                let mut results = Vec::new();
                for split_index in start_index..end_index {
                    let op = operators[split_index];
                    for &left_value in &table[start_index][split_index] {
                        for &right_value in &table[split_index + 1][end_index] {
                            let result = match op {
                                '+' => left_value + right_value,
                                '-' => left_value - right_value,
                                '*' => left_value * right_value,
                                _ => unreachable!(),
                            };
                            results.push(result);
                        }
                    }
                }
                table[start_index][end_index] = results;
            }
        }
        
        table[0][numbers.len() - 1].clone()
    }
}
```
```JavaScript []
/**
 * @param {string} expression
 * @return {number[]}
 */
var diffWaysToCompute = function(expression) {
    const length = expression.length;
    const table = Array.from({ length }, () => Array.from({ length }, () => []));
    const numbers = [];
    const operators = [];
    
    // Parse the expression
    let currentNumber = 0;
    for (let c of expression) {
        if (c >= '0' && c <= '9') {
            currentNumber = currentNumber * 10 + parseInt(c);
        } else {
            numbers.push(currentNumber);
            currentNumber = 0;
            operators.push(c);
        }
    }
    numbers.push(currentNumber);
    
    // Initialize base cases (single numbers)
    for (let i = 0; i < numbers.length; i++) {
        table[i][i] = [numbers[i]];
    }
    
    // Fill the table table
    for (let len = 2; len <= numbers.length; len++) {
        for (let startIndex = 0; startIndex + len <= numbers.length; startIndex++) {
            const endIndex = startIndex + len - 1;
            for (let splitIndex = startIndex; splitIndex < endIndex; splitIndex++) {
                const op = operators[splitIndex];
                for (const leftValue of table[startIndex][splitIndex]) {
                    for (const rightValue of table[splitIndex + 1][endIndex]) {
                        switch(op) {
                            case '+': table[startIndex][endIndex].push(leftValue + rightValue); break;
                            case '-': table[startIndex][endIndex].push(leftValue - rightValue); break;
                            case '*': table[startIndex][endIndex].push(leftValue * rightValue); break;
                        }
                    }
                }
            }
        }
    }
    
    return table[0][numbers.length - 1];
};
```
---
Approach 3 Bootom up optimized
```Java []
class Solution {
    private static final int MAX_EXPRESSION_LENGTH = 20;
    private static final int MAX_NUMBER = 99;

    public List<Integer> diffWaysToCompute(String expression) {
        int expressionLength = expression.length();
        List<Integer>[][] resultTable = new ArrayList[expressionLength][expressionLength];

        List<Integer> numbers = new ArrayList<>();
        List<Character> operators = new ArrayList<>();
        
        parseExpression(expression, numbers, operators);
        
        // Initialize base cases (single numbers)
        for (int i = 0; i < numbers.size(); i++) {
            resultTable[i][i] = new ArrayList<>();
            resultTable[i][i].add(numbers.get(i));
        }
        
        // Fill the result table
        for (int subexprLength = 2; subexprLength <= numbers.size(); subexprLength++) {
            for (int start = 0; start + subexprLength <= numbers.size(); start++) {
                int end = start + subexprLength - 1;
                resultTable[start][end] = new ArrayList<>();
                
                for (int split = start; split < end; split++) {
                    char operator = operators.get(split);
                    List<Integer> leftResults = resultTable[start][split];
                    List<Integer> rightResults = resultTable[split + 1][end];
                    
                    combineResults(leftResults, rightResults, operator, resultTable[start][end]);
                }
            }
        }
        
        return resultTable[0][numbers.size() - 1];
    }
    
    private void parseExpression(String expression, List<Integer> numbers, List<Character> operators) {
        int currentNumber = 0;
        for (char c : expression.toCharArray()) {
            if (Character.isDigit(c)) {
                currentNumber = currentNumber * 10 + (c - '0');
            } else {
                numbers.add(currentNumber);
                currentNumber = 0;
                operators.add(c);
            }
        }
        numbers.add(currentNumber);
    }
    
    private void combineResults(List<Integer> leftResults, List<Integer> rightResults, 
                                char operator, List<Integer> combinedResults) {
        for (int leftValue : leftResults) {
            for (int rightValue : rightResults) {
                int result = computeOperation(leftValue, rightValue, operator);
                combinedResults.add(result);
            }
        }
    }
    
    private int computeOperation(int left, int right, char operator) {
        switch (operator) {
            case '+': return left + right;
            case '-': return left - right;
            case '*': return left * right;
            default: throw new IllegalArgumentException("Invalid operator: " + operator);
        }
    }
}

//kartikdevsharmaa
```
```C++ []
class Solution {
private:
    static const int MAX_EXPRESSION_LENGTH = 20;
    static const int MAX_NUMBER = 99;

    void parseExpression(const std::string& expression, std::vector<int>& numbers, std::vector<char>& operators) {
        int currentNumber = 0;
        for (char c : expression) {
            if (std::isdigit(c)) {
                currentNumber = currentNumber * 10 + (c - '0');
            } else {
                numbers.push_back(currentNumber);
                currentNumber = 0;
                operators.push_back(c);
            }
        }
        numbers.push_back(currentNumber);
    }

    void combineResults(const std::vector<int>& leftResults, const std::vector<int>& rightResults,
                        char op, std::vector<int>& combinedResults) {
        for (int leftValue : leftResults) {
            for (int rightValue : rightResults) {
                int result = computeOperation(leftValue, rightValue, op);
                combinedResults.push_back(result);
            }
        }
    }

    int computeOperation(int left, int right, char op) {
        switch (op) {
            case '+': return left + right;
            case '-': return left - right;
            case '*': return left * right;
            default: throw std::invalid_argument("Invalid operator: " + std::string(1, op));
        }
    }

public:
    std::vector<int> diffWaysToCompute(std::string expression) {
        int expressionLength = expression.length();
        std::vector<std::vector<std::vector<int>>> resultTable(expressionLength, std::vector<std::vector<int>>(expressionLength));

        std::vector<int> numbers;
        std::vector<char> operators;
        
        parseExpression(expression, numbers, operators);
        
        // Initialize base cases (single numbers)
        for (int i = 0; i < numbers.size(); i++) {
            resultTable[i][i] = {numbers[i]};
        }
        
        // Fill the result table
        for (int subexprLength = 2; subexprLength <= numbers.size(); subexprLength++) {
            for (int start = 0; start + subexprLength <= numbers.size(); start++) {
                int end = start + subexprLength - 1;
                
                for (int split = start; split < end; split++) {
                    char op = operators[split];
                    const auto& leftResults = resultTable[start][split];
                    const auto& rightResults = resultTable[split + 1][end];
                    
                    combineResults(leftResults, rightResults, op, resultTable[start][end]);
                }
            }
        }
        
        return resultTable[0][numbers.size() - 1];
    }
};


```
```C# []
public class Solution {
    private const int MaxExpressionLength = 20;
    private const int MaxNumber = 99;

    public IList<int> DiffWaysToCompute(string expression) {
        int expressionLength = expression.Length;
        var resultTable = new List<int>[expressionLength, expressionLength];

        var (numbers, operators) = ParseExpression(expression);
        
        // Initialize base cases (single numbers)
        for (int i = 0; i < numbers.Count; i++) {
            resultTable[i, i] = new List<int> { numbers[i] };
        }
        
        // Fill the result table
        for (int subexprLength = 2; subexprLength <= numbers.Count; subexprLength++) {
            for (int start = 0; start + subexprLength <= numbers.Count; start++) {
                int end = start + subexprLength - 1;
                resultTable[start, end] = new List<int>();
                
                for (int split = start; split < end; split++) {
                    char op = operators[split];
                    var leftResults = resultTable[start, split];
                    var rightResults = resultTable[split + 1, end];
                    
                    CombineResults(leftResults, rightResults, op, resultTable[start, end]);
                }
            }
        }
        
        return resultTable[0, numbers.Count - 1];
    }
    
    private (List<int> numbers, List<char> operators) ParseExpression(string expression) {
        var numbers = new List<int>();
        var operators = new List<char>();
        int currentNumber = 0;
        foreach (char c in expression) {
            if (char.IsDigit(c)) {
                currentNumber = currentNumber * 10 + (c - '0');
            } else {
                numbers.Add(currentNumber);
                currentNumber = 0;
                operators.Add(c);
            }
        }
        numbers.Add(currentNumber);
        return (numbers, operators);
    }
    
    private void CombineResults(IList<int> leftResults, IList<int> rightResults, 
                                char op, IList<int> combinedResults) {
        foreach (int leftValue in leftResults) {
            foreach (int rightValue in rightResults) {
                int result = ComputeOperation(leftValue, rightValue, op);
                combinedResults.Add(result);
            }
        }
    }
    
    private int ComputeOperation(int left, int right, char op) {
        return op switch {
            '+' => left + right,
            '-' => left - right,
            '*' => left * right,
            _ => throw new ArgumentException($"Invalid operator: {op}")
        };
    }
}
```
```Python []
class Solution:
    MAX_EXPRESSION_LENGTH = 20
    MAX_NUMBER = 99

    def diffWaysToCompute(self, expression: str) -> List[int]:
        expression_length = len(expression)
        result_table = [[[] for _ in range(expression_length)] for _ in range(expression_length)]

        numbers, operators = self.parse_expression(expression)
        
        # Initialize base cases (single numbers)
        for i in range(len(numbers)):
            result_table[i][i] = [numbers[i]]
        
        # Fill the result table
        for subexpr_length in range(2, len(numbers) + 1):
            for start in range(len(numbers) - subexpr_length + 1):
                end = start + subexpr_length - 1
                
                for split in range(start, end):
                    op = operators[split]
                    left_results = result_table[start][split]
                    right_results = result_table[split + 1][end]
                    
                    self.combine_results(left_results, right_results, op, result_table[start][end])
        
        return result_table[0][len(numbers) - 1]

    def parse_expression(self, expression: str) -> tuple[List[int], List[str]]:
        numbers = []
        operators = []
        current_number = 0
        for c in expression:
            if c.isdigit():
                current_number = current_number * 10 + int(c)
            else:
                numbers.append(current_number)
                current_number = 0
                operators.append(c)
        numbers.append(current_number)
        return numbers, operators

    def combine_results(self, left_results: List[int], right_results: List[int], op: str, combined_results: List[int]):
        for left_value in left_results:
            for right_value in right_results:
                result = self.compute_operation(left_value, right_value, op)
                combined_results.append(result)

    def compute_operation(self, left: int, right: int, op: str) -> int:
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        else:
            raise ValueError(f"Invalid operator: {op}")
```

```Go []
const (
	maxExpressionLength = 20
	maxNumber           = 99
)

func diffWaysToCompute(expression string) []int {
	expressionLength := len(expression)
	resultTable := make([][][]int, expressionLength)
	for i := range resultTable {
		resultTable[i] = make([][]int, expressionLength)
	}

	numbers, operators := parseExpression(expression)

	// Initialize base cases (single numbers)
	for i := 0; i < len(numbers); i++ {
		resultTable[i][i] = []int{numbers[i]}
	}

	// Fill the result table
	for subexprLength := 2; subexprLength <= len(numbers); subexprLength++ {
		for start := 0; start+subexprLength <= len(numbers); start++ {
			end := start + subexprLength - 1

			for split := start; split < end; split++ {
				op := operators[split]
				leftResults := resultTable[start][split]
				rightResults := resultTable[split+1][end]

				combineResults(leftResults, rightResults, op, &resultTable[start][end])
			}
		}
	}

	return resultTable[0][len(numbers)-1]
}

func parseExpression(expression string) ([]int, []rune) {
	var numbers []int
	var operators []rune
	currentNumber := 0

	for _, c := range expression {
		if unicode.IsDigit(c) {
			digit, _ := strconv.Atoi(string(c))
			currentNumber = currentNumber*10 + digit
		} else {
			numbers = append(numbers, currentNumber)
			currentNumber = 0
			operators = append(operators, c)
		}
	}
	numbers = append(numbers, currentNumber)

	return numbers, operators
}

func combineResults(leftResults, rightResults []int, op rune, combinedResults *[]int) {
	for _, leftValue := range leftResults {
		for _, rightValue := range rightResults {
			result := computeOperation(leftValue, rightValue, op)
			*combinedResults = append(*combinedResults, result)
		}
	}
}

func computeOperation(left, right int, op rune) int {
	switch op {
	case '+':
		return left + right
	case '-':
		return left - right
	case '*':
		return left * right
	default:
		panic(fmt.Sprintf("Invalid operator: %c", op))
	}
}

```
```Rust []
use std::collections::HashMap;

const MAX_EXPRESSION_LENGTH: usize = 20;
const MAX_NUMBER: i32 = 99;

impl Solution {
    pub fn diff_ways_to_compute(expression: String) -> Vec<i32> {
        let expression_length = expression.len();
        let mut result_table: Vec<Vec<Vec<i32>>> = vec![vec![Vec::new(); expression_length]; expression_length];

        let (numbers, operators) = Self::parse_expression(&expression);
        
        // Initialize base cases (single numbers)
        for i in 0..numbers.len() {
            result_table[i][i] = vec![numbers[i]];
        }
        
        // Fill the result table
        for subexpr_length in 2..=numbers.len() {
            for start in 0..=numbers.len() - subexpr_length {
                let end = start + subexpr_length - 1;
                
                for split in start..end {
                    let operator = operators[split];
                    let left_results = result_table[start][split].clone();
                    let right_results = result_table[split + 1][end].clone();
                    
                    Self::combine_results(&left_results, &right_results, operator, &mut result_table[start][end]);
                }
            }
        }
        
        result_table[0][numbers.len() - 1].clone()
    }

    fn parse_expression(expression: &str) -> (Vec<i32>, Vec<char>) {
        let mut numbers = Vec::new();
        let mut operators = Vec::new();
        let mut current_number = 0;

        for c in expression.chars() {
            if c.is_digit(10) {
                current_number = current_number * 10 + c.to_digit(10).unwrap() as i32;
            } else {
                numbers.push(current_number);
                current_number = 0;
                operators.push(c);
            }
        }
        numbers.push(current_number);

        (numbers, operators)
    }

    fn combine_results(left_results: &[i32], right_results: &[i32], operator: char, combined_results: &mut Vec<i32>) {
        for &left_value in left_results {
            for &right_value in right_results {
                let result = Self::compute_operation(left_value, right_value, operator);
                combined_results.push(result);
            }
        }
    }

    fn compute_operation(left: i32, right: i32, operator: char) -> i32 {
        match operator {
            '+' => left + right,
            '-' => left - right,
            '*' => left * right,
            _ => panic!("Invalid operator: {}", operator),
        }
    }
}
```
```kotlin []
class Solution {
    companion object {
        private const val MAX_EXPRESSION_LENGTH = 20
        private const val MAX_NUMBER = 99
    }

    fun diffWaysToCompute(expression: String): List<Int> {
        val expressionLength = expression.length
        val resultTable = Array(expressionLength) { Array<MutableList<Int>>(expressionLength) { mutableListOf() } }

        val (numbers, operators) = parseExpression(expression)
        
        // Initialize base cases (single numbers)
        for (i in numbers.indices) {
            resultTable[i][i].add(numbers[i])
        }
        
        // Fill the result table
        for (subexprLength in 2..numbers.size) {
            for (start in 0..numbers.size - subexprLength) {
                val end = start + subexprLength - 1
                
                for (split in start until end) {
                    val operator = operators[split]
                    val leftResults = resultTable[start][split]
                    val rightResults = resultTable[split + 1][end]
                    
                    combineResults(leftResults, rightResults, operator, resultTable[start][end])
                }
            }
        }
        
        return resultTable[0][numbers.size - 1]
    }
    
    private fun parseExpression(expression: String): Pair<List<Int>, List<Char>> {
        val numbers = mutableListOf<Int>()
        val operators = mutableListOf<Char>()
        var currentNumber = 0
        
        for (c in expression) {
            if (c.isDigit()) {
                currentNumber = currentNumber * 10 + (c - '0')
            } else {
                numbers.add(currentNumber)
                currentNumber = 0
                operators.add(c)
            }
        }
        numbers.add(currentNumber)
        
        return Pair(numbers, operators)
    }
    
    private fun combineResults(leftResults: List<Int>, rightResults: List<Int>, 
                               operator: Char, combinedResults: MutableList<Int>) {
        for (leftValue in leftResults) {
            for (rightValue in rightResults) {
                val result = computeOperation(leftValue, rightValue, operator)
                combinedResults.add(result)
            }
        }
    }
    
    private fun computeOperation(left: Int, right: Int, operator: Char): Int {
        return when (operator) {
            '+' -> left + right
            '-' -> left - right
            '*' -> left * right
            else -> throw IllegalArgumentException("Invalid operator: $operator")
        }
    }
}
```
```TypeScript []
function diffWaysToCompute(expression: string): number[] {
    const MAX_EXPRESSION_LENGTH: number = 20;
    const MAX_NUMBER: number = 99;

    const expressionLength = expression.length;
    const resultTable: number[][][] = Array(expressionLength).fill(null).map(() => 
        Array(expressionLength).fill(null).map(() => [])
    );

    const [numbers, operators] = parseExpression(expression);
    
    // Initialize base cases (single numbers)
    for (let i = 0; i < numbers.length; i++) {
        resultTable[i][i] = [numbers[i]];
    }
    
    // Fill the result table
    for (let subexprLength = 2; subexprLength <= numbers.length; subexprLength++) {
        for (let start = 0; start + subexprLength <= numbers.length; start++) {
            const end = start + subexprLength - 1;
            
            for (let split = start; split < end; split++) {
                const operator = operators[split];
                const leftResults = resultTable[start][split];
                const rightResults = resultTable[split + 1][end];
                
                combineResults(leftResults, rightResults, operator, resultTable[start][end]);
            }
        }
    }
    
    return resultTable[0][numbers.length - 1];
}

function parseExpression(expression: string): [number[], string[]] {
    const numbers: number[] = [];
    const operators: string[] = [];
    let currentNumber = 0;
    
    for (const c of expression) {
        if (c >= '0' && c <= '9') {
            currentNumber = currentNumber * 10 + (c.charCodeAt(0) - '0'.charCodeAt(0));
        } else {
            numbers.push(currentNumber);
            currentNumber = 0;
            operators.push(c);
        }
    }
    numbers.push(currentNumber);
    
    return [numbers, operators];
}

function combineResults(leftResults: number[], rightResults: number[], 
                        operator: string, combinedResults: number[]): void {
    for (const leftValue of leftResults) {
        for (const rightValue of rightResults) {
            const result = computeOperation(leftValue, rightValue, operator);
            combinedResults.push(result);
        }
    }
}

function computeOperation(left: number, right: number, operator: string): number {
    switch (operator) {
        case '+': return left + right;
        case '-': return left - right;
        case '*': return left * right;
        default: throw new Error(`Invalid operator: ${operator}`);
    }
}
```
```JavaScript []
/**
 * @param {string} expression
 * @return {number[]}
 */
var diffWaysToCompute = function(expression) {
    const MAX_EXPRESSION_LENGTH = 20;
    const MAX_NUMBER = 99;

    const expressionLength = expression.length;
    const resultTable = Array(expressionLength).fill(null).map(() => 
        Array(expressionLength).fill(null).map(() => [])
    );

    const [numbers, operators] = parseExpression(expression);
    
    // Initialize base cases (single numbers)
    for (let i = 0; i < numbers.length; i++) {
        resultTable[i][i] = [numbers[i]];
    }
    
    // Fill the result table
    for (let subexprLength = 2; subexprLength <= numbers.length; subexprLength++) {
        for (let start = 0; start + subexprLength <= numbers.length; start++) {
            const end = start + subexprLength - 1;
            
            for (let split = start; split < end; split++) {
                const operator = operators[split];
                const leftResults = resultTable[start][split];
                const rightResults = resultTable[split + 1][end];
                
                combineResults(leftResults, rightResults, operator, resultTable[start][end]);
            }
        }
    }
    
    return resultTable[0][numbers.length - 1];
};

function parseExpression(expression) {
    const numbers = [];
    const operators = [];
    let currentNumber = 0;
    
    for (const c of expression) {
        if (c >= '0' && c <= '9') {
            currentNumber = currentNumber * 10 + (c.charCodeAt(0) - '0'.charCodeAt(0));
        } else {
            numbers.push(currentNumber);
            currentNumber = 0;
            operators.push(c);
        }
    }
    numbers.push(currentNumber);
    
    return [numbers, operators];
}

function combineResults(leftResults, rightResults, operator, combinedResults) {
    for (const leftValue of leftResults) {
        for (const rightValue of rightResults) {
            const result = computeOperation(leftValue, rightValue, operator);
            combinedResults.push(result);
        }
    }
}

function computeOperation(left, right, operator) {
    switch (operator) {
        case '+': return left + right;
        case '-': return left - right;
        case '*': return left * right;
        default: throw new Error(`Invalid operator: ${operator}`);
    }
}
```

