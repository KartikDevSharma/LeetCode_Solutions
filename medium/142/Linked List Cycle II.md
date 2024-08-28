
```java
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return null; // No cycle if list is empty or has only one node
        }

        ListNode tortoise = head;
        ListNode hare = head;

        // Phase 1: Detect cycle
        while (hare != null && hare.next != null) {
            tortoise = tortoise.next;
            hare = hare.next.next;
            
            if (tortoise == hare) {
                // Cycle detected, move to phase 2
                tortoise = head;
                while (tortoise != hare) {
                    tortoise = tortoise.next;
                    hare = hare.next;
                }
                return tortoise; // This is the start of the cycle
            }
        }

        return null; // No cycle found
    }
}

```
```cpp []
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head || !head->next) {
            return nullptr;
        }

        ListNode *tortoise = head;
        ListNode *hare = head;

        // Phase 1: Detect cycle
        while (hare && hare->next) {
            tortoise = tortoise->next;
            hare = hare->next->next;

            if (tortoise == hare) {
                // Cycle detected, move to phase 2
                tortoise = head;
                while (tortoise != hare) {
                    tortoise = tortoise->next;
                    hare = hare->next;
                }
                return tortoise;  // This is the start of the cycle
            }
        }

        return nullptr;  // No cycle found
    }
};

```

```python []
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        tortoise = head
        hare = head

        # Phase 1: Detect cycle
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                # Cycle detected, move to phase 2
                tortoise = head
                while tortoise != hare:
                    tortoise = tortoise.next
                    hare = hare.next
                return tortoise  # This is the start of the cycle

        return None  # No cycle found

```

```go []

func detectCycle(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return nil
    }

    tortoise := head
    hare := head

    // Phase 1: Detect cycle
    for hare != nil && hare.Next != nil {
        tortoise = tortoise.Next
        hare = hare.Next.Next

        if tortoise == hare {
            // Cycle detected, move to phase 2
            tortoise = head
            for tortoise != hare {
                tortoise = tortoise.Next
                hare = hare.Next
            }
            return tortoise  // This is the start of the cycle
        }
    }

    return nil  // No cycle found
}

```

```rust []


use std::ptr::NonNull;

impl Solution {
    pub fn detect_cycle(head: Option<Box<ListNode>>) -> Option<NonNull<ListNode>> {
        let mut head_ptr = head.as_deref().map(|node| NonNull::from(&*node));
        
        if head_ptr.is_none() || head_ptr.unwrap().as_ref().next.is_none() {
            return None;
        }

        let mut tortoise = head_ptr;
        let mut hare = head_ptr;

        // Phase 1: Detect cycle
        while hare.is_some() && hare.unwrap().as_ref().next.is_some() {
            tortoise = tortoise.unwrap().as_ref().next.as_deref().map(NonNull::from);
            hare = hare.unwrap().as_ref().next.as_deref().and_then(|node| node.next.as_deref().map(NonNull::from));

            if tortoise == hare {
                // Cycle detected, move to phase 2
                tortoise = head_ptr;
                while tortoise != hare {
                    tortoise = tortoise.unwrap().as_ref().next.as_deref().map(NonNull::from);
                    hare = hare.unwrap().as_ref().next.as_deref().map(NonNull::from);
                }
                return tortoise;  // This is the start of the cycle
            }
        }

        None  // No cycle found
    }
}

```

```javascript []


/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
    if (!head || !head.next) {
        return null;
    }

    let tortoise = head;
    let hare = head;

    // Phase 1: Detect cycle
    while (hare && hare.next) {
        tortoise = tortoise.next;
        hare = hare.next.next;

        if (tortoise === hare) {
            // Cycle detected, move to phase 2
            tortoise = head;
            while (tortoise !== hare) {
                tortoise = tortoise.next;
                hare = hare.next;
            }
            return tortoise;  // This is the start of the cycle
        }
    }

    return null;  // No cycle found
};

```

