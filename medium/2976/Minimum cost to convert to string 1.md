## Problem in Simpler Terms

Imagine you have a word game where you need to change one word (let's call it the "source" word) into another word (the "target" word). Here are the rules:

1. Both words have the same length.
2. You can only change one letter at a time.
3. Each letter change has a specific cost.
4. You're given a list of allowed letter changes and their costs.
5. You can use these changes as many times as you want.

Your goal is to find the cheapest way to change the source word into the target word.

Here's a breakdown of the key elements:

1. `source` and `target`: These are the starting and ending words.
2. `original` and `changed`: These lists show what letter changes are allowed.
3. `cost`: This list shows how much each allowed change costs.

For example:
- If you're allowed to change 'a' to 'b' for a cost of 5
- And 'b' to 'c' for a cost of 3
- Then you could change 'a' to 'c' for a total cost of 8 (5 + 3)

The tricky part is that sometimes it's cheaper to make multiple small changes rather than one big change. Your job is to figure out the cheapest overall path to change the source word into the target word.

If it's impossible to change the source word into the target word using the allowed changes, you should return -1.

---



# Intuition

When first approaching this problem, we need to understand that we're essentially dealing with a graph problem. Each character in the alphabet can be thought of as a node in a graph, and the allowed character conversions represent the edges between these nodes. The cost of each conversion is the weight of the edge.

The core challenge is to find the cheapest way to transform the source string into the target string. This immediately brings to mind the concept of finding the shortest path in a weighted graph. However, we're not just finding a single path - we need to find the shortest path between every pair of characters, as we might need to transform any character into any other character.

This realization leads us to consider algorithms for finding all-pairs shortest paths in a graph. The Floyd-Warshall algorithm is a perfect fit for this scenario, as it efficiently computes the shortest paths between all pairs of nodes in a weighted graph.

# Approach

## 1. Building the Conversion Graph

The first step is to represent our problem as a graph. We'll use a 2D array (matrix) to represent this graph, where each cell [i][j] represents the cost of converting character i to character j.

Pseudo-code for this step:

```
function buildConversionGraph(original, changed, cost):
    // Initialize graph with all edges set to infinity
    graph = 2D array of size [CHAR_COUNT][CHAR_COUNT] filled with INF

    // Set cost of converting a character to itself to 0
    for i from 0 to CHAR_COUNT - 1:
        graph[i][i] = 0

    // Fill in the known conversion costs
    for i from 0 to length of cost - 1:
        from = index of original[i] in alphabet
        to = index of changed[i] in alphabet
        graph[from][to] = minimum of (graph[from][to], cost[i])

    return graph
```

This function creates our initial graph representation. Here's a detailed breakdown of what's happening:

1. We start by creating a 2D array filled with a very large value (INF). This represents that initially, we assume there's no direct way to convert any character to any other character.

2. We then set the cost of converting a character to itself to 0. This is logical - it costs nothing to keep a character as is.

3. Finally, we iterate through the given conversion rules (original, changed, and cost arrays). For each rule, we update our graph. The `from` character is represented by the row index, and the `to` character by the column index. We use the minimum of the current value and the new cost in case there are multiple ways to perform the same conversion.
4. Now, why do we use `minimum of (graph[from][to], cost[i])` here? well, we might have multiple ways to change one letter to another. like, we might be told we can change 'a' to 'b' for 5 points, but later we're told we can do it for 3 points. we want to keep the cheaper option, so we use `minimum of (graph[from][to], cost[i])`.
5. After all this, we end up with a grid that shows the cheapest way to directly change any letter to any other letter, based on the rules we were given.

This step gives us a graph that represents all direct conversions we can make based on the given rules.

**PS:** I've seen a lot of people getting confused with this, so let me explain:

the reason we use graph[from][to] = Math.min(graph[from][to], cost[i]); instead of just graph[from][to] = cost[i]; is because there might be multiple ways to convert one character to another, with different costs. by using Math.min(), we're always keeping the lowest cost option for converting from one character to another.

here's an example: let's say in our input we have:
original = ['a', 'a']
changed = ['b', 'b']
cost = [5, 3]

this means we have two ways to convert 'a' to 'b': one costs 5 and another costs 3. if we just used graph[from][to] = cost[i];, the cost of converting a to b would be set to 5 first and then overwritten with 3. but we want to keep the lower cost of 3.

so by using math.min(graph[from][to], cost[i]) we make sure we always keep the lowest cost for each character conversion, even if there are multiple conversion options in the input.


## 2. Optimizing Conversion Paths

Now that we have our initial graph, we need to find the cheapest way to convert any character to any other character, even if it requires multiple steps. This is where the Floyd-Warshall algorithm comes in.

Pseudo-code for this step:

```
function optimizeConversionPaths(graph):
    for k from 0 to CHAR_COUNT - 1:
        for i from 0 to CHAR_COUNT - 1:
            if graph[i][k] < INF:
                for j from 0 to CHAR_COUNT - 1:
                    if graph[k][j] < INF:
                        graph[i][j] = minimum of (graph[i][j], graph[i][k] + graph[k][j])
```

This is the heart of the Floyd-Warshall algorithm. Here's what's happening:

1. We iterate through all possible intermediate nodes (k).

2. For each pair of nodes (i and j), we check if going through k gives us a cheaper path than the one we currently know.

3. If we find a cheaper path, we update our graph.

The brilliance of this algorithm is that it considers all possible paths between all pairs of nodes. After this step, graph[i][j] will contain the cost of the cheapest possible way to convert character i to character j, even if it requires multiple intermediate steps.

A key optimization in our implementation is the check `if graph[i][k] < INF` and `if graph[k][j] < INF`. This prevents unnecessary calculations when there's no path between nodes, significantly speeding up the algorithm for sparse graphs.

## 3. Computing the Total Conversion Cost

With our fully optimized conversion graph, we can now calculate the cost of converting the source string to the target string.

Pseudo-code for this step:

```
function computeTotalConversionCost(source, target, graph):
    totalCost = 0
    for i from 0 to length of source - 1:
        sourceChar = index of source[i] in alphabet
        targetChar = index of target[i] in alphabet
        if sourceChar != targetChar:
            if graph[sourceChar][targetChar] == INF:
                return -1  // Conversion is impossible
            totalCost += graph[sourceChar][targetChar]
    return totalCost
```

Here's what this function does:

1. We iterate through each position in the source and target strings simultaneously.

2. If the characters at the current position are different, we need to perform a conversion.

3. We look up the cost of this conversion in our optimized graph.

4. If the cost is INF, it means there's no way to perform this conversion, so we return -1 to indicate that the overall conversion is impossible.

5. Otherwise, we add the cost to our total.

6. After checking all positions, if we haven't returned -1, we return the total cost.

This approach ensures that we're always using the cheapest possible way to convert each character, even if it involves multiple steps.



# Complexity Analysis

## Time Complexity

The time complexity of this solution is dominated by the Floyd-Warshall algorithm used in the `optimizeConversionPaths` function.

- Building the initial graph takes O(CHAR_COUNT^2 + N) time, where N is the number of given conversion rules. This is because we initialize a CHAR_COUNT x CHAR_COUNT matrix and then process N rules.

- The Floyd-Warshall algorithm in `optimizeConversionPaths` has a time complexity of O(CHAR_COUNT^3). This comes from the three nested loops, each iterating CHAR_COUNT times.

- Computing the total cost takes O(L) time, where L is the length of the source/target strings.

Since CHAR_COUNT is a constant (26 for lowercase English letters), the O(CHAR_COUNT^3) term is actually O(1) in the context of this problem. Therefore, the overall time complexity is **O(N + L)**.

**IMPORTANT:** 
It's worth noting that the constant factor here (26^3 = 17,576) is quite large. For very small inputs, this could be slower than a more straightforward approach. But for larger inputs, especially when N or L is large, this approach becomes very efficient.
In practice, this means:
1. For small N and L, the constant time from the Floyd-Warshall part might dominate.
2. For larger N or L, the O(N + L) part will dominate, making the algorithm very efficient.

## Space Complexity

The space complexity is determined by the size of our graph:

- We use a 2D array of size CHAR_COUNT x CHAR_COUNT to represent our graph.
- Again, since CHAR_COUNT is a constant (26), this is actually O(1) space.

We don't use any other data structures that grow with the input size, so the overall space complexity remains **O(1)**.

This constant space usage is a significant advantage of this approach, especially for large inputs. No matter how long the strings are or how many conversion rules are given, we always use the same amount of memory.





---

# Code
Java
```Java []
class Solution {
    private static final int CHAR_COUNT = 26;
    private static final int INF = Integer.MAX_VALUE / 2;

    public long minimumCost(String source, String target, char[] original, char[] changed, int[] cost) {
        int[][] conversionGraph = buildConversionGraph(original, changed, cost);
        optimizeConversionPaths(conversionGraph);
        return computeTotalConversionCost(source, target, conversionGraph);
    }

    private int[][] buildConversionGraph(char[] original, char[] changed, int[] cost) {
        int[][] graph = new int[CHAR_COUNT][CHAR_COUNT];
        for (int[] row : graph) {
            Arrays.fill(row, INF);
        }
        for (int i = 0; i < CHAR_COUNT; i++) {
            graph[i][i] = 0;
        }
        for (int i = 0; i < cost.length; i++) {
            int from = original[i] - 'a';
            int to = changed[i] - 'a';
            graph[from][to] = Math.min(graph[from][to], cost[i]);
        }
        return graph;
    }

    private void optimizeConversionPaths(int[][] graph) {
        for (int k = 0; k < CHAR_COUNT; k++) {
            for (int i = 0; i < CHAR_COUNT; i++) {
                if (graph[i][k] < INF) {
                    for (int j = 0; j < CHAR_COUNT; j++) {
                        if (graph[k][j] < INF) {
                            graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                        }
                    }
                }
            }
        }
    }

    private long computeTotalConversionCost(String source, String target, int[][] graph) {
        long totalCost = 0;
        for (int i = 0; i < source.length(); i++) {
            int sourceChar = source.charAt(i) - 'a';
            int targetChar = target.charAt(i) - 'a';
            if (sourceChar != targetChar) {
                if (graph[sourceChar][targetChar] == INF) {
                    return -1L;
                }
                totalCost += graph[sourceChar][targetChar];
            }
        }
        return totalCost;
    }
}
```
C++
```C++ []
#include <vector>
#include <string>
#include <algorithm>

class Solution {
private:
    static constexpr int CHAR_COUNT = 26;
    static constexpr int INF = 1e9;

    std::vector<std::vector<int>> buildConversionGraph(const std::vector<char>& original, const std::vector<char>& changed, const std::vector<int>& cost) {
        std::vector<std::vector<int>> graph(CHAR_COUNT, std::vector<int>(CHAR_COUNT, INF));
        for (int i = 0; i < CHAR_COUNT; i++) {
            graph[i][i] = 0;
        }
        for (size_t i = 0; i < cost.size(); i++) {
            int from = original[i] - 'a';
            int to = changed[i] - 'a';
            graph[from][to] = std::min(graph[from][to], cost[i]);
        }
        return graph;
    }

    void optimizeConversionPaths(std::vector<std::vector<int>>& graph) {
        for (int k = 0; k < CHAR_COUNT; k++) {
            for (int i = 0; i < CHAR_COUNT; i++) {
                if (graph[i][k] < INF) {
                    for (int j = 0; j < CHAR_COUNT; j++) {
                        if (graph[k][j] < INF) {
                            graph[i][j] = std::min(graph[i][j], graph[i][k] + graph[k][j]);
                        }
                    }
                }
            }
        }
    }

    long long computeTotalConversionCost(const std::string& source, const std::string& target, const std::vector<std::vector<int>>& graph) {
        long long totalCost = 0;
        for (size_t i = 0; i < source.length(); i++) {
            int sourceChar = source[i] - 'a';
            int targetChar = target[i] - 'a';
            if (sourceChar != targetChar) {
                if (graph[sourceChar][targetChar] == INF) {
                    return -1;
                }
                totalCost += graph[sourceChar][targetChar];
            }
        }
        return totalCost;
    }

public:
    long long minimumCost(std::string source, std::string target, std::vector<char>& original, std::vector<char>& changed, std::vector<int>& cost) {
        auto conversionGraph = buildConversionGraph(original, changed, cost);
        optimizeConversionPaths(conversionGraph);
        return computeTotalConversionCost(source, target, conversionGraph);
    }
};

```
Python
```Python []

class Solution:
    CHAR_COUNT = 26
    INF = float('inf')

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        conversionGraph = self.buildConversionGraph(original, changed, cost)
        self.optimizeConversionPaths(conversionGraph)
        return self.computeTotalConversionCost(source, target, conversionGraph)

    def buildConversionGraph(self, original: List[str], changed: List[str], cost: List[int]) -> List[List[int]]:
        graph = [[self.INF] * self.CHAR_COUNT for _ in range(self.CHAR_COUNT)]
        for i in range(self.CHAR_COUNT):
            graph[i][i] = 0
        for i in range(len(cost)):
            fromChar = ord(original[i]) - ord('a')
            toChar = ord(changed[i]) - ord('a')
            graph[fromChar][toChar] = min(graph[fromChar][toChar], cost[i])
        return graph

    def optimizeConversionPaths(self, graph: List[List[int]]) -> None:
        for k in range(self.CHAR_COUNT):
            for i in range(self.CHAR_COUNT):
                if graph[i][k] < self.INF:
                    for j in range(self.CHAR_COUNT):
                        if graph[k][j] < self.INF:
                            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    def computeTotalConversionCost(self, source: str, target: str, graph: List[List[int]]) -> int:
        totalCost = 0
        for i in range(len(source)):
            sourceChar = ord(source[i]) - ord('a')
            targetChar = ord(target[i]) - ord('a')
            if sourceChar != targetChar:
                if graph[sourceChar][targetChar] == self.INF:
                    return -1
                totalCost += graph[sourceChar][targetChar]
        return totalCost
```
JavaScript
```JavaScript []
/**
 * @param {string} source
 * @param {string} target
 * @param {character[]} original
 * @param {character[]} changed
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(source, target, original, changed, cost) {
    const CHAR_COUNT = 26;
    const INF = Number.MAX_SAFE_INTEGER / 2;

    const buildConversionGraph = (original, changed, cost) => {
        const graph = Array(CHAR_COUNT).fill().map(() => Array(CHAR_COUNT).fill(INF));
        for (let i = 0; i < CHAR_COUNT; i++) {
            graph[i][i] = 0;
        }
        for (let i = 0; i < cost.length; i++) {
            const from = original[i].charCodeAt(0) - 'a'.charCodeAt(0);
            const to = changed[i].charCodeAt(0) - 'a'.charCodeAt(0);
            graph[from][to] = Math.min(graph[from][to], cost[i]);
        }
        return graph;
    };

    const optimizeConversionPaths = (graph) => {
        for (let k = 0; k < CHAR_COUNT; k++) {
            for (let i = 0; i < CHAR_COUNT; i++) {
                if (graph[i][k] < INF) {
                    for (let j = 0; j < CHAR_COUNT; j++) {
                        if (graph[k][j] < INF) {
                            graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                        }
                    }
                }
            }
        }
    };

    const computeTotalConversionCost = (source, target, graph) => {
        let totalCost = 0;
        for (let i = 0; i < source.length; i++) {
            const sourceChar = source.charCodeAt(i) - 'a'.charCodeAt(0);
            const targetChar = target.charCodeAt(i) - 'a'.charCodeAt(0);
            if (sourceChar !== targetChar) {
                if (graph[sourceChar][targetChar] === INF) {
                    return -1;
                }
                totalCost += graph[sourceChar][targetChar];
            }
        }
        return totalCost;
    };

    const conversionGraph = buildConversionGraph(original, changed, cost);
    optimizeConversionPaths(conversionGraph);
    return computeTotalConversionCost(source, target, conversionGraph);
};

```
Go
```Go []
package main

import (
    "math"
)

const CHAR_COUNT = 26
const INF = math.MaxInt32 / 2

func minimumCost(source string, target string, original []byte, changed []byte, cost []int) int64 {
    conversionGraph := buildConversionGraph(original, changed, cost)
    optimizeConversionPaths(conversionGraph)
    return computeTotalConversionCost(source, target, conversionGraph)
}

func buildConversionGraph(original []byte, changed []byte, cost []int) [][]int {
    graph := make([][]int, CHAR_COUNT)
    for i := range graph {
        graph[i] = make([]int, CHAR_COUNT)
        for j := range graph[i] {
            graph[i][j] = INF
        }
        graph[i][i] = 0
    }
    for i, c := range cost {
        from := int(original[i] - 'a')
        to := int(changed[i] - 'a')
        if c < graph[from][to] {
            graph[from][to] = c
        }
    }
    return graph
}

func optimizeConversionPaths(graph [][]int) {
    for k := 0; k < CHAR_COUNT; k++ {
        for i := 0; i < CHAR_COUNT; i++ {
            if graph[i][k] < INF {
                for j := 0; j < CHAR_COUNT; j++ {
                    if graph[k][j] < INF {
                        if graph[i][k]+graph[k][j] < graph[i][j] {
                            graph[i][j] = graph[i][k] + graph[k][j]
                        }
                    }
                }
            }
        }
    }
}

func computeTotalConversionCost(source string, target string, graph [][]int) int64 {
    var totalCost int64 = 0
    for i := 0; i < len(source); i++ {
        sourceChar := int(source[i] - 'a')
        targetChar := int(target[i] - 'a')
        if sourceChar != targetChar {
            if graph[sourceChar][targetChar] == INF {
                return -1
            }
            totalCost += int64(graph[sourceChar][targetChar])
        }
    }
    return totalCost
}

```
Rust
```Rust []

use std::cmp::min;
use std::i64;

const CHAR_COUNT: usize = 26;
const INF: i64 = i64::MAX / 2;

impl Solution {
    pub fn minimum_cost(
        source: String,
        target: String,
        original: Vec<char>,
        changed: Vec<char>,
        cost: Vec<i32>,
    ) -> i64 {
        let mut conversion_graph = Self::build_conversion_graph(&original, &changed, &cost);
        Self::optimize_conversion_paths(&mut conversion_graph);
        Self::compute_total_conversion_cost(&source, &target, &conversion_graph)
    }

    fn build_conversion_graph(
        original: &[char],
        changed: &[char],
        cost: &[i32],
    ) -> Vec<Vec<i64>> {
        let mut graph = vec![vec![INF; CHAR_COUNT]; CHAR_COUNT];
        for i in 0..CHAR_COUNT {
            graph[i][i] = 0;
        }
        for (i, &o) in original.iter().enumerate() {
            let from = (o as usize) - ('a' as usize);
            let to = (changed[i] as usize) - ('a' as usize);
            graph[from][to] = min(graph[from][to], cost[i] as i64);
        }
        graph
    }

    fn optimize_conversion_paths(graph: &mut Vec<Vec<i64>>) {
        for k in 0..CHAR_COUNT {
            for i in 0..CHAR_COUNT {
                if graph[i][k] < INF {
                    for j in 0..CHAR_COUNT {
                        if graph[k][j] < INF {
                            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
                        }
                    }
                }
            }
        }
    }

    fn compute_total_conversion_cost(
        source: &str,
        target: &str,
        graph: &[Vec<i64>],
    ) -> i64 {
        if source.len() != target.len() {
            return -1;
        }
        let mut total_cost = 0;
        for (s, t) in source.chars().zip(target.chars()) {
            let source_char = (s as usize) - ('a' as usize);
            let target_char = (t as usize) - ('a' as usize);
            if source_char != target_char {
                if graph[source_char][target_char] == INF {
                    return -1;
                }
                total_cost += graph[source_char][target_char];
            }
        }
        total_cost
    }
}


```
---

## DRY RUN


**Example:**
- source = "abc"
- target = "ade"
- original = ['a', 'b', 'c', 'd']
- changed = ['b', 'c', 'd', 'e']
- cost = [1, 2, 3, 4]

Let's go through the solution step by step:

**1. Building the Conversion Graph:**



```java
int[][] buildConversionGraph(char[] original, char[] changed, int[] cost) {
    int[][] graph = new int[CHAR_COUNT][CHAR_COUNT];
    for (int[] row : graph) {
        Arrays.fill(row, INF);
    }
    for (int i = 0; i < CHAR_COUNT; i++) {
        graph[i][i] = 0;
    }
    for (int i = 0; i < cost.length; i++) {
        int from = original[i] - 'a';
        int to = changed[i] - 'a';
        graph[from][to] = Math.min(graph[from][to], cost[i]);
    }
    return graph;
}

```

Let's walk through this step:

a. Initialize a 26x26 matrix with INF (infinity) values.
b. Set the diagonal (converting a character to itself) to 0.
c. Fill in the known conversion costs:
   - 'a' to 'b': cost 1
   - 'b' to 'c': cost 2
   - 'c' to 'd': cost 3
   - 'd' to 'e': cost 4

The resulting graph would look like this (showing only the relevant part):

```
    a   b   c   d   e
a   0   1   INF INF INF
b   INF 0   2   INF INF
c   INF INF 0   3   INF
d   INF INF INF 0   4
e   INF INF INF INF 0
```

**2. Optimizing Conversion Paths:**



```java
void optimizeConversionPaths(int[][] graph) {
    for (int k = 0; k < CHAR_COUNT; k++) {
        for (int i = 0; i < CHAR_COUNT; i++) {
            if (graph[i][k] < INF) {
                for (int j = 0; j < CHAR_COUNT; j++) {
                    if (graph[k][j] < INF) {
                        graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                    }
                }
            }
        }
    }
}

```

This step applies the Floyd-Warshall algorithm to find the shortest path between all pairs of characters. Let's see how it affects our graph:

a. For k = 0 (a), no changes as 'a' doesn't provide any new shortest paths.
b. For k = 1 (b), we can now go from 'a' to 'c' through 'b':
   - 'a' to 'c': min(INF, 1 + 2) = 3
c. For k = 2 (c), we can go from 'a' to 'd' and 'b' to 'd':
   - 'a' to 'd': min(INF, 3 + 3) = 6
   - 'b' to 'd': min(INF, 2 + 3) = 5
d. For k = 3 (d), we can reach 'e' from 'a', 'b', and 'c':
   - 'a' to 'e': min(INF, 6 + 4) = 10
   - 'b' to 'e': min(INF, 5 + 4) = 9
   - 'c' to 'e': min(INF, 3 + 4) = 7

After optimization, our graph looks like this:

```
    a   b   c   d   e
a   0   1   3   6   10
b   INF 0   2   5   9
c   INF INF 0   3   7
d   INF INF INF 0   4
e   INF INF INF INF 0
```

**3. Computing the Total Conversion Cost:**



Now we compare the source and target strings character by character:

a. 'a' to 'a': No change needed, cost 0
b. 'b' to 'd': Cost is 5 (from our optimized graph)
c. 'c' to 'e': Cost is 7 (from our optimized graph)

Total cost: 0 + 5 + 7 = 12

Therefore, the minimum cost to convert "abc" to "ade" is 12.
