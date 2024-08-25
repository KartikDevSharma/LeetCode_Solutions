# Complexity
- Time complexity: $O((V+E)logV)$ where 𝐸 is the number of edges and 𝑉 is the number of nodes.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(V+E)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```java []
//18-ms
class Solution {
    public int reachableNodes(int[][] edges, int maxMoves, int nodeCount) {
       
        List<int[]>[] adjacencyList = new List[nodeCount];
        for (int i = 0; i < nodeCount; i++) {
            adjacencyList[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            int start = edge[0], end = edge[1], subdivisions = edge[2];
            adjacencyList[start].add(new int[]{end, subdivisions});
            adjacencyList[end].add(new int[]{start, subdivisions});
        }
        int[] shortestDistances = new int[nodeCount];
        Arrays.fill(shortestDistances, Integer.MAX_VALUE);
        shortestDistances[0] = 0;

        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        minHeap.offer(new int[]{0, 0});

        int reachableNodeCount = 0;
        while (!minHeap.isEmpty()) {
            int[] current = minHeap.poll();
            int currentNode = current[0], distanceToCurrentNode = current[1];

            if (distanceToCurrentNode > shortestDistances[currentNode]) continue;
            if (distanceToCurrentNode <= maxMoves) reachableNodeCount++;

            for (int[] neighborInfo : adjacencyList[currentNode]) {
                int neighborNode = neighborInfo[0], edgeWeight = neighborInfo[1];
                int distanceToNeighbor = distanceToCurrentNode + edgeWeight + 1;

                if (distanceToNeighbor < shortestDistances[neighborNode] && distanceToNeighbor <= maxMoves) {
                    shortestDistances[neighborNode] = distanceToNeighbor;
                    minHeap.offer(new int[]{neighborNode, distanceToNeighbor});
                }
            }
        }
        
        for (int[] edge : edges) {
            int start = edge[0], end = edge[1], subdivisions = edge[2];
            int reachableFromStart = Math.max(0, maxMoves - shortestDistances[start]);
            int reachableFromEnd = Math.max(0, maxMoves - shortestDistances[end]);
            reachableNodeCount += Math.min(subdivisions, reachableFromStart + reachableFromEnd);
        }

        return reachableNodeCount;
    }
}

//https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/submissions/1365472681/
```

```C++ []
//70-ms
class Solution {
public:
    int reachableNodes(std::vector<std::vector<int>>& edges, int maxMoves, int nodeCount) {
        std::vector<std::vector<std::pair<int, int>>> adjacencyList(nodeCount);
        for (const auto& edge : edges) {
            int start = edge[0], end = edge[1], subdivisions = edge[2];
            adjacencyList[start].emplace_back(end, subdivisions);
            adjacencyList[end].emplace_back(start, subdivisions);
        }

        std::vector<int> shortestDistances(nodeCount, std::numeric_limits<int>::max());
        shortestDistances[0] = 0;

        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<>> minHeap;
        minHeap.emplace(0, 0);

        int reachableNodeCount = 0;
        while (!minHeap.empty()) {
            auto [distanceToCurrentNode, currentNode] = minHeap.top();
            minHeap.pop();

            if (distanceToCurrentNode > shortestDistances[currentNode]) continue;
            if (distanceToCurrentNode <= maxMoves) reachableNodeCount++;

            for (const auto& [neighborNode, edgeWeight] : adjacencyList[currentNode]) {
                int distanceToNeighbor = distanceToCurrentNode + edgeWeight + 1;

                if (distanceToNeighbor < shortestDistances[neighborNode] && distanceToNeighbor <= maxMoves) {
                    shortestDistances[neighborNode] = distanceToNeighbor;
                    minHeap.emplace(distanceToNeighbor, neighborNode);
                }
            }
        }

        for (const auto& edge : edges) {
            int start = edge[0], end = edge[1], subdivisions = edge[2];
            int reachableFromStart = std::max(0, maxMoves - shortestDistances[start]);
            int reachableFromEnd = std::max(0, maxMoves - shortestDistances[end]);
            reachableNodeCount += std::min(subdivisions, reachableFromStart + reachableFromEnd);
        }

        return reachableNodeCount;
    }
};

static const int speedup = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();

//https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/submissions/1365504500/
```
```Python []
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, nodeCount: int) -> int:
        adjacencyList = [[] for _ in range(nodeCount)]
        for start, end, subdivisions in edges:
            adjacencyList[start].append((end, subdivisions))
            adjacencyList[end].append((start, subdivisions))

        shortestDistances = [float('inf')] * nodeCount
        shortestDistances[0] = 0

        minHeap = [(0, 0)]
        reachableNodeCount = 0

        while minHeap:
            distanceToCurrentNode, currentNode = heapq.heappop(minHeap)

            if distanceToCurrentNode > shortestDistances[currentNode]:
                continue
            if distanceToCurrentNode <= maxMoves:
                reachableNodeCount += 1

            for neighborNode, edgeWeight in adjacencyList[currentNode]:
                distanceToNeighbor = distanceToCurrentNode + edgeWeight + 1

                if distanceToNeighbor < shortestDistances[neighborNode] and distanceToNeighbor <= maxMoves:
                    shortestDistances[neighborNode] = distanceToNeighbor
                    heapq.heappush(minHeap, (distanceToNeighbor, neighborNode))

        for start, end, subdivisions in edges:
            reachableFromStart = max(0, maxMoves - shortestDistances[start])
            reachableFromEnd = max(0, maxMoves - shortestDistances[end])
            reachableNodeCount += min(subdivisions, reachableFromStart + reachableFromEnd)

        return reachableNodeCount

import os

def main():
    input_file = "user.in" 
    output_file = "user.out"  

    if not os.path.exists(input_file):
        print(f"Error: The input file '{input_file}' does not exist.")
        return
    
    with open(input_file, "r") as f:
        inputs = json.load(f)
    
    solution = Solution()
    results = []

    for data in inputs:
        edges = data['edges']
        maxMoves = data['maxMoves']
        nodeCount = data['nodeCount']
        result = solution.reachableNodes(edges, maxMoves, nodeCount)
        results.append(result)
    
    with open(output_file, "w") as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()


#https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/submissions/1365496132/
```

```Go []

type MinHeap [][2]int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i][1] < h[j][1] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{}) { *h = append(*h, x.([2]int)) }
func (h *MinHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

func reachableNodes(edges [][]int, maxMoves int, nodeCount int) int {
    adjacencyList := make([][][2]int, nodeCount)
    for _, edge := range edges {
        start, end, subdivisions := edge[0], edge[1], edge[2]
        adjacencyList[start] = append(adjacencyList[start], [2]int{end, subdivisions})
        adjacencyList[end] = append(adjacencyList[end], [2]int{start, subdivisions})
    }

    shortestDistances := make([]int, nodeCount)
    for i := range shortestDistances {
        shortestDistances[i] = math.MaxInt32
    }
    shortestDistances[0] = 0

    minHeap := &MinHeap{{0, 0}}
    heap.Init(minHeap)

    reachableNodeCount := 0
    for minHeap.Len() > 0 {
        current := heap.Pop(minHeap).([2]int)
        currentNode, distanceToCurrentNode := current[0], current[1]

        if distanceToCurrentNode > shortestDistances[currentNode] {
            continue
        }
        if distanceToCurrentNode <= maxMoves {
            reachableNodeCount++
        }

        for _, neighborInfo := range adjacencyList[currentNode] {
            neighborNode, edgeWeight := neighborInfo[0], neighborInfo[1]
            distanceToNeighbor := distanceToCurrentNode + edgeWeight + 1

            if distanceToNeighbor < shortestDistances[neighborNode] && distanceToNeighbor <= maxMoves {
                shortestDistances[neighborNode] = distanceToNeighbor
                heap.Push(minHeap, [2]int{neighborNode, distanceToNeighbor})
            }
        }
    }

    for _, edge := range edges {
        start, end, subdivisions := edge[0], edge[1], edge[2]
        reachableFromStart := max(0, maxMoves-shortestDistances[start])
        reachableFromEnd := max(0, maxMoves-shortestDistances[end])
        reachableNodeCount += min(subdivisions, reachableFromStart+reachableFromEnd)
    }

    return reachableNodeCount
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

//https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/submissions/1365476118/
```
```Rust []
use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn reachable_nodes(edges: Vec<Vec<i32>>, max_moves: i32, node_count: i32) -> i32 {
        let node_count = node_count as usize;
        let mut adjacency_list = vec![Vec::new(); node_count];
        for edge in &edges {
            let start = edge[0] as usize;
            let end = edge[1] as usize;
            let subdivisions = edge[2];
            adjacency_list[start].push((end, subdivisions));
            adjacency_list[end].push((start, subdivisions));
        }

        let mut shortest_distances = vec![i32::MAX; node_count];
        shortest_distances[0] = 0;

        let mut min_heap = BinaryHeap::new();
        min_heap.push(Reverse((0, 0)));

        let mut reachable_node_count = 0;
        while let Some(Reverse((distance_to_current_node, current_node))) = min_heap.pop() {
            if distance_to_current_node > shortest_distances[current_node] {
                continue;
            }
            if distance_to_current_node <= max_moves {
                reachable_node_count += 1;
            }

            for &(neighbor_node, edge_weight) in &adjacency_list[current_node] {
                let distance_to_neighbor = distance_to_current_node + edge_weight + 1;

                if distance_to_neighbor < shortest_distances[neighbor_node] && distance_to_neighbor <= max_moves {
                    shortest_distances[neighbor_node] = distance_to_neighbor;
                    min_heap.push(Reverse((distance_to_neighbor, neighbor_node)));
                }
            }
        }

        for edge in edges {
            let start = edge[0] as usize;
            let end = edge[1] as usize;
            let subdivisions = edge[2];
            let reachable_from_start = 0.max(max_moves - shortest_distances[start]);
            let reachable_from_end = 0.max(max_moves - shortest_distances[end]);
            reachable_node_count += subdivisions.min(reachable_from_start + reachable_from_end);
        }

        reachable_node_count
    }
}


//https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/submissions/1365476549/
```
```JavaScript []

```
