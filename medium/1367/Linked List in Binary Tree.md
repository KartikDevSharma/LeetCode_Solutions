Java
```Java []

class Solution {
    public boolean isSubPath(ListNode linkedListHead, TreeNode treeRoot) {
        return searchForPath(linkedListHead, linkedListHead, treeRoot);
    }
    private boolean searchForPath(ListNode pathStart, ListNode currentNode, TreeNode treeNode) {
        if (currentNode == null) {
            return true;
        }
        if (treeNode == null) {
            return false;
        }
        
        if (currentNode.val == treeNode.val) {
            currentNode = currentNode.next;
        } else if (pathStart.val == treeNode.val) {
            pathStart = pathStart.next;
        } else {
            currentNode = pathStart;
        }
        
        return searchForPath(pathStart, currentNode, treeNode.left) || 
               searchForPath(pathStart, currentNode, treeNode.right);
    }
}
```
C++
```C++ []
class Solution {
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        return searchForPath(head, head, root);
    }
private:
    bool searchForPath(ListNode* pathStart, ListNode* currentNode, TreeNode* treeNode) {
        if (currentNode == nullptr) {
            return true;
        }
        if (treeNode == nullptr) {
            return false;
        }
        
        if (currentNode->val == treeNode->val) {
            currentNode = currentNode->next;
        } else if (pathStart->val == treeNode->val) {
            pathStart = pathStart->next;
        } else {
            currentNode = pathStart;
        }
        
        return searchForPath(pathStart, currentNode, treeNode->left) || 
               searchForPath(pathStart, currentNode, treeNode->right);
    }
};
```
Python
```Python []
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def searchForPath(pathStart: ListNode, currentNode: ListNode, treeNode: TreeNode) -> bool:
            if not currentNode:
                return True
            if not treeNode:
                return False
            
            if currentNode.val == treeNode.val:
                currentNode = currentNode.next
            elif pathStart.val == treeNode.val:
                pathStart = pathStart.next
            else:
                currentNode = pathStart
            
            return searchForPath(pathStart, currentNode, treeNode.left) or \
                   searchForPath(pathStart, currentNode, treeNode.right)
        
        return searchForPath(head, head, root)
```
Go
```Go []
func isSubPath(head *ListNode, root *TreeNode) bool {
    var searchForPath func(*ListNode, *ListNode, *TreeNode) bool
    searchForPath = func(pathStart, currentNode *ListNode, treeNode *TreeNode) bool {
        if currentNode == nil {
            return true
        }
        if treeNode == nil {
            return false
        }
        
        if currentNode.Val == treeNode.Val {
            currentNode = currentNode.Next
        } else if pathStart.Val == treeNode.Val {
            pathStart = pathStart.Next
        } else {
            currentNode = pathStart
        }
        
        return searchForPath(pathStart, currentNode, treeNode.Left) || 
               searchForPath(pathStart, currentNode, treeNode.Right)
    }
    
    return searchForPath(head, head, root)
}
```

JavaScript
```JavaScript []
/**
 * @param {ListNode} head
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSubPath = function(head, root) {
    const searchForPath = (pathStart, currentNode, treeNode) => {
        if (currentNode === null) {
            return true;
        }
        if (treeNode === null) {
            return false;
        }
        
        if (currentNode.val === treeNode.val) {
            currentNode = currentNode.next;
        } else if (pathStart.val === treeNode.val) {
            pathStart = pathStart.next;
        } else {
            currentNode = pathStart;
        }
        
        return searchForPath(pathStart, currentNode, treeNode.left) || 
               searchForPath(pathStart, currentNode, treeNode.right);
    };
    
    return searchForPath(head, head, root);
};
```
