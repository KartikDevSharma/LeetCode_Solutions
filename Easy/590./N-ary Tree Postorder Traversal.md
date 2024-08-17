
# Intuition

When we first encounter this problem our mind naturally gravitates towards the recursive nature of tree structures. Trees, by their very definition, are recursive data structures - each node can be thought of as the root of its own subtree.

The postorder traversal requires us to visit all the children of a node before visiting the node itself. This immediately suggests a depth-first approach, where we dive deep into the tree structure before we start collecting node values.

Consider a tree where each node is a person in a family tree. In a postorder traversal, we'd want to visit all of a person's descendants before visiting the person themselves. It's like tracing a family lineage from the youngest generation up to the oldest.

The key insight here is that we need to fully explore each child's subtree before we can process the parent node. This naturally lends itself to a recursive solution, where we can leverage the call stack to keep track of our position in the tree as we dive deeper and deeper into the structure.

# Approach

Let's break down our approach step-by-step:

1. We start by defining our main function, let's call it `postorder_traversal`. This function will take the root of our N-ary tree as input and return a list of integers representing the postorder traversal.

2. Our first step in this function is to handle the base case. If the root is null (an empty tree), we should return an empty list.

   ```
   function postorder_traversal(root):
       if root is null:
           return empty list
   ```

3. Next, we initialize an empty list to store our results. This list will contain the values of the nodes in postorder.

   ```
   result = empty list
   ```

4. Now comes the heart of our solution. We need a helper function to perform the actual traversal. Let's call this `traverse`. This function will take a node and our result list as parameters.

   ```
   function traverse(node, result):
   ```

5. Inside `traverse`, we first need to handle all the children of the current node. We do this by iterating over the children and recursively calling `traverse` on each child.

   ```
   for each child in node.children:
       traverse(child, result)
   ```

6. After we've processed all the children, we can finally add the current node's value to our result list.

   ```
   append node.value to result
   ```

7. Back in our main `postorder_traversal` function, we call our `traverse` helper function with the root node and our result list.

   ```
   traverse(root, result)
   ```

8. Finally, we return the result list containing the postorder traversal.

   ```
   return result
   ```

Putting it all together, our pseudo-code looks like this:

```
function postorder_traversal(root):
    if root is null:
        return empty list
    
    result = empty list
    
    function traverse(node, result):
        for each child in node.children:
            traverse(child, result)
        append node.value to result
    
    traverse(root, result)
    return result
```

This approach mimics the natural structure of the tree. We're essentially saying, "For each node, first deal with all its children, then deal with the node itself." This recursive approach allows us to easily handle trees of any depth and with any number of children per node.

This solution closely maps to our intuitive understanding of postorder traversal. As we recurse deeper into the tree, we're building up a series of function calls on the call stack. Each of these calls represents a node waiting for its children to be processed. Only when we reach a leaf node (a node with no children) do we start adding values to our result list and unwinding the call stack.

### Complexity
- **Time complexity: O(N)**, where N is the number of nodes in the tree. We visit each node exactly once, performing constant-time operations for each visit.

- **Space complexity: O(H)**, where H is the height of the tree. This space is used by the call stack during the recursive calls. In the worst case of a completely unbalanced tree, this could be O(N), but for a balanced tree, it would be O(log N).

The space complexity doesn't include the space used by the output list, as that's generally not counted when discussing space complexity of algorithms. If we were to include it, the space complexity would be O(N) in all cases, as the output list will always contain all N nodes.

### Code
```Java []
class Solution {
    public List<Integer> postorder(Node treeRoot) {
        List<Integer> traversalOutput = new ArrayList<>();
        if (treeRoot == null) {
            return traversalOutput;
        }
        executePostorderTraversal(treeRoot, traversalOutput);
        return traversalOutput;
    }
    
    private void executePostorderTraversal(
        Node currentElement,
        List<Integer> outputSequence
    ) {
        if (currentElement == null) {
            return;
        }
        
        switch (currentElement.children.size()) {
            case 0:
                break;
            default:
                for (Node childElement : currentElement.children) {
                    executePostorderTraversal(childElement, outputSequence);
                }
        }
        
        outputSequence.add(currentElement.val);
    }
}



//https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/1358014770/
```
```C++ []
class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> traversalOutput;
        if (!root) return traversalOutput;
        
        executePostorderTraversal(root, traversalOutput);
        return traversalOutput;
    }

private:
    void executePostorderTraversal(Node* node, vector<int>& output) {
        if (!node) return;

        for (Node* child : node->children) {
            executePostorderTraversal(child, output);
        }

        output.push_back(node->val);
    }
};

static const int speedup = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();



//https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/1358108575/
```
```Python []
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, treeRoot: 'Node') -> list[int]:
        traversal_output = []
        if treeRoot is None:
            return traversal_output
        self.execute_postorder_traversal(treeRoot, traversal_output)
        return traversal_output
    
    def execute_postorder_traversal(self, current_element: 'Node', output_sequence: list[int]):
        if current_element is None:
            return
        
        for child_element in current_element.children:
            self.execute_postorder_traversal(child_element, output_sequence)
        
        output_sequence.append(current_element.val)


```
```Go []
func postorder(root *Node) []int {
    var result []int
    if root == nil {
        return result
    }
    return executePostorderTraversal(root)
}

func executePostorderTraversal(node *Node) []int {
    var output []int
    if node == nil {
        return output
    }

    for _, child := range node.Children {
        output = append(output, executePostorderTraversal(child)...)
    }
    output = append(output, node.Val)
    return output
}

//https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/1358112473/
```

```JavaScript []
/**
 * Definition for a _Node.
 * function _Node(val, children) {
 *     this.val = val;
 *     this.children = children;
 * }
 */

/**
 * @param {_Node|null} root
 * @return {number[]}
 */
var postorder = function(root) {
    const result = [];
    if (root === null) {
        return result;
    }
    executePostorderTraversal(root, result);
    return result;
};

function executePostorderTraversal(node, result) {
    if (node === null) {
        return;
    }

    for (const child of node.children) {
        executePostorderTraversal(child, result);
    }
    result.push(node.val);
}

//https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/1358113850/
```
---

### Dry Run

### Example 1: `root = [1,null,3,2,4,null,5,6]`

Here is the structure of the N-ary tree:
```
        1
       /|\
      3 2 4
     / \
    5   6
```

**Expected Postorder Output**: `[5, 6, 3, 2, 4, 1]`

Let's dry run it step by step:

| Step | Call Stack                                           | Node Processed | Result List  | Comments                                      |
|------|------------------------------------------------------|----------------|--------------|-----------------------------------------------|
| 1    | `postorder(1)`                                       | -              | `[]`         | Start postorder traversal from root `1`.      |
| 2    | `executePostorderTraversal(1)`                       | -              | `[]`         | Process node `1`, recursively process its children. |
| 3    | `executePostorderTraversal(3)`                       | -              | `[]`         | Process node `3`, recursively process its children. |
| 4    | `executePostorderTraversal(5)`                       | -              | `[]`         | Process node `5`, no children, add to result. |
| 5    | `executePostorderTraversal(6)`                       | `5` added      | `[5]`        | Process node `6`, no children, add to result. |
| 6    | Returning to `executePostorderTraversal(3)`           | `6` added      | `[5, 6]`     | All children of `3` processed, add `3` to result. |
| 7    | `executePostorderTraversal(2)`                       | `3` added      | `[5, 6, 3]`  | Process node `2`, no children, add to result. |
| 8    | `executePostorderTraversal(4)`                       | `2` added      | `[5, 6, 3, 2]`| Process node `4`, no children, add to result. |
| 9    | Returning to `executePostorderTraversal(1)`           | `4` added      | `[5, 6, 3, 2, 4]`| All children of `1` processed, add `1` to result. |
| 10   | -                                                    | `1` added      | `[5, 6, 3, 2, 4, 1]`| Postorder traversal complete.                |

**Final Output**: `[5, 6, 3, 2, 4, 1]`

---

### Example 2: `root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`

Here is the structure of the N-ary tree:
```
        1
     / / \  \
    2  3   4   5
      / \   \  \  \
     6   7   8  9  10
          |  |   |
         11  12  13
          |  
         14
```

**Expected Postorder Output**: `[2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]`

Let's dry run it step by step:

| Step | Call Stack                                           | Node Processed | Result List  | Comments                                      |
|------|------------------------------------------------------|----------------|--------------|-----------------------------------------------|
| 1    | `postorder(1)`                                       | -              | `[]`         | Start postorder traversal from root `1`.      |
| 2    | `executePostorderTraversal(1)`                       | -              | `[]`         | Process node `1`, recursively process its children. |
| 3    | `executePostorderTraversal(2)`                       | -              | `[]`         | Process node `2`, no children, add to result. |
| 4    | `executePostorderTraversal(3)`                       | `2` added      | `[2]`        | Process node `3`, recursively process its children. |
| 5    | `executePostorderTraversal(6)`                       | -              | `[2]`        | Process node `6`, no children, add to result. |
| 6    | `executePostorderTraversal(7)`                       | `6` added      | `[2, 6]`     | Process node `7`, recursively process its child `11`. |
| 7    | `executePostorderTraversal(11)`                      | -              | `[2, 6]`     | Process node `11`, recursively process its child `14`. |
| 8    | `executePostorderTraversal(14)`                      | -              | `[2, 6]`     | Process node `14`, no children, add to result. |
| 9    | Returning to `executePostorderTraversal(11)`          | `14` added     | `[2, 6, 14]` | All children of `11` processed, add `11` to result. |
| 10   | Returning to `executePostorderTraversal(7)`           | `11` added     | `[2, 6, 14, 11]`| All children of `7` processed, add `7` to result. |
| 11   | Returning to `executePostorderTraversal(3)`           | `7` added      | `[2, 6, 14, 11, 7]`| All children of `3` processed, add `3` to result. |
| 12   | `executePostorderTraversal(4)`                       | `3` added      | `[2, 6, 14, 11, 7, 3]`| Process node `4`, recursively process its child `8`. |
| 13   | `executePostorderTraversal(8)`                       | -              | `[2, 6, 14, 11, 7, 3]`| Process node `8`, recursively process its child `12`. |
| 14   | `executePostorderTraversal(12)`                      | -              | `[2, 6, 14, 11, 7, 3]`| Process node `12`, no children, add to result. |
| 15   | Returning to `executePostorderTraversal(8)`           | `12` added     | `[2, 6, 14, 11, 7, 3, 12]`| All children of `8` processed, add `8` to result. |
| 16   | Returning to `executePostorderTraversal(4)`           | `8` added      | `[2, 6, 14, 11, 7, 3, 12, 8]`| All children of `4` processed, add `4` to result. |
| 17   | `executePostorderTraversal(5)`                       | `4` added      | `[2, 6, 14, 11, 7, 3, 12, 8, 4]`| Process node `5`, recursively process its children `9` and `10`. |
| 18   | `executePostorderTraversal(9)`                       | -              | `[2, 6, 14, 11, 7, 3, 12, 8, 4]`| Process node `9`, recursively process its child `13`. |
| 19   | `executePostorderTraversal(13)`                      | -              | `[2, 6, 14, 11, 7, 3, 12, 8, 4]`| Process node `13`, no children, add to result. |
| 20   | Returning to `executePostorderTraversal(9)`           | `13` added     | `[2, 6, 14, 11, 7, 3, 12, 8, 4, 13]`| All children of `9` processed, add `9` to result. |
| 21   | `executePostorderTraversal(10)`                      | `9` added      | `[2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9]`| Process node `10`, no children, add to result. |
| 22   | Returning to `executePostorderTraversal(5)`           | `10` added     | `[2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10]`| All children of `5` processed, add `5` to result. |
| 23   | Returning to `executePostorderTraversal(1)`           | `5` added      | `[2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5

]`| All children of `1` processed, add `1` to result. |
| 24   | -                                                    | `1` added      | `[2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]`| Postorder traversal complete.                |

**Final Output**: `[2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]`

---



