

### Intuition
Let's start by breaking down the problem statement and constraints:

1. We have stones on a 2D plane at integer coordinates.
2. A stone can be removed if it shares a row or column with another stone.
3. We need to find the maximum number of stones that can be removed.
4. We're dealing with up to 1000 stones, with coordinates ranging from 0 to 10,000.

My initial thought was to imagine the stones on a grid. Try to imagine some lines connecting stones in the same row or column, forming a kind of network. Well This mental image immediately reminded me of some graph problems I've solved before.

So at first I considered a brute-force approach to try remove the stones one by one, always picking a stone that shares a row or column with another. But I quickly realized this would be inefficient and wouldn't guarantee the optimal solution.

Then I thought about using depth-first search (DFS). The idea was to treat each stone as a node in a graph, with edges between stones that share a row or column. I could use DFS to explore all connected stones, removing them as I go. This was good, but still like how would I efficiently find all stones in the same row or column?

I even tried an idea of using hash maps to group stones by row and column, but it felt like overkill. But think it like this what if, instead of focusing on the stones themselves, I considered the rows and columns as the primary elements?
Therefore, I realized that all stones in the same row or column form a single connected component. Instead of explicitly connecting stones, I could implicitly connect them through their shared rows and columns.

This helped me to think about disjoint set union (DSU) data structures, also known as union-find. I've used DSU before to efficiently handle merging of sets, and it seemed perfect for this problem. Each row and column could start as its own set, and as we process the stones, we'd merge these sets. But again how to represent rows and columns in a way that doesn't confuse them? I couldn't use the same numbering system for both. That's when I came up with the idea of offsetting the column values by a large number, effectively creating two separate ranges for rows and columns.

When I was working on this concept, I realized I needed to keep track of the number of unique components. Each new row or column encountered would initially be its own component, but as we process the stones, these components would merge. The final number of components would be crucial in determining how many stones we could remove.

I also thought about the edge cases. What if all stones are in the same row? Or if no stones share any rows or columns? My approach needed to handle these scenarios correctly.

Throughout this thought process, I kept circling back to the core insight: the maximum number of stones we can remove is equal to the total number of stones minus the number of connected components. This is because in each connected component, we can remove all stones except one.
The good thing about this approach is that it scales well – processing each stone once and performing efficient union-find operations means we can handle even the maximum input size of 1000 stones quickly.




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
### **Mathematical Proof**

#### **1. Problem Recap**

Given `n` stones on a 2D plane at integer coordinates, we need to determine the maximum number of stones that can be removed. A stone can be removed if it shares a row or column with at least one other stone.

#### **2. Key Insight**

The core insight is that the maximum number of stones that can be removed equals the total number of stones minus the number of connected components on the grid. 

#### **3. Graph Representation**

Consider the stones and their relationships as a graph:
- **Nodes**: Each stone is a node.
- **Edges**: There is an edge between two nodes if the corresponding stones share the same row or the same column.

**Connected Component**: A connected component is a group of stones such that every stone in the group is connected directly or indirectly (via other stones) through shared rows or columns.

#### **4. Lemma: Maximum Stones Removable from a Connected Component**

**Lemma**: In a connected component of `k` stones, the maximum number of removable stones is `k - 1`.

**Proof**:
1. **Base Case**: If `k = 1` (a single stone), no stones can be removed.
2. **Induction Step**: For `k > 1`:
   - Start by picking any stone in the component. Since it's connected to at least one other stone, we can remove it.
   - Move to the next stone and repeat the process.
   - Continue until only one stone remains, which cannot be removed.
   - Thus, in a component of `k` stones, we can remove `k - 1` stones.

#### **5. Theorem: Maximum Removable Stones**

The maximum number of removable stones $R$ is given by $R = |S| - C$, where:
- $|S|$ is the total number of stones.
- $C$ is the number of connected components.

**Proof**:
1. **Sum of Stones in All Components**:
   - Let $k_1, k_2, \ldots, k_C$ be the number of stones in each of the $C$ connected components.
   - The total number of stones is $|S| = k_1 + k_2 + \cdots + k_C$.
   
2. **Removable Stones in Each Component**:
   - From the Lemma, in each component $i$, we can remove $k_i - 1$ stones.
   - Therefore, the total number of removable stones is $R = \sum_{i=1}^{C} (k_i - 1)$.

3. **Simplifying the Formula**:
   - Expand the sum: $R = (k_1 - 1) + (k_2 - 1) + \cdots + (k_C - 1)$.
   - This simplifies to $R = (k_1 + k_2 + \cdots + k_C) - C$.
   - Since $|S| = k_1 + k_2 + \cdots + k_C$, we have $R = |S| - C$.

This shows that the maximum number of stones that can be removed is the total number of stones minus the number of connected components.

#### **6. Algorithm Implementation: Union-Find**

The Union-Find (or Disjoint Set Union, DSU) algorithm efficiently tracks and merges connected components:

1. **Initialization**: Start with each stone as its own component.
2. **Union Operation**: For each stone, connect its row and column to merge components that share rows or columns.
3. **Find Operation**: Identify the representative (root) of the component to which a stone belongs.
4. **Final Count**: After processing all stones, the number of distinct components $C$ is determined. The maximum number of removable stones is $|S| - C$.

#### **7. Induction Proof for Algorithm Correctness**

**Base Case**: 
- If there is 1 stone, $|S| = 1$ and $C = 1$. The formula gives $R = 1 - 1 = 0$, which is correct since the stone cannot be removed.

**Induction Step**:
- Assume the formula $R = |S| - C$ holds for $n$ stones.
- Consider adding the $(n+1)$-th stone.

**Case 1**: The new stone forms a new connected component.
- Before: $R(n) = n - C$.
- After: $R(n+1) = (n + 1) - (C + 1) = n - C = R(n)$.
- The stone is isolated and cannot be removed, so the formula holds.

**Case 2**: The new stone connects to an existing component.
- Before: $R(n) = n - C$.
- After: $R(n+1) = (n + 1) - C = R(n) + 1$.
- The new stone can be removed, increasing the count, so the formula holds.

By induction, the formula $R = |S| - C$ is valid for all $n$.

#### **8. Complexity Analysis**

- **Time Complexity**: $O(n \cdot \alpha(n))$, where $\alpha(n)$ is the inverse Ackermann function, effectively constant for practical purposes.
- **Space Complexity**: $O(m)$, where $m$ is the range of coordinates, to store the Union-Find structure.

#### **9. Conclusion**

The proof combines graph theory (connected components) with the Union-Find algorithm to show that the maximum number of removable stones is given by $R = |S| - C$. This approach is both mathematically rigorous and computationally efficient, ensuring the solution is correct and optimal for large inputs.
