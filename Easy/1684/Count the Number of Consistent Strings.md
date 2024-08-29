Java
```Java []
class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
      boolean[] occur = new boolean[26];
      int count = 0;

      for(int i = 0;i<allowed.length();i++){
        occur[allowed.charAt(i)-'a'] =true;
      }  

      for(String str: words){

        if(check(str,occur)){
            count++;
        }
      }
      return count;
    }

    boolean check(String str,boolean[]occur){

        for(int i = 0;i<str.length();i++){
            if(occur[str.charAt(i)-'a'] == false){
                return false;
            }
        }
        return true;
    }
}

//https://leetcode.com/problems/count-the-number-of-consistent-strings/submissions/1372105134/
```

C++
```C++ []
class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        vector<bool> occur(26, false);
        int count = 0;
        
        for (char c : allowed) {
            occur[c - 'a'] = true;
        }
        
        for (const string& str : words) {
            if (check(str, occur)) {
                count++;
            }
        }
        return count;
    }
    
private:
    bool check(const string& str, const vector<bool>& occur) {
        for (char c : str) {
            if (!occur[c - 'a']) {
                return false;
            }
        }
        return true;
    }
};

static const auto speedup = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();

//https://leetcode.com/problems/count-the-number-of-consistent-strings/submissions/1372104563/
```


Python
```Python []
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        occur = [False] * 26
        count = 0
        
        for c in allowed:
            occur[ord(c) - ord('a')] = True
        
        for word in words:
            if self.check(word, occur):
                count += 1
        
        return count
    
    def check(self, word: str, occur: List[bool]) -> bool:
        for c in word:
            if not occur[ord(c) - ord('a')]:
                return False
        return True

def main():
    input_data = sys.stdin.read().strip().split('\n')
    results = []
    
    i = 0
    while i < len(input_data):
        allowed = json.loads(input_data[i])
        words = json.loads(input_data[i + 1])
        result = Solution().countConsistentStrings(allowed, words)
        results.append(result)
        i += 2

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()
    exit(0)


#https://leetcode.com/problems/count-the-number-of-consistent-strings/submissions/1372103342/
```
