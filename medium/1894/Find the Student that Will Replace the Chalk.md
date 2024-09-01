```Java []

class Solution {
    public int chalkReplacer(int[] chalk, int initialChalkPieces) {
        long totalChalkNeeded = 0;
        for (int studentChalkUse : chalk) {
            totalChalkNeeded += studentChalkUse;
        }
        
        int remainingChalk = (int)(initialChalkPieces % totalChalkNeeded);
        
        for (int studentIndex = 0; studentIndex < chalk.length; studentIndex++) {
            if (remainingChalk < chalk[studentIndex]) {
                return studentIndex;
            }
            remainingChalk -= chalk[studentIndex];
        }
        
        return 0;  
    }
}

```
```C++ []
class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int initialChalkPieces) {
        long long totalChalkNeeded = 0;
        for (int studentChalkUse : chalk) {
            totalChalkNeeded += studentChalkUse;
        }
        
        int remainingChalk = initialChalkPieces % totalChalkNeeded;
        
        for (int studentIndex = 0; studentIndex < chalk.size(); studentIndex++) {
            if (remainingChalk < chalk[studentIndex]) {
                return studentIndex;
            }
            remainingChalk -= chalk[studentIndex];
        }
        
        return 0;
    }
};


```
```Python []
class Solution:
    def chalkReplacer(self, chalk: List[int], initialChalkPieces: int) -> int:
        totalChalkNeeded = sum(chalk)
        remainingChalk = initialChalkPieces % totalChalkNeeded
        
        for studentIndex, studentChalkUse in enumerate(chalk):
            if remainingChalk < studentChalkUse:
                return studentIndex
            remainingChalk -= studentChalkUse
        
        return 0

# I/O handling
import sys
import json

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines) // 2
    results = []

    for i in range(num_test_cases):
        chalk = json.loads(lines[i*2])
        initialChalkPieces = int(lines[i*2 + 1])
        
        result = Solution().chalkReplacer(chalk, initialChalkPieces)
        results.append(str(result))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)


```
```Go []

func chalkReplacer(chalk []int, initialChalkPieces int) int {
    totalChalkNeeded := 0
    for _, studentChalkUse := range chalk {
        totalChalkNeeded += studentChalkUse
    }
    
    remainingChalk := initialChalkPieces % totalChalkNeeded
    
    for studentIndex, studentChalkUse := range chalk {
        if remainingChalk < studentChalkUse {
            return studentIndex
        }
        remainingChalk -= studentChalkUse
    }
    
    return 0
}

```
```Rust []
impl Solution {
    pub fn chalk_replacer(chalk: Vec<i32>, initial_chalk_pieces: i32) -> i32 {
        let total_chalk_needed: i64 = chalk.iter().map(|&x| x as i64).sum();
        let mut remaining_chalk = (initial_chalk_pieces as i64 % total_chalk_needed) as i32;
        
        for (student_index, &student_chalk_use) in chalk.iter().enumerate() {
            if remaining_chalk < student_chalk_use {
                return student_index as i32;
            }
            remaining_chalk -= student_chalk_use;
        }
        
        0
    }
}


```
```JavaScript []

/**
 * @param {number[]} chalk
 * @param {number} initialChalkPieces
 * @return {number}
 */
var chalkReplacer = function(chalk, initialChalkPieces) {
    let totalChalkNeeded = chalk.reduce((sum, studentChalkUse) => sum + studentChalkUse, 0);
    let remainingChalk = initialChalkPieces % totalChalkNeeded;
    
    for (let studentIndex = 0; studentIndex < chalk.length; studentIndex++) {
        if (remainingChalk < chalk[studentIndex]) {
            return studentIndex;
        }
        remainingChalk -= chalk[studentIndex];
    }
    
    return 0;
};

```


---
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
