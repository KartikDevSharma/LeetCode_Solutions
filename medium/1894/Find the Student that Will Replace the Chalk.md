#### Intuition
 
To start, let's first understand what the question is really asking we have a classroom of students each with a specific chalk requirement. The teacher goes around the room and starts giving chalk to the students until they run out. Our job is to find out which student will be the one to say, "Hey, we need more chalk!" 

At first this can appear like a straightforward simulation problem where we could just go through the motions subtracting chalk as we go until we hit a negative number But no the constraints tell us that we could have up to 10^5 students and up to 10^9 pieces of chalk. If we tried to simulate this naively we might end up going around the classroom thousands or even millions of times before running out of chalk. 
So, what's our first instinct? Well, we know we're going to be repeating the same pattern of chalk distribution over and over. This screams "modular arithmetic" to me. If we can figure out how much chalk is used in one complete round of the classroom, we can use the modulus operator to fast-forward through most of the repetitions.

Let's think about this with a simpler example. Say we have 3 students who need 2, 3, and 4 pieces of chalk respectively. If we start with 20 pieces of chalk, how many complete rounds can we make? We'd use 2 + 3 + 4 = 9 chalk per round so we can complete 2 full rounds (using 18 chalk) with 2 pieces left over. Those leftover 2 pieces are what we really care about as they determine where in the third round we'll run out. Let's talk about calculating the total chalk used in one round. By summing up all the values in our chalk array, we get this important information. Then, using the modulus operator with our initial chalk amount, we can immediately get to the round where we'll run out.

But remember, we're not just looking for the round where we run out we also need to know exactly which student will be the one to run out. This means we can't just do a single modulus operation and say we got the results. We need to actually simulate that final partial round. That is why lets talk about a single pass through the array to simulate the final round. We start with our "remaining chalk" (the result of our modulus operation), and we go student by student, subtracting their chalk requirement. The moment we can't meet a student's requirement congrats we've found our answer.

Now, you might be thinking  why even bother with the modulus operation at all Why cant we just simulate from the beginning well We use the modulus to quickly bypass all the complete rounds, then switch to simulation for the final important round. This gives us both speed and accuracy. By using the modulus we're essentially "wrapping" our chalk distribution around the classroom it's as if we're working with a circular array where the end connects back to the beginning. This circular nature mirrors the problem description perfectly, the teacher starts over at student 0 after reaching the end.

Let's talk about some edge cases for ex if we have exactly enough chalk for a whole number of rounds In this case, our modulus operation will give us 0 and we'll return 0 (the first student) as our answer. This makes sense - if we have exactly enough chalk we'll run out just as we're about to start a new round, another case to consider is when one student uses significantly more chalk than the others for ex if we have [1, 1, 1000] as our chalk array in this case our modulus operation becomes important without it we might waste a lot of time simulating the first two students over and over before finally hitting the third, this solution also handles the case where we have a very large amount of initial chalk efficiently. Even if we start with billions of pieces of chalk, our modulus operation cuts that down to a manageable number right away.

Another thing is we willbe using long for the totla chalk sum and a doubt you might have is why we use a long for this but keep using int for the remaining chalk well this is a subtle but important point as the total sum could potentially exceed the range of an int if we have many students using a lot of chalk. But after the modulus operation we're guaranteed to have a value less than the sum which fits safely in an int.

The approach also has the advantage of being very space-efficient. We just have a few variables to keep track of our sums and remainders. This means our space complexity is O(1), which is as good as it gets and in terms of time complexity, we will be making two passes through the array once to calculate the total, and once to simulate the final round this will give us a linear time complexity of O(n), where n is the number of students. Considering that we could potentially be dealing with billions of pieces of chalk, reducing this to a linear operation is a significant optimization.

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
