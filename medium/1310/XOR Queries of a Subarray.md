```Java []
class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        for(int i =1;i<arr.length;i++){
            arr[i] = arr[i-1]^arr[i];
        }
        int [] xor = new int [queries.length];

        for(int i =0;i<queries.length;i++){
            int l = queries[i][0];
            int r = queries [i][1];
            if(l>0){
                xor[i] = arr[r]^arr[l-1];
            }
            else{
                xor[i] = arr[r];
            }
        }
        return xor;
    }
}

//Kds
```
```C++ []
class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int> result;
        for (int i = 1; i < arr.size(); ++i) {
            arr[i] ^= arr[i - 1];
        }

        for (const auto& q : queries) {
            if (q[0] > 0) {
                result.push_back(arr[q[0] - 1] ^ arr[q[1]]);
            } else {
                result.push_back(arr[q[1]]);
            }
        }

        return result;
    }
};
static const int kds = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();
//KDS
```
```Python []
class Solution:
    def xorQueries(self, arr, queries):
        for i in range(1, len(arr)):
            arr[i] = arr[i-1] ^ arr[i]
        
        xor = []
        for l, r in queries:
            if l > 0:
                xor.append(arr[r] ^ arr[l-1])
            else:
                xor.append(arr[r])
        
        return xor

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
