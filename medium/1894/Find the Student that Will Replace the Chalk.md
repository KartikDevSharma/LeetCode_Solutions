```Java []
class Solution {
    public int chalkReplacer(int[] chalkArray, int totalChalk) {
        return findChalkReplacer(chalkArray, totalChalk);
    }
    
    public int findChalkReplacer(int[] chalkArray, int remainingChalk) {
        long chalkUsed = 0;
        int index = 0;
        
        while (index < chalkArray.length) {
            chalkUsed += chalkArray[index];
            
            switch (Long.compare(remainingChalk, chalkUsed)) {
                case -1:
                    return index;
                case 0:
                    return (index + 1) % chalkArray.length;
            }
            
            index++;
        }
        
        long reducedChalk = remainingChalk % chalkUsed;
        return findChalkReplacer(chalkArray, (int) reducedChalk);
    }
}

```
```C++ []
class Solution {
public:
    int chalkReplacer(vector<int>& pieces, int total) {
        return calculateReplacement(pieces, total);
    }
    
private:
    int calculateReplacement(vector<int>& pieces, long long remaining) {
        long long sum = 0;
        int index = 0;
        while (index < pieces.size()) {
            sum += pieces[index];
            if (remaining - sum < 0) {
                return index;
            }
            index++;
        }
        return calculateReplacement(pieces, remaining % sum);
    }
};
static const auto speedup = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();

```
```Python []

class Solution:
    def chalkReplacer(self, chalkArray: List[int], totalChalk: int) -> int:
        return self.findChalkReplacer(chalkArray, totalChalk)
    
    def findChalkReplacer(self, chalkArray: List[int], remainingChalk: int) -> int:
        chalkUsed = 0
        index = 0
        
        while index < len(chalkArray):
            chalkUsed += chalkArray[index]
            
            comparison = (remainingChalk > chalkUsed) - (remainingChalk < chalkUsed)
            if comparison == -1:
                return index
            elif comparison == 0:
                return (index + 1) % len(chalkArray)
            
            index += 1
        
        reducedChalk = remainingChalk % chalkUsed
        return self.findChalkReplacer(chalkArray, reducedChalk)

```
