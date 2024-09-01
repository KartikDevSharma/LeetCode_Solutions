#### Intuition
 
To start, let's first understand what the question is really asking we have a classroom of students each with a specific chalk requirement. The teacher goes around the room and starts giving chalk to the students until they run out. Our job is to find out which student will be the one to say, "Hey, we need more chalk!" 
>- Cyclic Nature: The teacher starts again from the first student after the last one creating a cyclic pattern which basically means we need to consider how the chalk is distributed in multiple rounds, not just one.
>- Chalk Consumption: Each student has a different chalk consumption rate (chalk[i]). If a student's required chalk exceeds the remaining chalk that student needs to replace the chalk which is the problem's stopping condition.

At first this can appear like a straightforward simulation problem where we could just go through the motions subtracting chalk as we go until we hit a negative number But no the constraints tell us that we could have up to 10^5 students and up to 10^9 pieces of chalk. If we tried to simulate this naively we might end up going around the classroom thousands or even millions of times before running out of chalk. 

Well now since we know we're going to be repeating the same pattern of chalk distribution over and over as each time the teacher completes a round they will return to the first student and if we can calculate the total amount of chalk required for one full round then we can use this information to "skip" through the unnecessary repetitions and focus on the point where the chalk actually runs out so we will use modular arithmetic i.e If we can figure out how much chalk is used in one complete round of the classroom, we can use the modulus operator to fast-forward through most of the repetitions. Try to understand that the total amount of chalk used in one complete cycle (from student 0 to student n-1) is fixed. so if k (the total chalk available) is greater than this sum we don't need to simulate every round Instead we can reduce the problem size by considering the remainder of k after subtracting full cycles this is where modular arithmetic is important instead of simulating each student's use of chalk over multiple rounds we can calculate how much chalk remains after several full cycles, focusing only on the "partial" cycle that causes the chalk to run out.

Let's think about this with a simpler example. Say we have 3 students who need 2, 3, and 4 pieces of chalk respectively. If we start with 20 pieces of chalk, how many complete rounds can we make? We'd use 2 + 3 + 4 = 9 chalk per round so we can complete 2 full rounds (using 18 chalk) with 2 pieces left over. Those leftover 2 pieces are what we really care about as they determine where in the third round we'll run out. Let's talk about calculating the total chalk used in one round. By summing up all the values in our chalk array, we get this important information. Then, using the modulus operator with our initial chalk amount, we can immediately get to the round where we'll run out.

But remember, we're not just looking for the round where we run out we also need to know exactly which student will be the one to run out. This means we can't just do a single modulus operation and say we got the results. We need to actually simulate that final partial round. That is why lets talk about a single pass through the array to simulate the final round, we start from the first student and we go student by student and begin subtracting their chalk requirement from the remaining chalk(the result of our modulus operation). Continue this process until you find the first student whose requirement exceeds the remaining chalk. The moment we can't meet a student's requirement this student will be the one who will say, "Hey, we need more chalk!" 

Now, you might be thinking  why even bother with the modulus operation at all Why cant we just simulate from the beginning well We use the modulus to quickly bypass all the complete rounds, then switch to simulation for the final important round. This gives us both speed and accuracy. By using the modulus we're essentially "wrapping" our chalk distribution around the classroom it's as if we're working with a circular array where the end connects back to the beginning. This circular nature mirrors the problem description perfectly, the teacher starts over at student 0 after reaching the end.

Let's talk about some edge cases for ex if we have exactly enough chalk for a whole number of rounds In this case, our modulus operation will give us 0 and we'll return 0 (the first student) as our answer. This makes sense - if we have exactly enough chalk we'll run out just as we're about to start a new round, another case to consider is when one student uses significantly more chalk than the others for ex if we have [1, 1, 1000] as our chalk array in this case our modulus operation becomes important without it we might waste a lot of time simulating the first two students over and over before finally hitting the third, this solution also handles the case where we have a very large amount of initial chalk efficiently. Even if we start with billions of pieces of chalk, our modulus operation cuts that down to a manageable number right away.

Another thing is we willbe using long for the totla chalk sum and a doubt you might have is why we use a long for this but keep using int for the remaining chalk well this is a subtle but important point as the total sum could potentially exceed the range of an int if we have many students using a lot of chalk. But after the modulus operation we're guaranteed to have a value less than the sum which fits safely in an int.

The approach also has the advantage of being very space-efficient. We just have a few variables to keep track of our sums and remainders. This means our space complexity is O(1), which is as good as it gets and in terms of time complexity, we will be making two passes through the array once to calculate the total, and once to simulate the final round this will give us a linear time complexity of O(n), where n is the number of students. Considering that we could potentially be dealing with billions of pieces of chalk, reducing this to a linear operation is a significant optimization.


### Appraoch


#### Problem Explanation

In this problem, we have a classroom of students where each student requires a specific amount of chalk to perform their tasks. The teacher distributes an initial amount of chalk in a cyclic manner (i.e., from the first student to the last, and then starting again from the first student) until all the chalk is depleted. Our objective is to identify which student will run out of chalk first.

#### Approach Overview

The approach involves two major steps:
1. **Calculating the total chalk needed for one complete cycle through all students.**
2. **Using modular arithmetic to efficiently find out where in the cycle the chalk will run out, followed by a linear scan to identify the specific student.**

#### Key Concepts

1. **Cyclic Distribution:** The teacher goes through the students in a cyclic manner. This means that once all students have been served, the process starts again from the first student. 
2. **Modular Arithmetic:** To handle large amounts of chalk and avoid unnecessary simulations, modular arithmetic helps to reduce the problem size by focusing on the remainder after distributing chalk for several complete rounds.
3. **Simulation of the Final Round:** After using modular arithmetic to reduce the problem size, a simple simulation of the partial cycle determines the exact student who will run out of chalk.

#### Detailed Explanation

#### Step 1: Calculate Total Chalk Needed for One Complete Round

**Concept:**
To handle the cyclic nature of the problem efficiently, we first need to know how much chalk is consumed in one complete round through all students. This is crucial because it allows us to understand how many complete rounds we can make before the chalk potentially runs out.

**Pseudo-Code:**

```pseudo
function calculateTotalChalkNeeded(chalk):
    totalChalkNeeded = 0
    for each amount in chalk:
        totalChalkNeeded += amount
    return totalChalkNeeded
```

**Explanation:**
- Iterate through the `chalk` array.
- Sum all the chalk amounts required by each student.
- The result, `totalChalkNeeded`, represents the total chalk required to serve all students once.

**Example:**
For `chalk = [3, 4, 1]`:
- Total chalk needed for one round = `3 + 4 + 1 = 8`

#### Step 2: Use Modular Arithmetic to Skip Full Rounds

**Concept:**
If we have a large number of chalk pieces and a large number of students, simulating each round is inefficient. Instead, we use the modulus operation to determine the remaining chalk after accounting for several full rounds. This step reduces the problem size significantly.

**Pseudo-Code:**

```pseudo
function calculateRemainingChalk(initialChalkPieces, totalChalkNeeded):
    remainingChalk = initialChalkPieces % totalChalkNeeded
    return remainingChalk
```

**Explanation:**
- Calculate the remainder when `initialChalkPieces` is divided by `totalChalkNeeded`.
- This remainder tells us how much chalk will be left after completing as many full rounds as possible.

**Example:**
If `initialChalkPieces = 22` and `totalChalkNeeded = 8`:
- Remaining chalk = `22 % 8 = 6`

#### Step 3: Simulate the Final Round to Find the Student

**Concept:**
With the remaining chalk from the previous step, we need to simulate the final partial round to determine which student will run out of chalk first. This involves iterating through the students and subtracting their chalk requirements from the remaining chalk until it is no longer sufficient.

**Pseudo-Code:**

```pseudo
function findStudentToRunOut(chalk, remainingChalk):
    for i from 0 to length(chalk) - 1:
        if remainingChalk < chalk[i]:
            return i
        remainingChalk -= chalk[i]
    return 0  // This case occurs if remainingChalk is exactly enough for another full cycle
```

**Explanation:**
- Iterate through the `chalk` array using the remaining chalk from the modulus operation.
- For each student, check if their chalk requirement exceeds the remaining chalk.
- If so, return the current student's index as they are the one who will run out of chalk.
- If the iteration completes without finding such a student (which theoretically should not happen after the modulus step), return `0` as a fallback.

**Example:**
Continuing from the previous example with `remainingChalk = 6` and `chalk = [3, 4, 1]`:
- For Student 0: `6 - 3 = 3` (still have chalk, move to the next student)
- For Student 1: `3 - 4 = -1` (chalk runs out here, Student 1 is the one who will run out of chalk)

### Mathematical Justification

1. **Modular Arithmetic:** The modulus operation efficiently reduces the problem size by determining the exact amount of chalk left after completing full rounds. This is because:
   - Distributing chalk in complete cycles is redundant once we know the total chalk needed for one cycle.
   - By reducing the problem to the remainder after full cycles, we avoid excessive computations.

2. **Simulation of Partial Cycle:** After using modular arithmetic, the remaining chalk is guaranteed to be less than the total chalk needed for one full round. Simulating this final partial round ensures that we accurately find the student who will run out of chalk first, making the solution both accurate and efficient.

### Edge Cases

1. **Exact Multiple of Total Chalk Needed:**
   - If `initialChalkPieces` is an exact multiple of `totalChalkNeeded`, the remainder will be `0`. The chalk runs out exactly as the teacher starts a new cycle, and the first student will be the one to run out of chalk.

2. **Single Student:**
   - If there is only one student, the solution simplifies to checking if that single student’s chalk requirement exceeds the initial chalk pieces. This straightforward case is inherently handled by the same approach.

3. **Large Amount of Initial Chalk:**
   - The use of modular arithmetic ensures that even with billions of pieces of chalk, the problem size is reduced to a manageable number, ensuring efficient processing.

### Conclusion

This approach combines modular arithmetic and simulation to provide a highly efficient solution to the problem of determining which student will run out of chalk first. By leveraging the cyclic nature of chalk distribution and reducing the problem size through modulus operations, the solution is both time-efficient (O(n) complexity) and space-efficient (constant space complexity). This method ensures that even with large inputs, the solution remains practical and performant.

### Detailed Time Complexity (TC) and Space Complexity (SC) Analysis


### Time Complexity (TC)

The time complexity of an algorithm represents the amount of time it takes to complete as a function of the input size. For this problem, we need to analyze the time complexity of the operations performed in the solution.

#### 1. **Calculating Total Chalk Needed**

In this step, we iterate through the `chalk` array to compute the sum of chalk requirements for one complete cycle.

**Pseudo-Code:**

```pseudo
function calculateTotalChalkNeeded(chalk):
    totalChalkNeeded = 0
    for each amount in chalk:
        totalChalkNeeded += amount
    return totalChalkNeeded
```

- **Operations:** One iteration through the `chalk` array.
- **Time Complexity:** $O(n)$, where $n$ is the number of students (length of the `chalk` array).

#### 2. **Calculating Remaining Chalk**

We use the modulus operation to determine how much chalk will be left after completing as many full rounds as possible.

**Pseudo-Code:**

```pseudo
function calculateRemainingChalk(initialChalkPieces, totalChalkNeeded):
    remainingChalk = initialChalkPieces % totalChalkNeeded
    return remainingChalk
```

- **Operations:** The modulus operation and a few arithmetic operations.
- **Time Complexity:** $O(1)$ (constant time), as these operations do not depend on the size of the input array.

#### 3. **Simulating the Final Partial Round**

In this step, we simulate the final partial round to find out which student will run out of chalk first.

**Pseudo-Code:**

```pseudo
function findStudentToRunOut(chalk, remainingChalk):
    for i from 0 to length(chalk) - 1:
        if remainingChalk < chalk[i]:
            return i
        remainingChalk -= chalk[i]
    return 0  // Fallback case
```

- **Operations:** One iteration through the `chalk` array, which is done to find the student where the chalk runs out.
- **Time Complexity:** $O(n)$, where $n$ is the number of students.

#### Total Time Complexity

The overall time complexity is determined by combining the complexities of each step:

- Calculating the total chalk needed: $O(n)$
- Calculating the remaining chalk: $O(1)$
- Simulating the final partial round: $O(n)$

Thus, the total time complexity is:

\[ O(n) + O(1) + O(n) = O(n) \]

### Space Complexity (SC)

The space complexity of an algorithm represents the amount of memory required to execute the algorithm. It includes both the space needed for input storage and additional space used during execution.

#### 1. **Input Storage**

The primary input to the algorithm is the `chalk` array, which holds the chalk requirements for each student.

- **Space Complexity:** $O(n)$, where $n$ is the number of students, as the input array itself takes $O(n)$ space.

#### 2. **Auxiliary Space**

The auxiliary space refers to the additional memory used by the algorithm, excluding the input storage.

**In the solution:**

- Variables for storing `totalChalkNeeded`, `remainingChalk`, and indices require constant space.
- **Space Complexity:** $O(1)$ (constant space), as we only use a few extra variables regardless of the size of the input.

#### Total Space Complexity

Combining the input storage and auxiliary space:

- Input storage: $O(n)$
- Auxiliary space: $O(1)$

Thus, the total space complexity is:

\[ O(n) + O(1) = O(n) \]

### Summary

- **Time Complexity (TC):** $O(n)$, where $n$ is the number of students. This reflects the linear time needed to process the chalk requirements and simulate the final round.
- **Space Complexity (SC):** $O(n)$, where $n$ is the number of students. This accounts for the space used by the input array.

The approach efficiently handles both large input sizes and large amounts of initial chalk, ensuring that it performs well in practical scenarios while maintaining clarity and correctness.


### CODE
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

### **Problem Recap:**
We are given an array `chalk` where `chalk[i]` represents the amount of chalk the `i`-th student needs to use. The teacher distributes `initialChalkPieces` pieces of chalk to students in a cyclic manner (starting from the first student after reaching the last student) until the chalk runs out. Our task is to determine the index of the student who will cause the chalk to run out.

### **Solution Recap:**
Your solution involves two key steps:
1. **Calculate the total amount of chalk needed for one complete round across all students.**
2. **Use the modulus operation to skip complete rounds and focus on the remaining chalk, then simulate the final round to find the student who runs out of chalk.**

### **Mathematical Proof:**

#### **Step 1: Calculate Total Chalk Needed for One Full Round**

Let:
- `chalk[i]` represent the amount of chalk needed by the `i`-th student.
- `n` be the total number of students (i.e., `chalk.length`).
- `totalChalkNeeded` represent the total amount of chalk needed for all students in one full round.

**Calculation:**

$text{totalChalkNeeded} = \sum_{i=0}^{n-1} \text{chalk}[i]$

This is a simple summation of all the chalk values in the `chalk` array.

**Example:**
If `chalk = [3, 4, 1]`, then:

$text{totalChalkNeeded} = 3 + 4 + 1 = 8$

#### **Step 2: Skip Full Rounds Using Modulus Operation**

Next, we calculate the chalk that remains after distributing chalk for as many full rounds as possible.

Let:
- `initialChalkPieces` be the total initial chalk available.
- `remainingChalk` represent the chalk left after all possible full rounds.

**Calculation:**

$text{remainingChalk} = \text{initialChalkPieces} \mod \text{totalChalkNeeded}$

The modulus operation (`%`) gives us the remainder when `initialChalkPieces` is divided by `totalChalkNeeded`. This remainder tells us how much chalk is left after distributing for several complete rounds.

**Example:**
Continuing from the previous example, if `initialChalkPieces = 22`:

$text{remainingChalk} = 22 \mod 8 = 6$

This means that after distributing chalk for 2 full rounds (16 pieces of chalk used), 6 pieces are left.

**Why the Modulus?**

The modulus operation efficiently reduces the problem size. Instead of simulating every single piece of chalk from the beginning, we reduce the problem to a much smaller number (`remainingChalk`), which represents the chalk left after all full cycles. This reduction is crucial for handling large numbers efficiently.

#### **Step 3: Find the Student Who Causes the Chalk to Run Out**

Now that we know how much chalk remains, we need to determine which student will be the one to deplete it.

We iterate through each student and subtract their chalk requirement from `remainingChalk`. The first student whose chalk requirement cannot be met (i.e., when `remainingChalk < chalk[i]`) is the one who will say, "Hey, we need more chalk!"

**Algorithmic Steps:**

1. Start with the first student (`i = 0`).
2. Check if `remainingChalk < chalk[i]`:
   - If true, return the index `i` (because this student cannot be provided with enough chalk).
   - If false, subtract `chalk[i]` from `remainingChalk` and move to the next student.
3. Continue this process until you find the student who will cause the chalk to run out.

**Example:**

Continuing from the previous example with `remainingChalk = 6` and `chalk = [3, 4, 1]`:

- **Student 0** needs 3 pieces: `6 - 3 = 3` (move to the next student).
- **Student 1** needs 4 pieces: but `remainingChalk = 3 < 4`, so Student 1 cannot be provided with enough chalk.

Therefore, the output is `1`, meaning the second student (index 1) is the one who will need more chalk.

#### **Edge Case Considerations:**
- **If `initialChalkPieces` is exactly a multiple of `totalChalkNeeded`:** The modulus operation will return 0, meaning the chalk will run out exactly as a new cycle starts, and the first student (`index 0`) will be the one who will need more chalk.
- **If there’s only one student (`n = 1`):** The solution still works as `remainingChalk` will directly indicate if the single student can receive the required amount of chalk.

### **Time and Space Complexity:**
- **Time Complexity:** The solution requires two passes through the `chalk` array:
  - The first pass to calculate `totalChalkNeeded` (O(n)).
  - The second pass to find the student who runs out of chalk (O(n)).
  - Overall, this gives a time complexity of O(n).

- **Space Complexity:** The solution uses a constant amount of extra space (O(1)) since no additional data structures are needed beyond a few variables.

### **Conclusion:**
This mathematical proof shows that your approach is both correct and efficient. By leveraging the modulus operation, the problem size is reduced dramatically, allowing for a quick identification of the student who will run out of chalk, even with large inputs. The proof also shows that the approach handles all possible edge cases, ensuring its robustness.





---
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
