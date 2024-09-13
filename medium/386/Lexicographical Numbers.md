### Appraoch 1

```java []
class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> result = new ArrayList<>(n);
        for (int i = 1; i < 10; i++) {
            dfs(i, n, result);
        }
        return result;
    }

    private void dfs(int cur, int n, List<Integer> result) {
        if (cur > n) {
            return;
        }
        result.add(cur);
        for (int i = 0; i < 10; i++) {
            if (10 * cur + i > n) {
                return;
            }
            dfs(10 * cur + i, n, result);
        }
    }
}
//KDS approach 1
```
```C++ []
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> result;
        for (int i = 1; i < 10; i++) {
            dfs(i, n, result);
        }
        return result;
    }

private:
    void dfs(int cur, int n, vector<int>& result) {
        if (cur > n) {
            return;
        }
        result.push_back(cur);
        for (int i = 0; i < 10; i++) {
            if (10 * cur + i > n) {
                return;
            }
            dfs(10 * cur + i, n, result);
        }
    }
};
```
```python []
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(cur, n, result):
            if cur > n:
                return
            result.append(cur)
            for i in range(10):
                if 10 * cur + i > n:
                    return
                dfs(10 * cur + i, n, result)

        result = []
        for i in range(1, 10):
            dfs(i, n, result)
        return result
```

```Go []
func lexicalOrder(n int) []int {
    result := make([]int, 0, n)
    
    var dfs func(cur, n int)
    dfs = func(cur, n int) {
        if cur > n {
            return
        }
        result = append(result, cur)
        for i := 0; i < 10; i++ {
            if 10*cur+i > n {
                return
            }
            dfs(10*cur+i, n)
        }
    }
    
    for i := 1; i < 10; i++ {
        dfs(i, n)
    }
    return result
}
```
```Rust []
impl Solution {
    pub fn lexical_order(n: i32) -> Vec<i32> {
        let mut result = Vec::with_capacity(n as usize);
        
        fn dfs(cur: i32, n: i32, result: &mut Vec<i32>) {
            if cur > n {
                return;
            }
            result.push(cur);
            for i in 0..10 {
                if 10 * cur + i > n {
                    return;
                }
                dfs(10 * cur + i, n, result);
            }
        }
        
        for i in 1..10 {
            dfs(i, n, &mut result);
        }
        result
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function(n) {
    const result = [];
    
    function dfs(cur, n) {
        if (cur > n) {
            return;
        }
        result.push(cur);
        for (let i = 0; i < 10; i++) {
            if (10 * cur + i > n) {
                return;
            }
            dfs(10 * cur + i, n);
        }
    }
    
    for (let i = 1; i < 10; i++) {
        dfs(i, n);
    }
    return result;
};
```


### Appraoch 2

```java []
class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> result = new ArrayList<>(n);
        int current = 1;
        for (int i = 1; i <= n; i++) {
            result.add(current);
            if (current * 10 <= n) {
                current *= 10;
            } else {
                if (current >= n) {
                    current /= 10;
                }
                current++;
                while (current % 10 == 0) {
                    current /= 10;
                }
            }
        }
        return result;
    }
}
//KDS approach 2
```
```C++ []
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> result;
        result.reserve(n);
        int current = 1;
        for (int i = 1; i <= n; i++) {
            result.push_back(current);
            if (current * 10 <= n) {
                current *= 10;
            } else {
                if (current >= n) {
                    current /= 10;
                }
                current++;
                while (current % 10 == 0) {
                    current /= 10;
                }
            }
        }
        return result;
    }
};
```
```python []
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1
        for _ in range(n):
            result.append(current)
            if current * 10 <= n:
                current *= 10
            else:
                if current >= n:
                    current //= 10
                current += 1
                while current % 10 == 0:
                    current //= 10
        return result
```

```Go []
func lexicalOrder(n int) []int {
    result := make([]int, 0, n)
    current := 1
    for i := 1; i <= n; i++ {
        result = append(result, current)
        if current * 10 <= n {
            current *= 10
        } else {
            if current >= n {
                current /= 10
            }
            current++
            for current % 10 == 0 {
                current /= 10
            }
        }
    }
    return result
}
```
```Rust []
impl Solution {
    pub fn lexical_order(n: i32) -> Vec<i32> {
        let mut result = Vec::with_capacity(n as usize);
        let mut current = 1;
        for _ in 1..=n {
            result.push(current);
            if current * 10 <= n {
                current *= 10;
            } else {
                if current >= n {
                    current /= 10;
                }
                current += 1;
                while current % 10 == 0 {
                    current /= 10;
                }
            }
        }
        result
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function(n) {
    const result = [];
    let current = 1;
    for (let i = 1; i <= n; i++) {
        result.push(current);
        if (current * 10 <= n) {
            current *= 10;
        } else {
            if (current >= n) {
                current = Math.floor(current / 10);
            }
            current++;
            while (current % 10 === 0) {
                current = Math.floor(current / 10);
            }
        }
    }
    return result;
};
```
