
Approach 1: Depth First Search
Intuition
In this problem, each node in the binary tree is represented by a 3-digit integer, where the unit digit holds the node's value, and the other digits indicate the node's position in the tree. Our goal is to find the sum of all root-to-leaf paths. To do this efficiently, we can use either depth-first search (DFS) or breadth-first search (BFS).


In this approach, we will use the DFS algorithm. The DFS algorithm explores as far as possible along each branch before backing up, which mirrors the path-like exploration from root to leaf. The figure below illustrates the paths:

![imageeditorial.png](https://assets.leetcode.com/users/images/6e5ed00d-ac4c-4e88-aa79-1f0f6567039c_1724872617.0069056.png)


As we observe from the image, the depth of the nodes increases with each DFS iteration. For example, if a node is at depth 2, its children will be at depth 3, meaning the depth of each child is the current node's depth plus one.

To determine the horizontal position of the child nodes, if a node is at position p, its left child will be at 2*p - 1, and its right child at 2*p. This calculation is based on the properties of a full binary tree, where positions double as you move deeper. It's a standard formula that you can remember for future use.

Each node is uniquely identified by its depth and position, which we can map to the node's value. Using a hashmap, where the key is the node's depth and position, and the value is the node's value, we can efficiently retrieve any node's value using its coordinates.

Algorithm
Main function - pathSum(nums)

If nums is empty, return 0.
Initialize a hashmap map to store tree nodes.
Iterate through each element in nums:
Calculate coordinates by dividing the current element by 10.
Calculate value by taking the remainder of the element when divided by 10.
Store the coordinates as the key and value as the value in map.
Initialize an integer variable sum with 0.
Call the helper function dfs(rootCoordinates, preSum, sum, map) with:
rootCoordinates set to nums[0] / 10.
preSum set to 0.
sum passed by reference.
Return the value of sum.
Helper function - dfs(rootCoordinates, preSum, sum, map)

Calculate the level and position from rootCoordinates:
level is obtained by dividing rootCoordinates by 10.
position is obtained by taking the remainder of rootCoordinates when divided by 10.
Determine the coordinates of the left and right children:
left is calculated as (level + 1) * 10 + position * 2 - 1.
right is calculated as (level + 1) * 10 + position * 2.
Update currSum by adding the value of the current node to preSum.
If map does not contain both left and right coordinates:
Add currSum to sum.
Return from the function.
If left exists in map, call dfs(left, currSum, sum, map).
If right exists in map, call dfs(right, currSum, sum, map).


```Java 
class Solution {

    Map<Integer, Integer> map = new HashMap<>();

    public int pathSum(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        // Store the data in a hashmap, with the coordinates as the key and the
        // node value as the value
        for (int num : nums) {
            int key = num / 10;
            int value = num % 10;
            map.put(key, value);
        }

        return dfs(nums[0] / 10, 0);
    }

    private int dfs(int root, int preSum) {
        // Find the level and position values from the coordinates
        int level = root / 10;
        int pos = root % 10;

        //the left child and right child position in the tree
        int left = (level + 1) * 10 + pos * 2 - 1;
        int right = (level + 1) * 10 + pos * 2;
        int currSum = preSum + map.get(root);

        // If the node is a leaf node, return its root to leaf path sum.
        if (!map.containsKey(left) && !map.containsKey(right)) {
            return currSum;
        }

        // Otherwise iterate through the left and right children recursively
        // using depth first search
        int leftSum = map.containsKey(left) ? dfs(left, currSum) : 0;
        int rightSum = map.containsKey(right) ? dfs(right, currSum) : 0;

        //return the total path sum of the tree rooted at the current node
        return leftSum + rightSum;
    }
}
```

Approach 2: Breadth First Search
Intuition
In this approach, we use the breadth-first search algorithm to explore all root-to-leaf paths in the tree. Unlike depth-first search, where we explore each path from root to leaf before moving on, BFS processes all nodes at the current level before proceeding to the next.

To track the running sum as we reach leaf nodes, we initialize a queue that stores pairs of coordinates and the current sum up to each node. We start by enqueuing the root node. While the queue is not empty, we process each node by checking if it is a leaf. If it is not a leaf, we enqueue its children with updated sums by adding the current node's value to the running sum. If the node is a leaf, we add the current sum to the total sum.

Algorithm
Initialize map as an empty hashmap, and q as an empty queue that stores a pair of integers.
Initialize totalSum as 0.
For each element in nums:
Compute coordinates as element / 10.
Compute value as element % 10.
Store value in the map with key coordinates.
Compute rootCoordinates as nums[0] / 10.
Enqueue rootCoordinates and map[rootCoordinates] into q.
While q is not empty:
Dequeue coordinates and currentSum.
Compute level as coordinates / 10 and position as coordinates % 10.
Compute left as (level + 1) * 10 + position * 2 - 1 and right as (level + 1) * 10 + position * 2.
If the current node is a leaf node:
Add currentSum to totalSum.
If map contains left:
Enqueue left and currentSum + map[left] into q.
If map contains right:
Enqueue right and currentSum + map[right] into q.
Return totalSum.
Implementation

```Java
class Solution {

    public int pathSum(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        // Store the node values in a hashmap, using coordinates as the key.
        Map<Integer, Integer> map = new HashMap<>();
        for (int element : nums) {
            int coordinates = element / 10;
            int value = element % 10;
            map.put(coordinates, value);
        }

        // Initialize the BFS queue and start with the root node.
        Queue<Pair<Integer, Integer>> q = new LinkedList<>();
        int totalSum = 0;

        int rootCoordinates = nums[0] / 10;
        q.add(
            new Pair<Integer, Integer>(
                rootCoordinates,
                map.get(rootCoordinates)
            )
        );

        while (!q.isEmpty()) {
            Pair<Integer, Integer> current = q.poll();
            int coordinates = current.getKey();
            int currentSum = current.getValue();
            int level = coordinates / 10;
            int position = coordinates % 10;

            // Find the left and right child coordinates.
            int left = (level + 1) * 10 + position * 2 - 1;
            int right = (level + 1) * 10 + position * 2;

            // If it's a leaf node (no left and right children), add currentSum to totalSum.
            if (!map.containsKey(left) && !map.containsKey(right)) {
                totalSum += currentSum;
            }

            // Add the left child to the queue if it exists.
            if (map.containsKey(left)) {
                q.add(
                    new Pair<Integer, Integer>(left, currentSum + map.get(left))
                );
            }

            // Add the right child to the queue if it exists.
            if (map.containsKey(right)) {
                q.add(
                    new Pair<Integer, Integer>(
                        right,
                        currentSum + map.get(right)
                    )
                );
            }
        }

        return totalSum;
    }
}

```
