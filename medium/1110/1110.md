![1100.png](https://github.com/KartikDevSharma/LeetCode_Solutions/blob/main/medium/1110/1100.png)

![dfs2.png](https://assets.leetcode.com/users/images/54175522-2c69-4609-8681-7bfb9d82dbad_1721195415.695838.png)

## Problem Statement
### 1. The Problem Setup:
   - You're given a binary tree. A binary tree is a tree-like structure where each node has at most two children (left and right).
   - The root of the tree is given to you. The root is the topmost node of the tree.
   - Each node in this tree has a unique value (no two nodes have the same value).
   - You're also given an array called `to_delete`. This array contains values of nodes that need to be deleted from the tree.

### 2. What You Need to Do:
   - Your task is to delete all the nodes whose values are in the `to_delete` array.
   - After deleting these nodes, the original tree might break into multiple smaller trees. This collection of smaller trees is called a forest.
   - You need to return a list of the root nodes of all these smaller trees.

### 3. Understanding the Process:
   - When you delete a node:
     - If it's a leaf node (no children), you simply remove it.
     - If it has children, those children become roots of new trees in the forest.
   - The nodes that aren't deleted and don't have a parent after deletions become roots of trees in the forest.

### 4. Examples Explained:

   Example 1:
   ```
   Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
   ```
   - The tree looks like this:
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
   - You need to delete nodes with values 3 and 5.
   - After deletion:
     - Node 1 remains the root of a tree (with 2 and 4 as its descendants)
     - Node 6 becomes the root of a new tree
     - Node 7 becomes the root of another new tree
   - So the output is [[1,2,null,4],[6],[7]]

   Example 2:
   ```
   Input: root = [1,2,4,null,3], to_delete = [3]
   ```
   - The tree looks like this:
         1
       /   \
      2     4
       \
        3
   - You need to delete the node with value 3.
   - After deletion, only the original tree remains intact (just without node 3).
   - So the output is [[1,2,4]]

### 5. Constraints to Keep in Mind:
   - The tree won't have more than 1000 nodes.
   - Node values are between 1 and 1000.
   - The `to_delete` array won't have more than 1000 elements.

### 6. Approach to Solve:
   - You'll likely need to traverse the tree (e.g., using depth-first search).
   - As you traverse, you'll check if each node's value is in the `to_delete` array.
   - If a node needs to be deleted, you'll need to handle its children appropriately.
   - Keep track of the roots of new trees formed after deletions.

Remember, the order of the trees in your output doesn't matter. The important thing is to correctly identify and return all the root nodes of the trees in the resulting forest.



# Intuition and Approach: Depth-First Search (DFS) with Node Deletion

The approach used in this solution can be termed as "Depth-First Search (DFS) with Node Deletion". This method combines the power of DFS traversal with an efficient mechanism for node deletion and forest construction. Let's break down the intuition and approach in great detail:

## Intuition:

The core idea behind this solution is to traverse the entire binary tree once, making decisions about each node as we go. We need to determine which nodes to delete, which nodes become new roots in our forest, and how to handle the children of deleted nodes. 

A depth-first approach is intuitive here because:

1. It allows us to process each node exactly once.
2. We can make decisions about a node before processing its children, which is crucial for determining if those children will become new roots.
3. It naturally follows the tree structure, making it easier to reason about parent-child relationships.

The use of a boolean array for marking nodes to delete is a clever optimization. Since we know the range of node values (1 to 1000), we can use this array for O(1) lookups, which is faster than using a HashSet.

## Approach:

Let's dive deep into the approach, examining each part of the code:

1. Class Setup:
   ```java
   class Solution {
       private boolean[] toDelete = new boolean[1001];
       private List<TreeNode> forest = new ArrayList<>();
       // ...
   }
   ```
   - We initialize a boolean array `toDelete` of size 1001 (since node values range from 1 to 1000).
   - We also create a list `forest` to store the roots of our resulting trees.

2. Main Method:
   ```java
   public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
       for (int val : to_delete) {
           toDelete[val] = true;
       }
       
       dfs(root, true);
       
       return forest;
   }
   ```
   - We first mark all the nodes that need to be deleted by setting their corresponding indices in `toDelete` to true.
   - We then call our DFS method on the root, passing `true` to indicate that it's initially a root.
   - Finally, we return our forest of remaining trees.

3. DFS Method:
   ```java
   private TreeNode dfs(TreeNode node, boolean isRoot) {
       if (node == null) {
           return null;
       }
       
       boolean shouldDelete = toDelete[node.val];
       
       if (isRoot && !shouldDelete) {
           forest.add(node);
       }
       
       node.left = dfs(node.left, shouldDelete);
       node.right = dfs(node.right, shouldDelete);
       
       return shouldDelete ? null : node;
   }
   ```
   This is the heart of our solution. Let's break it down further:

   a. Base case:
      ```java
      if (node == null) {
          return null;
      }
      ```
      If we reach a null node, we simply return null. This handles leaf nodes and empty subtrees.

   b. Deletion check:
      ```java
      boolean shouldDelete = toDelete[node.val];
      ```
      We check if the current node should be deleted by looking up its value in our `toDelete` array.

   c. Forest construction:
      ```java
      if (isRoot && !shouldDelete) {
          forest.add(node);
      }
      ```
      If the current node is a root (either the original root or a child of a deleted node) and it's not marked for deletion, we add it to our forest.

   d. Recursive calls:
      ```java
      node.left = dfs(node.left, shouldDelete);
      node.right = dfs(node.right, shouldDelete);
      ```
      We recursively process the left and right children. Note that we pass `shouldDelete` as the `isRoot` parameter for the children. This is because if the current node is deleted, its children will become new roots.

   e. Return value:
      ```java
      return shouldDelete ? null : node;
      ```
      If the current node should be deleted, we return null (effectively removing it from the tree). Otherwise, we return the node itself.

This approach elegantly handles all the requirements of the problem:
- It deletes nodes by returning null when `shouldDelete` is true.
- It constructs the forest by adding nodes to `forest` when they're roots and not deleted.
- It maintains the tree structure for non-deleted nodes.
- It turns children of deleted nodes into new roots by passing `shouldDelete` as the `isRoot` parameter in recursive calls.

## Complexity

### Time Complexity: O(N)

The time complexity of this solution is O(N), where N is the number of nodes in the binary tree. Here's a detailed breakdown:

1. Initialization of `toDelete` array:
   - This takes O(D) time, where D is the length of the `to_delete` array.
   - Since D ≤ N (we can't delete more nodes than exist), this step is O(N) in the worst case.

2. DFS traversal:
   - The DFS method visits each node in the tree exactly once.
   - For each node, we perform constant time operations:
     - Checking if the node is null: O(1)
     - Checking if the node should be deleted: O(1) (array lookup)
     - Possibly adding the node to the forest: O(1) (amortized time for ArrayList add)
     - Making recursive calls: O(1) (not counting the time within the recursive calls)
   - Since we visit each node once and perform constant time operations at each node, the overall time for DFS is O(N).

3. Returning the result:
   - This is a simple return of the `forest` list, which is O(1).

Combining all these steps, we get:
O(N) + O(N) + O(1) = O(N)

It's worth noting that while we have two O(N) terms, we don't add them to get O(2N) because in Big O notation, we drop constant factors.

### Space Complexity: O(N)

The space complexity is also O(N). Here's why:

1. `toDelete` array:
   - This is a boolean array of size 1001, which is O(1) space as it's a constant size regardless of the input.

2. `forest` list:
   - In the worst case, if no nodes are deleted, this could contain all N nodes of the tree.
   - Therefore, this could take up to O(N) space.

3. Recursion stack:
   - The depth of the recursion is equal to the height of the tree.
   - In the worst case (a completely unbalanced tree), this could be O(N).
   - In a balanced tree, this would be O(log N), but we consider the worst case for Big O notation.

4. Input storage:
   - We need to store the input tree, which takes O(N) space.
   - The `to_delete` array takes O(D) space, where D ≤ N.

Taking the maximum of these space requirements:
max(O(1), O(N), O(N), O(N)) = O(N)

It's important to note that while we have multiple O(N) terms, in Big O notation we're concerned with the order of growth, not the exact amount of memory used. Therefore, we express the overall space complexity as O(N).

This space complexity is essentially optimal for this problem, as we need to be able to represent the entire input tree and potentially return all nodes in the worst case.

### Dry Run Example
For dry run of the algorithm using a sample binary tree. Let's use the following example:

```
Input: 
root = [1,2,3,4,5,6,7]
to_delete = [3,5]
```

This tree looks like:

```
     1
   /   \
  2     3
 / \   / \
4   5 6   7
```

Here's a detailed dry run in:

| Step | Action | Node | isRoot | shouldDelete | forest | Left Child | Right Child | Return Value |
|------|--------|------|--------|--------------|--------|------------|-------------|--------------|
| 1 | Initialize | - | - | - | [] | - | - | - |
| 2 | Mark to_delete | - | - | - | [] | - | - | - |
| 3 | Call dfs(1, true) | 1 | true | false | [1] | - | - | - |
| 4 | dfs(2, false) | 2 | false | false | [1] | - | - | - |
| 5 | dfs(4, false) | 4 | false | false | [1] | null | null | 4 |
| 6 | dfs(5, false) | 5 | false | true | [1] | null | null | null |
| 7 | Return to 2 | 2 | false | false | [1] | 4 | null | 2 |
| 8 | dfs(3, false) | 3 | false | true | [1] | - | - | - |
| 9 | dfs(6, true) | 6 | true | false | [1,6] | null | null | 6 |
| 10 | dfs(7, true) | 7 | true | false | [1,6,7] | null | null | 7 |
| 11 | Return to 3 | 3 | false | true | [1,6,7] | 6 | 7 | null |
| 12 | Return to 1 | 1 | true | false | [1,6,7] | 2 | null | 1 |
| 13 | Final Result | - | - | - | [1,6,7] | - | - | - |

Explanation of what's happening behind the scenes:

1. We start by initializing an empty forest.
2. We mark nodes 3 and 5 for deletion in the `toDelete` array.
3. We begin DFS with the root node 1. It's not to be deleted, so we add it to the forest.
4. We move to node 2. It's not a root and not to be deleted, so we don't add it to the forest.
5. We process node 4. It's a leaf node, not to be deleted, so we return it as is.
6. We process node 5. It's to be deleted, so we return null, effectively removing it from the tree.
7. We return to node 2, updating its left child to 4 and right child to null (since 5 was deleted).
8. We move to node 3. It's to be deleted, but we process its children first.
9. We process node 6. Because its parent (3) will be deleted, it's treated as a root and added to the forest.
10. Similarly, we process node 7, adding it to the forest as a new root.
11. We return to node 3, which is deleted (return null).
12. Finally, we return to the root (1). Its left child is 2, and its right child is now null (since 3 was deleted).
13. The algorithm completes, and we return the forest containing nodes 1, 6, and 7 as roots of separate trees.

This dry run illustrates how the algorithm:
- Traverses the tree in a depth-first manner
- Handles deletion of nodes
- Creates new roots for the forest when necessary
- Maintains the structure of non-deleted subtrees

The final result `[1,6,7]` represents three trees:
- A tree rooted at 1 with 2 and 4 as descendants
- A single-node tree with 6
- A single-node tree with 7

This matches the expected output `[[1,2,null,4],[6],[7]]` from the problem statement.

## Code
```java []
class Solution {
    private boolean[] toDelete = new boolean[1001];
    private List<TreeNode> forest = new ArrayList<>();

    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        for (int val : to_delete) {
            toDelete[val] = true;
        }
        
        dfs(root, true);
        
        return forest;
    }
    
    private TreeNode dfs(TreeNode node, boolean isRoot) {
        if (node == null) {
            return null;
        }
        
        boolean shouldDelete = toDelete[node.val];
        
        if (isRoot && !shouldDelete) {
            forest.add(node);
        }
        
        node.left = dfs(node.left, shouldDelete);
        node.right = dfs(node.right, shouldDelete);
        
        return shouldDelete ? null : node;
    }
}
```
```python []
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []
        
        def dfs(node, is_root):
            if not node:
                return None
            
            is_deleted = node.val in to_delete_set
            if is_root and not is_deleted:
                forest.append(node)
            
            node.left = dfs(node.left, is_deleted)
            node.right = dfs(node.right, is_deleted)
            
            return None if is_deleted else node
        
        dfs(root, True)
        return forest
```
```c++ []
class Solution {
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        vector<TreeNode*> forest;
        unordered_set<int> to_delete_set(to_delete.begin(), to_delete.end());
        
        dfs(root, true, to_delete_set, forest);
        return forest;
    }
    
private:
    TreeNode* dfs(TreeNode* node, bool is_root, unordered_set<int>& to_delete_set, vector<TreeNode*>& forest) {
        if (!node) return nullptr;
        
        bool should_delete = to_delete_set.count(node->val);
        
        if (is_root && !should_delete) {
            forest.push_back(node);
        }
        
        node->left = dfs(node->left, should_delete, to_delete_set, forest);
        node->right = dfs(node->right, should_delete, to_delete_set, forest);
        
        return should_delete ? nullptr : node;
    }
};
```
```js []
/**
 * @param {TreeNode} root
 * @param {number[]} to_delete
 * @return {TreeNode[]}
 */
var delNodes = function(root, to_delete) {
    const toDeleteSet = new Set(to_delete);
    const forest = [];
    
    const dfs = (node, isRoot) => {
        if (!node) return null;
        
        const shouldDelete = toDeleteSet.has(node.val);
        
        if (isRoot && !shouldDelete) {
            forest.push(node);
        }
        
        node.left = dfs(node.left, shouldDelete);
        node.right = dfs(node.right, shouldDelete);
        
        return shouldDelete ? null : node;
    };
    
    dfs(root, true);
    return forest;
};
```
```go []
func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
    toDeleteMap := make(map[int]bool)
    for _, val := range to_delete {
        toDeleteMap[val] = true
    }
    
    var forest []*TreeNode
    
    var dfs func(*TreeNode, bool) *TreeNode
    dfs = func(node *TreeNode, isRoot bool) *TreeNode {
        if node == nil {
            return nil
        }
        
        shouldDelete := toDeleteMap[node.Val]
        
        if isRoot && !shouldDelete {
            forest = append(forest, node)
        }
        
        node.Left = dfs(node.Left, shouldDelete)
        node.Right = dfs(node.Right, shouldDelete)
        
        if shouldDelete {
            return nil
        }
        return node
    }
    
    dfs(root, true)
    return forest
}
```


## Recursive Approach (Simplified version of the solution):

Intuition:
This solution is based on the fundamental principle of recursion in tree traversal. The idea is to visit each node in the tree exactly once, making a decision about whether to delete it or keep it. By using recursion, we can elegantly handle the tree structure, allowing the solution to naturally adapt to any tree shape or size.

The key insight here is that when we delete a node, its children potentially become new roots in our forest. This recursive approach allows us to handle this situation smoothly: as we return up the recursion stack, we're essentially "bubbling up" the information about deleted nodes, allowing parent nodes to properly handle their children.

Detailed Approach:
1. Initialize a Set (toDelete) with the values of nodes to be deleted. We use a Set for O(1) lookup time, which is more efficient than scanning through an array each time we need to check if a node should be deleted.

2. Create an ArrayList (forest) to store the roots of our resulting forest.

3. Define a helper method (deleteNodes) that takes three parameters:
   - The current node
   - A boolean indicating if this node is currently considered a root

4. In the deleteNodes method:
   - If the node is null, return null (base case of recursion)
   - Check if the current node's value is in the toDelete Set
   - If the node is a root and shouldn't be deleted, add it to our forest
   - Recursively call deleteNodes on the left and right children
     - Pass true for the isRoot parameter if the current node should be deleted, as this will make the children new roots if they're not deleted
   - If the current node should be deleted, return null (which will remove it from its parent's reference)
   - If not deleted, return the node itself

5. In the main delNodes method, call deleteNodes on the root with isRoot set to true


```java []
class Solution {
    private Set<Integer> toDelete;
    private List<TreeNode> forest;

    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        toDelete = new HashSet<>();
        forest = new ArrayList<>();
        
        for (int val : to_delete) {
            toDelete.add(val);
        }
        
        deleteNodes(root, true);
        return forest;
    }
    
    private TreeNode deleteNodes(TreeNode node, boolean isRoot) {
        if (node == null) return null;
        
        boolean shouldDelete = toDelete.contains(node.val);
        
        if (isRoot && !shouldDelete) {
            forest.add(node);
        }
        
        node.left = deleteNodes(node.left, shouldDelete);
        node.right = deleteNodes(node.right, shouldDelete);
        
        return shouldDelete ? null : node;
    }
}

```

```python []
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.to_delete = set(to_delete)
        self.forest = []
        
        def delete_nodes(node: TreeNode, is_root: bool) -> TreeNode:
            if not node:
                return None
            
            should_delete = node.val in self.to_delete
            
            if is_root and not should_delete:
                self.forest.append(node)
            
            node.left = delete_nodes(node.left, should_delete)
            node.right = delete_nodes(node.right, should_delete)
            
            return None if should_delete else node
        
        delete_nodes(root, True)
        return self.forest

```
```c++ []
class Solution {
private:
    unordered_set<int> toDelete;
    vector<TreeNode*> forest;
    
    TreeNode* deleteNodes(TreeNode* node, bool isRoot) {
        if (!node) return nullptr;
        
        bool shouldDelete = toDelete.count(node->val);
        
        if (isRoot && !shouldDelete) {
            forest.push_back(node);
        }
        
        node->left = deleteNodes(node->left, shouldDelete);
        node->right = deleteNodes(node->right, shouldDelete);
        
        return shouldDelete ? nullptr : node;
    }
    
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        for (int val : to_delete) {
            toDelete.insert(val);
        }
        
        deleteNodes(root, true);
        return forest;
    }
};
```
```Js []

/**
 * @param {TreeNode} root
 * @param {number[]} to_delete
 * @return {TreeNode[]}
 */
var delNodes = function(root, to_delete) {
    const toDelete = new Set(to_delete);
    const forest = [];
    
    function deleteNodes(node, isRoot) {
        if (!node) return null;
        
        const shouldDelete = toDelete.has(node.val);
        
        if (isRoot && !shouldDelete) {
            forest.push(node);
        }
        
        node.left = deleteNodes(node.left, shouldDelete);
        node.right = deleteNodes(node.right, shouldDelete);
        
        return shouldDelete ? null : node;
    }
    
    deleteNodes(root, true);
    return forest;
};
```
```Go []

func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
    toDelete := make(map[int]bool)
    for _, val := range to_delete {
        toDelete[val] = true
    }
    
    var forest []*TreeNode
    
    var deleteNodes func(*TreeNode, bool) *TreeNode
    deleteNodes = func(node *TreeNode, isRoot bool) *TreeNode {
        if node == nil {
            return nil
        }
        
        shouldDelete := toDelete[node.Val]
        
        if isRoot && !shouldDelete {
            forest = append(forest, node)
        }
        
        node.Left = deleteNodes(node.Left, shouldDelete)
        node.Right = deleteNodes(node.Right, shouldDelete)
        
        if shouldDelete {
            return nil
        }
        return node
    }
    
    deleteNodes(root, true)
    return forest
}
```
### Time Complexity:
The time complexity of this solution is O(N), where N is the number of nodes in the tree. This is because we visit each node in the tree exactly once during our recursion. The Set operations (adding to toDelete and checking if a value is in toDelete) are O(1) on average, so they don't increase our overall time complexity.

### Space Complexity:
The space complexity is O(H + M), where H is the height of the tree and M is the number of nodes to delete.
- O(H) comes from the recursion stack. In the worst case of a skewed tree, this could be O(N), but for a balanced tree, it would be O(log N).
- O(M) is for the toDelete Set.
- The space for the forest ArrayList is not counted in the additional space complexity as it's part of the output.

Pros:
- Clean and intuitive implementation
- Handles the tree structure naturally
- Efficient for most tree shapes

Cons:
- Could lead to stack overflow for very deep trees
- Might be slightly harder to understand for those not familiar with recursive tree traversals

Difference from Original Solution:
The main difference from the original solution is the use of a Set instead of a boolean array for toDelete. This makes the solution more space-efficient when the number of nodes to delete is much smaller than the range of node values. The core logic and recursive structure remain very similar.

## Iterative Approach using Queue (BFS):

Intuition:

This solution leverages the power of Breadth-First Search (BFS) to traverse the tree level by level. The key insight here is that by using a queue, we can keep track of additional information about each node (its parent, whether it's a left or right child, and if it's a root) without needing to pass this information through recursive calls.

This approach "flattens" the tree traversal, which can be beneficial for very deep trees where recursion might cause stack overflow. It also allows us to process the tree in a very systematic, level-by-level manner, which can be more intuitive for some problems.

Detailed Approach:
1. Initialize a Set (toDeleteSet) with the values of nodes to be deleted, similar to the recursive approach.

2. Create an ArrayList (forest) to store the roots of our resulting forest.

3. Initialize a queue for BFS traversal. Each element in the queue is an Object array containing:
   - The current node
   - Its parent node
   - A Boolean indicating if it's a left child (null for the root)
   - A Boolean indicating if it's currently considered a root

4. Add the root node to the queue, with null parent, null for isLeftChild, and true for isRoot.

5. While the queue is not empty:
   - Poll an element from the queue
   - If the node is null, continue to the next iteration
   - Check if the current node's value is in the toDeleteSet
   - If the node is a root and shouldn't be deleted, add it to our forest
   - If the node should be deleted:
     - If it has a parent, set the appropriate child of the parent to null
     - Add its children to the queue as potential new roots
   - If the node shouldn't be deleted:
     - Add its children to the queue, maintaining the parent relationship


```java []
class Solution {
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        Set<Integer> toDeleteSet = new HashSet<>();
        for (int val : to_delete) {
            toDeleteSet.add(val);
        }
        
        List<TreeNode> forest = new ArrayList<>();
        Queue<Object[]> queue = new LinkedList<>();
        queue.offer(new Object[]{root, null, null, true}); // node, parent, isLeftChild, isRoot
        
        while (!queue.isEmpty()) {
            Object[] curr = queue.poll();
            TreeNode node = (TreeNode) curr[0];
            TreeNode parent = (TreeNode) curr[1];
            Boolean isLeftChild = (Boolean) curr[2];
            boolean isRoot = (Boolean) curr[3];
            
            if (node == null) continue;
            
            boolean shouldDelete = toDeleteSet.contains(node.val);
            
            if (isRoot && !shouldDelete) {
                forest.add(node);
            }
            
            if (shouldDelete) {
                if (parent != null) {
                    if (isLeftChild) {
                        parent.left = null;
                    } else {
                        parent.right = null;
                    }
                }
                queue.offer(new Object[]{node.left, null, null, true});
                queue.offer(new Object[]{node.right, null, null, true});
            } else {
                queue.offer(new Object[]{node.left, node, true, false});
                queue.offer(new Object[]{node.right, node, false, false});
            }
        }
        
        return forest;
    }
}
```

```python []

from collections import deque

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []
        queue = deque([(root, None, None, True)])  # node, parent, is_left_child, is_root
        
        while queue:
            node, parent, is_left_child, is_root = queue.popleft()
            
            if not node:
                continue
            
            should_delete = node.val in to_delete_set
            
            if is_root and not should_delete:
                forest.append(node)
            
            if should_delete:
                if parent:
                    if is_left_child:
                        parent.left = None
                    else:
                        parent.right = None
                queue.append((node.left, None, None, True))
                queue.append((node.right, None, None, True))
            else:
                queue.append((node.left, node, True, False))
                queue.append((node.right, node, False, False))
        
        return forest
```
```c++ []
class Solution {
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_set<int> toDeleteSet(to_delete.begin(), to_delete.end());
        vector<TreeNode*> forest;
        queue<tuple<TreeNode*, TreeNode*, bool, bool>> q;  // node, parent, isLeftChild, isRoot
        q.push({root, nullptr, false, true});
        
        while (!q.empty()) {
            auto [node, parent, isLeftChild, isRoot] = q.front();
            q.pop();
            
            if (!node) continue;
            
            bool shouldDelete = toDeleteSet.count(node->val);
            
            if (isRoot && !shouldDelete) {
                forest.push_back(node);
            }
            
            if (shouldDelete) {
                if (parent) {
                    if (isLeftChild) {
                        parent->left = nullptr;
                    } else {
                        parent->right = nullptr;
                    }
                }
                q.push({node->left, nullptr, false, true});
                q.push({node->right, nullptr, false, true});
            } else {
                q.push({node->left, node, true, false});
                q.push({node->right, node, false, false});
            }
        }
        
        return forest;
    }
};

```
```js []
/**
 * @param {TreeNode} root
 * @param {number[]} to_delete
 * @return {TreeNode[]}
 */
var delNodes = function(root, to_delete) {
    const toDeleteSet = new Set(to_delete);
    const forest = [];
    const queue = [[root, null, null, true]];  // node, parent, isLeftChild, isRoot
    
    while (queue.length > 0) {
        const [node, parent, isLeftChild, isRoot] = queue.shift();
        
        if (!node) continue;
        
        const shouldDelete = toDeleteSet.has(node.val);
        
        if (isRoot && !shouldDelete) {
            forest.push(node);
        }
        
        if (shouldDelete) {
            if (parent) {
                if (isLeftChild) {
                    parent.left = null;
                } else {
                    parent.right = null;
                }
            }
            queue.push([node.left, null, null, true]);
            queue.push([node.right, null, null, true]);
        } else {
            queue.push([node.left, node, true, false]);
            queue.push([node.right, node, false, false]);
        }
    }
    
    return forest;
};

```
```go []
func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
    toDeleteSet := make(map[int]bool)
    for _, val := range to_delete {
        toDeleteSet[val] = true
    }
    
    forest := []*TreeNode{}
    queue := [][]interface{}{{root, nil, nil, true}}  // node, parent, isLeftChild, isRoot
    
    for len(queue) > 0 {
        curr := queue[0]
        queue = queue[1:]
        
        node := curr[0].(*TreeNode)
        parent := curr[1].(*TreeNode)
        isLeftChild, _ := curr[2].(bool)
        isRoot := curr[3].(bool)
        
        if node == nil {
            continue
        }
        
        shouldDelete := toDeleteSet[node.Val]
        
        if isRoot && !shouldDelete {
            forest = append(forest, node)
        }
        
        if shouldDelete {
            if parent != nil {
                if isLeftChild {
                    parent.Left = nil
                } else {
                    parent.Right = nil
                }
            }
            queue = append(queue, []interface{}{node.Left, nil, nil, true})
            queue = append(queue, []interface{}{node.Right, nil, nil, true})
        } else {
            queue = append(queue, []interface{}{node.Left, node, true, false})
            queue = append(queue, []interface{}{node.Right, node, false, false})
        }
    }
    
    return forest
}

```
### Time Complexity:

The time complexity remains O(N), where N is the number of nodes in the tree. We still process each node exactly once, just in a different order compared to the recursive approach.

### Space Complexity:

The space complexity is O(W + M), where W is the maximum width of the tree and M is the number of nodes to delete.
- O(W) comes from the queue used for BFS. In the worst case (a complete binary tree), this could be O(N/2) for the last level.
- O(M) is for the toDeleteSet.

Pros:
- Avoids potential stack overflow issues with very deep trees
- Can be easier to understand for those more familiar with iterative approaches
- Allows for easy addition of extra node information (parent, isLeftChild, isRoot)

Cons:
- Requires more complex queue management
- Can use more memory for wide, shallow trees due to queue size

### Difference from Original Solution:
This solution is fundamentally different from the original recursive approach. It uses an iterative BFS traversal instead of a recursive DFS. This change in traversal strategy allows it to handle additional node information more easily but at the cost of a more complex implementation.

## 3. Single-Pass Recursive Solution:

Intuition:
This solution aims to combine the marking (identifying nodes to delete) and collecting (building the forest) steps into a single pass through the tree. The key insight is that we can make decisions about each node as we encounter it, rather than needing a separate marking phase.

This approach is similar to the first recursive solution, but it's designed to be more streamlined, making decisions and updating the forest in a single pass.

Detailed Approach:
1. Initialize a Set (toDeleteSet) with the values of nodes to be deleted.

2. Create an ArrayList (forest) to store the roots of our resulting forest.

3. Define a helper method (deleteNodes) that takes two parameters:
   - The current node
   - A boolean indicating if this node is currently considered a root

4. In the deleteNodes method:
   - If the node is null, return null (base case of recursion)
   - Check if the current node's value is in the toDeleteSet
   - If the node is a root and shouldn't be deleted, add it to our forest
   - Recursively call deleteNodes on the left and right children
     - Pass true for the isRoot parameter if the current node should be deleted
   - If the current node should be deleted, return null
   - If not deleted, return the node itself

5. In the main delNodes method, call deleteNodes on the root with isRoot set to true

```java []
class Solution {
    private Set<Integer> toDeleteSet;
    private List<TreeNode> forest;

    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        toDeleteSet = new HashSet<>();
        forest = new ArrayList<>();
        
        for (int val : to_delete) {
            toDeleteSet.add(val);
        }
        
        // Process the root separately
        root = deleteNodes(root, true);
        
        return forest;
    }
    
    private TreeNode deleteNodes(TreeNode node, boolean isRoot) {
        if (node == null) return null;
        
        boolean shouldDelete = toDeleteSet.contains(node.val);
        
        if (isRoot && !shouldDelete) {
            forest.add(node);
        }
        
        node.left = deleteNodes(node.left, shouldDelete);
        node.right = deleteNodes(node.right, shouldDelete);
        
        return shouldDelete ? null : node;
    }
}

```
```python []
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.to_delete_set = set(to_delete)
        self.forest = []
        
        def delete_nodes(node: TreeNode, is_root: bool) -> TreeNode:
            if not node:
                return None
            
            should_delete = node.val in self.to_delete_set
            
            if is_root and not should_delete:
                self.forest.append(node)
            
            node.left = delete_nodes(node.left, should_delete)
            node.right = delete_nodes(node.right, should_delete)
            
            return None if should_delete else node
        
        delete_nodes(root, True)
        return self.forest
```
```c++ []
class Solution {
private:
    unordered_set<int> toDeleteSet;
    vector<TreeNode*> forest;
    
    TreeNode* deleteNodes(TreeNode* node, bool isRoot) {
        if (!node) return nullptr;
        
        bool shouldDelete = toDeleteSet.count(node->val);
        
        if (isRoot && !shouldDelete) {
            forest.push_back(node);
        }
        
        node->left = deleteNodes(node->left, shouldDelete);
        node->right = deleteNodes(node->right, shouldDelete);
        
        return shouldDelete ? nullptr : node;
    }
    
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        for (int val : to_delete) {
            toDeleteSet.insert(val);
        }
        
        deleteNodes(root, true);
        return forest;
    }
};
```
```js []
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number[]} to_delete
 * @return {TreeNode[]}
 */
var delNodes = function(root, to_delete) {
    const toDeleteSet = new Set(to_delete);
    const forest = [];
    
    function deleteNodes(node, isRoot) {
        if (!node) return null;
        
        const shouldDelete = toDeleteSet.has(node.val);
        
        if (isRoot && !shouldDelete) {
            forest.push(node);
        }
        
        node.left = deleteNodes(node.left, shouldDelete);
        node.right = deleteNodes(node.right, shouldDelete);
        
        return shouldDelete ? null : node;
    }
    
    deleteNodes(root, true);
    return forest;
};
```
```go []
func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
    toDeleteSet := make(map[int]bool)
    for _, val := range to_delete {
        toDeleteSet[val] = true
    }
    
    var forest []*TreeNode
    
    var deleteNodes func(*TreeNode, bool) *TreeNode
    deleteNodes = func(node *TreeNode, isRoot bool) *TreeNode {
        if node == nil {
            return nil
        }
        
        shouldDelete := toDeleteSet[node.Val]
        
        if isRoot && !shouldDelete {
            forest = append(forest, node)
        }
        
        node.Left = deleteNodes(node.Left, shouldDelete)
        node.Right = deleteNodes(node.Right, shouldDelete)
        
        if shouldDelete {
            return nil
        }
        return node
    }
    
    deleteNodes(root, true)
    return forest
}
```

### Time Complexity:
The time complexity is O(N), where N is the number of nodes in the tree. We visit each node once during the traversal.

### Space Complexity:
The space complexity is O(H + M), where H is the height of the tree and M is the number of nodes to delete.
- O(H) comes from the recursion stack.
- O(M) is for the toDeleteSet.

Pros:
- Combines marking and collecting into a single pass, potentially making the code more concise
- Maintains the intuitive recursive structure
- Efficient for most tree shapes

Cons:
- Could still lead to stack overflow for very deep trees
- Might be slightly harder to modify if additional operations are needed during traversal

### Difference from Original Solution:
This solution is quite similar to the original solution in its recursive nature. The main difference is that it combines the deletion and collection of new roots into a single pass, whereas the original solution used a separate boolean array for marking nodes to delete. This solution also uses a Set instead of a boolean array, making it more space-efficient for sparse delete lists.

### Comparison and Conclusion:

All three solutions, including the original one, solve the problem correctly and have the same time complexity of O(N). The main differences lie in their space complexity, ease of understanding, and ability to handle different tree shapes.

the original solution used a boolean array to mark nodes for deletion, which has a fixed space complexity of O(1000) regardless of the input size. This can be memory-efficient if the range of node values is small and dense, but less so if the range is large or sparse.

The new solutions use a Set, which adapts to the actual number of nodes to delete. This is generally more space-efficient, especially when the number of nodes to delete is much smaller than the range of node values.

The iterative BFS solution (Solution 2) provides a fundamentally different approach. It's particularly useful for very deep trees where recursion might cause stack overflow. However, it can use more memory for wide, shallow trees due to the queue size.

In terms of readability and maintainability:

- The recursive solutions (1 and 3) are generally more concise and can be easier to understand for those familiar with recursive tree traversals.
- The iterative solution (2) might be easier to modify if you need to keep track of additional information about each node during traversal.

In practice, the choice between these solutions would depend on:
    1. The expected shape of the input trees (deep vs. wide)
    2. The range and distribution of node values
    3. The likelihood of extremely large inputs that might cause stack overflow
    4. The familiarity of the development team with recursive vs. iterative approaches
    5. Any additional requirements or potential future modifications to the algorithm

Each solution has its strengths, and the "best" choice would depend on the specific requirements and constraints of the system in which this code will be used.
