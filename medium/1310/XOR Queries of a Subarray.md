```Java []
class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        int n = arr.length;
        int m = queries.length;

        for (int i = 1; i < n; i++) {
            arr[i] ^= arr[i - 1];
        }
        
 
        int[] result = new int[m];
        for (int i = 0; i < m; i++) {
            int start = queries[i][0], end = queries[i][1];
            result[i] = start > 0 ? arr[end] ^ arr[start - 1] : arr[end];
        }
        
        return result;
    }
}

//Kds
```
```C++ []
class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n = arr.size();
        int m = queries.size();
  
        for (int i = 1; i < n; ++i) {
            arr[i] ^= arr[i - 1];
        }

        vector<int> result;
        result.reserve(m);

        for (const auto& q : queries) {
            int start = q[0], end = q[1];
            result.push_back(start > 0 ? arr[end] ^ arr[start - 1] : arr[end]);
        }
        
        return result;
    }
};


static const int KDS = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();
//KDS
```
```Python []
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        
  
        return [arr[end] ^ arr[start - 1] if start > 0 else arr[end] 
                for start, end in queries]

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines) // 2
    results = []

    for i in range(num_test_cases):
        arr = json.loads(lines[i*2])
        queries = json.loads(lines[i*2 + 1])
        
        result = Solution().xorQueries(arr, queries)
        results.append(json.dumps(result, separators=(',', ':')))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)
#Kartikdevsharmaa

```
