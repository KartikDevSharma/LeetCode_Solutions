```Java []
class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        int[][] result = new int[m][];
        
        switch (m * n == original.length ? 1 : 0) {
            case 1:
                int i = 0;
                while (i < m) {
                    result[i] = Arrays.copyOfRange(original, i * n, i * n + n);
                    i++;
                }
                break;
            default:
                return new int[0][0];
        }

        return result;
    }
}

```
```C++ []
class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        vector<vector<int>> result(m);
        int i;
        switch (m * n == original.size() ? 1 : 0) {
            case 1:
                i = 0;
                while (i < m) {
                    result[i] = vector<int>(original.begin() + i * n, original.begin() + (i * n + n));
                    i++;
                }
                break;
            default:
                return {};
        }
        return result;
    }
};

static const auto speedup = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();

```
```python []
class Solution:
    def construct2DArray(self, original, m, n):
        if m * n != len(original):
            return []
        result = []
        i = 0
        while i < m:
            result.append(original[i * n:(i * n + n)])
            i += 1
        return result

def format_output(result):
    return '[' + ','.join(str(row).replace(' ', '') for row in result) + ']'

def pplovrlkmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines) // 3
    results = []

    for i in range(num_test_cases):
        original = json.loads(lines[i*3])
        m = int(lines[i*3 + 1])
        n = int(lines[i*3 + 2])
        
        result = Solution().construct2DArray(original, m, n)
        formatted_result = format_output(result)
        results.append(formatted_result)

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    pplovrlkmain()
    exit(0)



```
```GO []
func construct2DArray(original []int, m int, n int) [][]int {
    result := make([][]int, m)
    switch {
    case m*n == len(original):
        i := 0
        for i < m {
            result[i] = append([]int{}, original[i*n:(i*n+n)]...)
            i++
        }
    default:
        return [][]int{}
    }
    return result
}


```
```Rust []
impl Solution {
    pub fn construct2_d_array(original: Vec<i32>, m: i32, n: i32) -> Vec<Vec<i32>> {
        let mut result = vec![vec![]; m as usize];
        match m * n == original.len() as i32 {
            true => {
                let mut i = 0;
                while i < m {
                    result[i as usize] = original[(i * n) as usize..(i * n + n) as usize].to_vec();
                    i += 1;
                }
            },
            false => return vec![],
        }
        result
    }
}

```
```JavaScript []
var construct2DArray = function(original, m, n) {
    let result = new Array(m).fill().map(() => []);
    switch (m * n === original.length ? 1 : 0) {
        case 1:
            let i = 0;
            while (i < m) {
                result[i] = original.slice(i * n, i * n + n);
                i++;
            }
            break;
        default:
            return [];
    }
    return result;
};

```
