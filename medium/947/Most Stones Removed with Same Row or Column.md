

# Intuition


## The Problem at Hand

Imagine we're playing a peculiar game on a giant chessboard. We've scattered stones across this board, each occupying its own square. Now, here's the twist: we can remove a stone if - and only if - there's another stone in the same row or column. Our goal? Remove as many stones as possible.

At first glance, this seems straightforward. Just keep removing stones that share rows or columns until you can't anymore, right? But hold on - the order in which we remove stones matters. Make the wrong choice early on, and we might leave stones stranded, unable to be removed. 

We're dealing with up to 1000 stones here, spread across a board that's 10,000 squares on each side. That's a lot of possibilities to consider. How do we ensure we're making the optimal choices?


### The Brute Force Approach

My first instinct was to tackle this head-on. "Let's just try all possible removal sequences!" I thought. We could start with any stone, remove it if possible, and then recursively try removing the rest. By exploring all paths, we'd surely find the optimal solution.

But wait a minute. With up to 1000 stones, the number of possible removal sequences is astronomical. We're talking about a factorial growth in possibilities. Even for a modest number of stones, this approach would take an eternity. Clearly, we need to be smarter about this.

### Visualizing Connections

As I looked at the problem, I started to visualize the stones and their relationships. In my mind's eye, I saw lines connecting stones in the same rows and columns, forming a intricate web across the board. This mental image was a crucial moment - it reminded me of graphs I'd worked with before.

What if, instead of thinking about individual stones, we considered these connections? After all, the ability to remove a stone depends entirely on its connections to other stones. This shift in perspective was the first step towards a more efficient solution.

### The Graph Analogy

With this new viewpoint, our chessboard transformed into a graph. Each stone became a node, and the shared rows and columns became edges connecting these nodes. Suddenly, our problem looked a lot like finding connected components in a graph.

Why is this important? Well, think about it. In a connected group of stones, we can remove all but one of them. The last one has to stay because it no longer shares a row or column with any other stone - all its "friends" have been removed.

This realization was a game-changer. Instead of focusing on the sequence of removals, we could focus on identifying these connected groups. The maximum number of removable stones would be the total number of stones minus the number of these groups (since we have to leave one stone per group).

### The DFS Attempt

With the help of this graph analogy, my next thought was to use depth-first search (DFS). It's a classic algorithm for exploring graphs, after all. We could start at any stone, use DFS to find all connected stones, mark them for removal, and repeat until we've covered the entire board.

This approach had promise. It would correctly identify the connected components and give us the right answer. But as I started to think about implementation, a question nagged at me: how would we efficiently find all stones in the same row or column?

We could maintain lists of stones for each row and column, but that would require a lot of memory and time to set up. Or we could scan through all stones for each DFS step, but that would be slow for a large number of stones. There had to be a better way.

### The Disjoint Set Union Epiphany

As I was struggling with the efficiency problem of DFS, I remembered the Disjoint Set Union (DSU) data structure, also known as Union-Find. DSU is fantastic at efficiently grouping elements and determining whether two elements belong to the same group.

But how could we apply DSU to our stone removal problem? The key insight came when I shifted my perspective once again. Instead of thinking about stones as the primary elements, what if we considered rows and columns as the elements to be grouped?

This was the "aha" moment. Every stone, by its very position, connects a row with a column. If we treat rows and columns as the elements in our DSU, then placing a stone is equivalent to unioning (merging) a row group with a column group.

### Representing Rows and Columns

With this new approach in mind, a new challenge emerged: how do we represent rows and columns in a way that doesn't confuse them? We can't use the same numbering system for both, as that would muddle our groups.

The solution was elegantly simple: offset the column values by a large number. By adding 10,001 (just beyond the maximum row value) to each column number, we effectively create two separate ranges - one for rows and one for columns. This allows our DSU structure to treat them as distinct elements while still maintaining their relationships.

### Tracking Components

As I developed this idea further, I realized we needed to keep careful track of the number of unique components. Each new row or column encountered would start as its own component. As we process the stones, these components would merge. The final number of components would be crucial in determining how many stones we could remove.

This tracking mechanism solves our problem beautifully. We start with zero components. Each time we encounter a new row or column, we increment our count. Each time we merge two components (by placing a stone), we decrement the count. In the end, the count gives us the number of connected components in our graph.

### Handling Edge Cases

No solution is complete without considering edge cases. What if all stones are in the same row? In this scenario, we'd have two components - the row and the column - and we could remove all but one stone. What if no stones share any rows or columns? Then each stone would be its own component, and we couldn't remove any.

The beauty of our DSU approach is that it handles these cases automatically. Whether we have one large group or many small ones, the component count will accurately reflect the situation.


**Mathematical Intuition for the DSU Approach:**

Let's consider the problem as a graph, where each stone represents a node, and two nodes are connected if they share the same row or column. Mathematically, we can define the stone positions as a set $S = \{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}$. 

To analyze the problem, imagine two functions: $f_r(x, y) = x$ and $f_c(x, y) = y + k$, where $k$ is a large constant (in our case, 10001). These functions map the 2D coordinates of stones into a 1D space, separating rows and columns. Applying these functions to the set $S$, we get two new sets: $R = \{f_r(x, y) \mid (x, y) \in S\}$ and $C = \{f_c(x, y) \mid (x, y) \in S\}$, representing all unique rows and columns.

Now, the union of these sets $U = R \cup C$ captures all unique rows and columns as if they were part of a larger "super set." The DSU structure operates on this set $U$, merging elements as we process each stone. The key insight here is that the number of connected components in this graph is given by $|U| - (|R \cup C| - |S|)$, where $|R \cup C|$ represents the total number of unique rows and columns.

This brings us to a critical realization: the number of stones we can remove is $|S| - (|R| + |C| - (|R \cup C| - |S|)) = 2|S| - |R \cup C|$. In simpler terms, $|S| - |U| + 1$ gives the number of stones that can be removed, because $|U|$ represents the number of connected components, and in each component, we can remove all but one stone. This formulation elegantly shows how we've transformed a 2D problem into a 1D set operation, allowing us to efficiently count the number of removable stones.




This final approach, using DSU with rows and columns as elements, is superior to our earlier attempts in several ways:

1. **Efficiency**: We process each stone exactly once, performing constant-time DSU operations for each. This scales well even for the maximum input size of 1000 stones.

2. **Simplicity**: We've eliminated the need to explicitly track connections between stones. The row-column unions implicitly capture all necessary relationships.

3. **Elegance**: By focusing on components rather than removal sequences, we've simplified the problem. The solution emerges naturally from the structure we've created.

4. **Flexibility**: This approach handles all possible configurations of stones, from highly connected to completely disconnected, without any special cases.

5. **Insight**: It provides a deeper understanding of the problem's structure, revealing that the key is in the connections, not the stones themselves.

The journey from brute force to this DSU solution mirrors a common pattern in algorithm design: moving from a direct, intuitive approach to a more abstract but more powerful representation of the problem. By reconceptualizing the stones as connections between rows and columns, we've transformed a complex sequence problem into an elegant grouping problem.

This solution method doesn't just solve the problem; it reframes our understanding of it. And that's the hallmark of a truly insightful algorithm - it doesn't just compute the answer, it changes how we think about the question.


### Approach

Let's break it down in detail:

1. **Data Structure Initialization:**
   - We create an array `setRepresentatives` of size 20003. Why this specific size?
     * Rows are represented by indices 1 to 10001 (adding 1 to avoid using index 0)
     * Columns are represented by indices 10002 to 20002 (adding 10002 to differentiate from rows)
     * This allows us to handle the maximum possible coordinate value of 10000 for both rows and columns
   - We initialize a `connectedComponentCount` to 0. This will keep track of the number of unique components in our DSU structure.

2. **Stone Processing:**
   For each stone, we perform the following steps:
   - Convert the row coordinate to a unique identifier: `rowElement = stonePosition[0] + 1`
     * Adding 1 ensures we don't use index 0, which we reserve to indicate an uninitialized state
   - Convert the column coordinate to a unique identifier: `columnElement = stonePosition[1] + 10002`
     * Adding 10002 shifts all column identifiers above the range used for rows, preventing any overlap
   - Call `mergeComponents(rowElement, columnElement, setRepresentatives)`
     * This step connects the row and column of the current stone

3. **The `findRepresentative` Method:**
   This method is the core of our DSU structure. It does three crucial things:
   a) Initializes new elements:
      - If `setRepresentatives[element] == 0`, it means we've encountered this element for the first time
      - We set it as its own representative: `setRepresentatives[element] = element`
      - We increment `connectedComponentCount`, as we've found a new unique component
   b) Finds the representative of a set:
      - If an element is its own representative (`setRepresentatives[element] == element`), we return it
      - Otherwise, we recursively find the representative of its parent
   c) Implements path compression:
      - After finding the true representative, we update `setRepresentatives[element]` to point directly to it
      - This flattens the tree structure, optimizing future lookups

4. **The `mergeComponents` Method:**
   This method connects two elements (in our case, a row and a column). Here's what it does:
   - Find the representatives of both elements using `findRepresentative`
   - If the representatives are different (i.e., the elements are in different sets):
     * We merge the sets by making one representative point to the other: `setRepresentatives[repB] = repA`
     * We decrement `connectedComponentCount`, as two components have become one

5. **Result Calculation:**
   - The total number of stones that can be removed is the difference between the total number of stones and the number of connected components
   - This works because in each connected component, we can remove all stones except one

By representing rows and columns as separate elements in our DSU structure, we automatically connect all stones that share a row or column. When we merge a row and column, we're effectively saying "all stones in this row are connected to all stones in this column."

Let's walk through an example:

Suppose we have stones at (0,0), (0,1), and (1,0).

1. For (0,0):
   - We merge row 1 (0+1) and column 10002 (0+10002)
   - These are new elements, so we create two components and immediately merge them

2. For (0,1):
   - We merge row 1 (0+1) and column 10003 (1+10002)
   - Row 1 is already in a component, but column 10003 is new
   - We create a new component for 10003 and merge it with the existing component of row 1

3. For (1,0):
   - We merge row 2 (1+1) and column 10002 (0+10002)
   - Row 2 is new, but column 10002 is already in a component
   - We create a new component for row 2 and merge it with the existing component of column 10002

At the end of this process, all three stones are in a single connected component, even though we never directly connected (0,1) and (1,0). This because of our row-and-column representation.

This approach  solves the problem without need for explicit graph construction or DFS traversal, making it both time and space efficient.

Pseudo-code for the main algorithm:

```
function removeStones(stonePositions):
    setRepresentatives = new array of size 20003, initialized with 0s
    connectedComponentCount = 0
    
    for each stonePosition in stonePositions:
        rowElement = stonePosition[0] + 1
        columnElement = stonePosition[1] + 10002
        mergeComponents(rowElement, columnElement, setRepresentatives)
    
    return length of stonePositions - connectedComponentCount

function findRepresentative(element, setRepresentatives):
    if setRepresentatives[element] == 0:
        setRepresentatives[element] = element
        connectedComponentCount++
    
    if setRepresentatives[element] == element:
        return element
    else:
        setRepresentatives[element] = findRepresentative(setRepresentatives[element], setRepresentatives)
        return setRepresentatives[element]

function mergeComponents(elementA, elementB, setRepresentatives):
    repA = findRepresentative(elementA, setRepresentatives)
    repB = findRepresentative(elementB, setRepresentatives)
    
    if repA != repB:
        setRepresentatives[repB] = repA
        connectedComponentCount--
```



### Complexity

* **Time complexity: $O(n * α(n))$**
where n is the number of stones and α is the inverse Ackermann function. 
  - We iterate through each stone once, performing two find operations and potentially one union operation for each stone.
  - The find and union operations have an amortized time complexity of O(α(n)), which is effectively constant for all practical values of n.
  - Therefore, the overall time complexity is nearly linear in the number of stones.

* **Space complexity: $O(m)$**
where m is the maximum possible coordinate value (10000 in this case).
  - We use an array of size 20003 to represent all possible row and column values.
  - The space used is constant relative to the number of stones, but depends on the range of coordinate values.

### Code
# Code
```java []
class Solution {
    private int connectedComponentCount = 0;

    public int removeStones(int[][] stonePositions) {
        int[] setRepresentatives = new int[20003];
        for (int[] stonePosition : stonePositions) {
            mergeComponents(stonePosition[0] + 1, stonePosition[1] + 10002, setRepresentatives);
        }
        return stonePositions.length - connectedComponentCount;
    }

    private int findRepresentative(int element, int[] setRepresentatives) {
        if (setRepresentatives[element] == 0) {
            setRepresentatives[element] = element;
            connectedComponentCount++;
        }
        return setRepresentatives[element] == element ? element : 
               (setRepresentatives[element] = findRepresentative(setRepresentatives[element], setRepresentatives));
    }

    private void mergeComponents(int elementA, int elementB, int[] setRepresentatives) {
        int repA = findRepresentative(elementA, setRepresentatives);
        int repB = findRepresentative(elementB, setRepresentatives);
        if (repA != repB) {
            setRepresentatives[repB] = repA;
            connectedComponentCount--;
        }
    }
}


//https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/submissions/1366056664/

```
```C++ []
class Solution {
private:
    int connectedComponentCount = 0;

    int findRepresentative(int element, vector<int>& setRepresentatives) {
        if (setRepresentatives[element] == 0) {
            setRepresentatives[element] = element;
            connectedComponentCount++;
        }
        return setRepresentatives[element] == element ? element : 
               (setRepresentatives[element] = findRepresentative(setRepresentatives[element], setRepresentatives));
    }

    void mergeComponents(int elementA, int elementB, vector<int>& setRepresentatives) {
        int repA = findRepresentative(elementA, setRepresentatives);
        int repB = findRepresentative(elementB, setRepresentatives);
        if (repA != repB) {
            setRepresentatives[repB] = repA;
            connectedComponentCount--;
        }
    }

public:
    int removeStones(vector<vector<int>>& stonePositions) {
        vector<int> setRepresentatives(20003, 0);
        for (const auto& stonePosition : stonePositions) {
            mergeComponents(stonePosition[0] + 1, stonePosition[1] + 10002, setRepresentatives);
        }
        return stonePositions.size() - connectedComponentCount;
    }
};

//https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/submissions/1366320221/

```

```Python []
class Solution:
    def __init__(self):
        self.connected_component_count = 0

    def removeStones(self, stone_positions: List[List[int]]) -> int:
        set_representatives = [0] * 20003
        for stone_position in stone_positions:
            self.merge_components(stone_position[0] + 1, stone_position[1] + 10002, set_representatives)
        return len(stone_positions) - self.connected_component_count

    def find_representative(self, element: int, set_representatives: List[int]) -> int:
        if set_representatives[element] == 0:
            set_representatives[element] = element
            self.connected_component_count += 1
        if set_representatives[element] != element:
            set_representatives[element] = self.find_representative(set_representatives[element], set_representatives)
        return set_representatives[element]

    def merge_components(self, element_a: int, element_b: int, set_representatives: List[int]) -> None:
        rep_a = self.find_representative(element_a, set_representatives)
        rep_b = self.find_representative(element_b, set_representatives)
        if rep_a != rep_b:
            set_representatives[rep_b] = rep_a
            self.connected_component_count -= 1


#https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/submissions/1366320771/

```

```Go []
func removeStones(stones [][]int) int {
    connectedComponentCount := 0
    setRepresentatives := make(map[int]int)

    var findRepresentative func(int) int
    findRepresentative = func(element int) int {
        if _, exists := setRepresentatives[element]; !exists {
            setRepresentatives[element] = element
            connectedComponentCount++
        }
        if setRepresentatives[element] != element {
            setRepresentatives[element] = findRepresentative(setRepresentatives[element])
        }
        return setRepresentatives[element]
    }

    mergeComponents := func(elementA, elementB int) {
        repA := findRepresentative(elementA)
        repB := findRepresentative(elementB)
        if repA != repB {
            setRepresentatives[repB] = repA
            connectedComponentCount--
        }
    }

    for _, stone := range stones {
        mergeComponents(stone[0]+1, stone[1]+10002)
    }

    return len(stones) - connectedComponentCount
}

//https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/submissions/1366539966/
```

```Rust []
impl Solution {
    pub fn remove_stones(stones: Vec<Vec<i32>>) -> i32 {
        let mut connected_component_count = 0;
        let mut set_representatives = std::collections::HashMap::new();

        fn find_representative(element: i32, set_representatives: &mut std::collections::HashMap<i32, i32>, connected_component_count: &mut i32) -> i32 {
            if !set_representatives.contains_key(&element) {
                set_representatives.insert(element, element);
                *connected_component_count += 1;
            }
            let rep = *set_representatives.get(&element).unwrap();
            if rep != element {
                let new_rep = find_representative(rep, set_representatives, connected_component_count);
                set_representatives.insert(element, new_rep);
                new_rep
            } else {
                element
            }
        }

        fn merge_components(element_a: i32, element_b: i32, set_representatives: &mut std::collections::HashMap<i32, i32>, connected_component_count: &mut i32) {
            let rep_a = find_representative(element_a, set_representatives, connected_component_count);
            let rep_b = find_representative(element_b, set_representatives, connected_component_count);
            if rep_a != rep_b {
                set_representatives.insert(rep_b, rep_a);
                *connected_component_count -= 1;
            }
        }

        for stone in stones.iter() {
            merge_components(stone[0] + 1, stone[1] + 10002, &mut set_representatives, &mut connected_component_count);
        }

        stones.len() as i32 - connected_component_count
    }
}

//https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/submissions/1366539101/
```

```JavaScript []
/**
 * @param {number[][]} stones
 * @return {number}
 */
var removeStones = function(stones) {
    let connectedComponentCount = 0;
    const setRepresentatives = new Map();

    const findRepresentative = (element) => {
        if (!setRepresentatives.has(element)) {
            setRepresentatives.set(element, element);
            connectedComponentCount++;
        }
        if (setRepresentatives.get(element) !== element) {
            setRepresentatives.set(element, findRepresentative(setRepresentatives.get(element)));
        }
        return setRepresentatives.get(element);
    };

    const mergeComponents = (elementA, elementB) => {
        const repA = findRepresentative(elementA);
        const repB = findRepresentative(elementB);
        if (repA !== repB) {
            setRepresentatives.set(repB, repA);
            connectedComponentCount--;
        }
    };

    for (const [x, y] of stones) {
        mergeComponents(x + 1, y + 10002);
    }

    return stones.length - connectedComponentCount;
};

//https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/submissions/1366536542/

```
---

Lets take example 1 from problem to understant this better
### **Given Stones**
- Stones are located at: \((0,0), (0,1), (1,0), (1,2), (2,1), (2,2)\).

### **Initialization**
- `setRepresentatives` is used to store the representative (leader) for both rows and columns. 
- Rows are indexed from 1 to 10001, and columns are indexed from 10002 to 20002.
- `connectedComponentCount` keeps track of the number of connected components.

### **Step-by-Step Dry Run**

**Step 1: Process the First Stone \([0, 0]\)**
- \(x = 0\), \(y = 0\).
- Row index for \(0\) is `1`.
- Column index for \(0\) is `10002`.
- Call `findRepresentative(1)` and `findRepresentative(10002)`.
  - Since both are new elements, they become their own representatives:
    - `findRepresentative(1) = 1`
    - `findRepresentative(10002) = 10002`
- Since they belong to different components, call `mergeComponents(1, 10002)`:
  - The smaller index `1` becomes the representative.
  - `setRepresentatives[10002] = 1`
  - `connectedComponentCount` is incremented by 1 for both row and column, but then decremented by 1 after the union, so it remains `1`.

**Step 2: Process the Second Stone \([0, 1]\)**
- \(x = 0\), \(y = 1\).
- Row index for \(0\) is `1`.
- Column index for \(1\) is `10003`.
- Call `findRepresentative(1)` and `findRepresentative(10003)`.
  - `findRepresentative(1) = 1` (already merged from the previous step).
  - Since column `1` is new, `findRepresentative(10003) = 10003`.
- Since they belong to different components, call `mergeComponents(1, 10003)`:
  - `1` remains the representative.
  - `setRepresentatives[10003] = 1`
  - `connectedComponentCount` remains `1` after the union.

**Step 3: Process the Third Stone \([1, 0]\)**
- \(x = 1\), \(y = 0\).
- Row index for \(1\) is `2`.
- Column index for \(0\) is `10002`.
- Call `findRepresentative(2)` and `findRepresentative(10002)`.
  - Since row `1` is new, `findRepresentative(2) = 2`.
  - `findRepresentative(10002) = 1` (already merged with \([0, 0]\)).
- Since they belong to different components, call `mergeComponents(2, 1)`:
  - `1` remains the representative.
  - `setRepresentatives[2] = 1`
  - `connectedComponentCount` remains `1` after the union.

**Step 4: Process the Fourth Stone \([1, 2]\)**
- \(x = 1\), \(y = 2\).
- Row index for \(1\) is `2`.
- Column index for \(2\) is `10004`.
- Call `findRepresentative(2)` and `findRepresentative(10004)`.
  - `findRepresentative(2) = 1` (already merged with \([1, 0]\)).
  - Since column `2` is new, `findRepresentative(10004) = 10004`.
- Since they belong to different components, call `mergeComponents(1, 10004)`:
  - `1` remains the representative.
  - `setRepresentatives[10004] = 1`
  - `connectedComponentCount` remains `1` after the union.

**Step 5: Process the Fifth Stone \([2, 1]\)**
- \(x = 2\), \(y = 1\).
- Row index for \(2\) is `3`.
- Column index for \(1\) is `10003`.
- Call `findRepresentative(3)` and `findRepresentative(10003)`.
  - Since row `2` is new, `findRepresentative(3) = 3`.
  - `findRepresentative(10003) = 1` (already merged with \([0, 1]\)).
- Since they belong to different components, call `mergeComponents(3, 1)`:
  - `1` remains the representative.
  - `setRepresentatives[3] = 1`
  - `connectedComponentCount` remains `1` after the union.

**Step 6: Process the Sixth Stone \([2, 2]\)**
- \(x = 2\), \(y = 2\).
- Row index for \(2\) is `3`.
- Column index for \(2\) is `10004`.
- Call `findRepresentative(3)` and `findRepresentative(10004)`.
  - `findRepresentative(3) = 1` (already merged with \([2, 1]\)).
  - `findRepresentative(10004) = 1` (already merged with \([1, 2]\)).
- Both already belong to the same component, so no union is needed.

### **Connected Components**

After processing all stones, the entire grid is connected as a single component, with `1` as the root representative.

### **Calculating Removable Stones**

The algorithm calculates the number of removable stones as `|S| - C`, where:
- `|S| = 6` (total number of stones).
- `C = 1` (only one connected component).

Thus, the number of removable stones is `6 - 1 = 5`.


---
### **Mathematical Proof**

#### **1. Problem Recap**

Given $n$ stones on a 2D plane at integer coordinates, the goal is to determine the maximum number of stones that can be removed. A stone can be removed if it shares a row or column with at least one other stone.

#### **2. Key Insight**

The maximum number of stones that can be removed equals the total number of stones minus the number of connected components on the grid.

#### **3. Graph Representation**

The stones and their relationships can be modeled as a graph:
- **Nodes**: Each stone is a node.
- **Edges**: An edge exists between two nodes if the corresponding stones share the same row or column.

**Connected Component**: A connected component is a group of stones such that every stone in the group is connected, directly or indirectly, through shared rows or columns.

#### **4. Lemma: Maximum Stones Removable from a Connected Component**

**Lemma**: In a connected component of $k$ stones, the maximum number of removable stones is $k - 1$.

**Inductive Proof**:

1. **Base Case (k ≤ 2)**:
   - For $k = 1$: No stones can be removed, so $k - 1 = 0$.
   - For $k = 2$: One stone can be removed, so $k - 1 = 1$.

2. **Induction Hypothesis**:
   - Assume the statement holds for all connected components with $k$ stones.

3. **Inductive Step**:
   - Consider a connected component $C$ of size $k + 1$.
   - Label each stone in $C$ with the number of other stones in $C$ it shares a coordinate with.
   - Remove the stone with the smallest label and decrement the labels of stones that share a coordinate with this removed stone.
   - The remaining component(s) have a combined size of $k$. No stone could be isolated in this process since if it were, the component would have been of size $≤ 2$ originally.
   - By the induction hypothesis, we can remove $k - 1$ stones from the remaining component(s), allowing a total of $k$ stones to be removed from $C$.

Thus, the maximum number of stones that can be removed from a connected component of size $k + 1$ is $k$.

#### **5. Theorem: Maximum Removable Stones**

The maximum number of removable stones $R$ is given by $R = |S| - C$, where:
- $|S|$ is the total number of stones.
- $C$ is the number of connected components.

**Proof**:
1. **Sum of Stones in All Components**:
   - Let $k_1, k_2, ..., k_C$ be the number of stones in each of the $C$ connected components.
   - The total number of stones is $|S| = k_1 + k_2 + ... + k_C$.
   
2. **Removable Stones in Each Component**:
   - From the lemma, in each component $i$, we can remove $k_i - 1$ stones.
   - Therefore, the total number of removable stones is $R = ∑(k_i - 1)$ for $i$ from 1 to $C$.

3. **Simplifying the Formula**:
   - Expand the sum: $R = (k_1 - 1) + (k_2 - 1) + ... + (k_C - 1)$.
   - This simplifies to $R = (k_1 + k_2 + ... + k_C) - C$.
   - Since $|S| = k_1 + k_2 + ... + k_C$, we have $R = |S| - C$.

This shows that the maximum number of stones that can be removed is the total number of stones minus the number of connected components.

#### **6. Induction Proof for Algorithm Correctness**

To ensure the algorithm correctly computes the number of stones that can be removed, we'll use induction:

**Base Case**: 
- If there is 1 stone, $|S| = 1$ and $C = 1$. The formula gives $R = 1 - 1 = 0$, which is correct since the stone cannot be removed.

**Induction Hypothesis**:
- Assume the formula $R = |S| - C$ holds for any configuration of $n$ stones.

**Induction Step**:
- Consider the scenario with $n + 1$ stones. 
- The new stone either:
  1. **Forms a New Component**: 
     - In this case, before the addition, we had $n$ stones with $C$ components.
     - The new stone forms a new component, so the number of components increases to $C + 1$.
     - The removable stones count is now $R = n - C + 1 - (C + 1) = n - C = R(n)$, meaning the stone cannot be removed, and the formula still holds.

  2. **Connects to an Existing Component**: 
     - Here, the new stone merges with an existing component, reducing the total number of components by one, i.e., $C - 1$.
     - The formula now is $R(n + 1) = (n + 1) - (C - 1) = R(n) + 1$, which aligns with the ability to remove one more stone.

Thus, the algorithm correctness is upheld by induction, validating that the formula $R = |S| - C$ holds for any number of stones.

#### **7. Alternative Proof and Algorithm**

Another way to prove this statement and derive a corresponding algorithm is using **spanning trees**:

1. **Construct a Spanning Tree**:
   - For each connected component, construct a spanning tree where each stone is a node, and edges are formed by shared rows or columns.
   
2. **Postorder Traversal**:
   - Perform a postorder traversal of the spanning tree.
   - In postorder traversal, you process the leaf nodes first. Removing stones in this order ensures that every time you remove a stone, it leaves the remaining stones still connected, except for the last one, which cannot be removed.

This alternative approach also reinforces the claim that in each connected component of size $k$, exactly $k - 1$ stones can be removed.

#### **8. Complexity Analysis**

- **Time Complexity**: The Union-Find algorithm operates in $O(n * α(n))$, where $α(n)$ is the inverse Ackermann function, effectively constant for practical purposes.
- **Space Complexity**: $O(m)$, where $m$ is the range of coordinates, to store the Union-Find structure.

#### **9. Conclusion**

This proof, combining inductive reasoning with an alternative spanning tree approach, validates the claim that the maximum number of removable stones is given by $R = |S| - C$. The Union-Find algorithm provides a computationally efficient solution, ensuring correctness and optimality for large inputs.
