
### Intuition
We're being asked to add two numbers. But these numbers are represented as linked lists and not just any linked lists but ones where:

> a) The digits are in reverse order
 b) Each node contains a single digit

This representation immediately raises some interesting questions. Why reverse order? How does this change our typical approach to addition? Let's consider a simple example:

342 + 465 = 807
In our linked list representation, this becomes: [2,4,3] + [5,6,4] = [7,0,8]

Do you see what's happening here? The least significant digits (2 and 5) are at the head of the list. This is actually quite convenient for addition, isn't it In normal addition we start from the right-most digits and work our way left. Here we can start from the head of the list and work our way through.


Try to convert these linked lists back into regular integers add them, and then convert the result back into a linked list. But let's think about that for a moment. What if the numbers are really large? We might run into integer overflow issues.

So, we need to work with the linked list representation directly. But how?

Remember how we do addition by hand? We start from the right-most digit, add the corresponding digits from both numbers, carry over any excess to the next column, and repeat. Can we mimic this process with our linked lists?



Let's think about the mathematical properties at play here. When we add two single-digit numbers, what's the maximum possible result? 9 + 9 = 18. So our sum can be at most two digits.

This gives us an important insight: at each step of our addition, we'll have:
- A sum of two digits (0-18)
- A single-digit result (0-9)
- A potential carry (0 or 1)

Mathematically, we can express this as:

$result = (digit1 + digit2 + carry) % 10$
$newcarry = (digit1 + digit2 + carry) / 10$  (integer division)

This forms the core of our addition algorithm. Now that we understand the mathematical foundation, how do we apply this to our linked lists? We could traverse both lists simultaneously, adding corresponding digits (and the carry from the previous step). But what if the lists are of different lengths? we need to continue our addition process as long as there are digits left in either list, or if there's a carry left over.

So, our process might look something like this:

    1. Start at the head of both lists
    2. While there are still digits in either list or a carry:
    a. Get the digit from list1 (if available, else use 0)
    b. Get the digit from list2 (if available, else use 0)
    c. Add these digits and the carry
    d. Create a new node with the result % 10
    e. Update the carry for the next iteration
    f. Move to the next nodes in both lists (if available)



We also need to consider some edge cases:

- What if one list is longer than the other? 
  Our approach of using 0 when a list runs out handles this.

- What if we have a carry after processing all digits?
  We need to ensure our loop continues even if both lists are exhausted, as long as there's a carry.

- What about leading zeros? 
  The problem states we don't have to worry about this, except for the number 0 itself.

- Empty lists?
  The problem specifies non-empty lists, but it's good to keep in mind.


If you think through this process, you might think how do we build our result list? We could start from the head, but that would require us to reverse our result at the end (remember, least significant digit comes first).A common technique in linked list problems is to use a dummy head node. This simplifies our list building process:

>   1 Create a dummy node
    2. Maintain a "current" pointer, starting at the dummy node
    3. As we calculate each digit of the result, add it as a new node after the current node
    4. Move the current pointer to this new node
    5. At the end, our result is dummy.next (skipping the dummy node itself)

This will allows us to build our result list in the correct order as we go, without needing to reverse it at the end.



Our approach works directly with the linked list representation, avoiding potential integer overflow issues. It mimics the grade-school addition process, which is intuitive and easy to understand. It handles lists of different lengths naturally, without needing separate logic. The use of a dummy head simplifies our list-building process.

The reverse order of digits actually works in our favor aligning perfectly with how we perform addition from right to left.



# Approach


As we have already talked that we're asked to add two numbers the numbers are represented as linked lists where each node contains a single digit, and the digits are in reverse order. For example:

342 + 465 = 807
Is represented as:
[2,4,3] + [5,6,4] = [7,0,8]

This reverse order is key to our solution, as it aligns perfectly with how we typically perform addition: from right to left (least significant digit to most significant digit).



Let's break it down into a high-level algorithm:

```pseudocode
function addTwoNumbers(l1, l2):
    initialize dummy node
    initialize current pointer to dummy node
    initialize carry to 0
    
    while l1 is not null OR l2 is not null OR carry is not 0:
        calculate sum of current digits and carry
        create new node with ones digit of sum
        update carry for next iteration
        move to next digits in both lists (if available)
    
    return dummy.next as head of result list
```





**a) Dummy Node and Current Pointer:**

```pseudocode
dummy = new ListNode(0)
current = dummy
```

The dummy node is a crucial technique in linked list problems. It serves as a placeholder at the beginning of our result list, simplifying the process of building the list. Here's why it's valuable:

- It eliminates the need for special case handling of the first node.
- It provides a consistent starting point for our result list.
- At the end, dummy.next will be the head of our actual result list.

The current pointer keeps track of where we are in building our result list. We start it at the dummy node and move it as we add new nodes.

**b) Carry Variable:**

```pseudocode
carry = 0
```

The carry variable is fundamental to the addition process. In decimal addition, when the sum of two digits exceeds 9, we "carry" 1 to the next column. Our carry variable simulates this process.

- It's initialized to 0 at the start.
- After each digit addition, it will hold any value that needs to be carried to the next column (0 or 1).

**c) Main Loop:**

```pseudocode
while l1 is not null OR l2 is not null OR carry is not 0:
```

This loop condition is crucial for handling various scenarios:

- It continues as long as there are digits left in either list (l1 or l2 is not null).
- It also continues if there's a remaining carry, even if both lists are exhausted.

This condition ensures we process all digits and handle cases where the result has more digits than either input number (e.g., 999 + 1 = 1000).

**d) Sum Calculation:**

```pseudocode
sum = carry
if l1 is not null:
    sum += l1.value
    l1 = l1.next
if l2 is not null:
    sum += l2.value
    l2 = l2.next
```

This step calculates the sum for the current digit position:

- We start with the carry from the previous iteration.
- We add the current digit from l1 if available (if not, it's effectively 0).
- We add the current digit from l2 if available (if not, it's effectively 0).
- We move to the next node in each list if available.

This approach elegantly handles lists of different lengths without needing separate logic.

**e) New Node Creation:**

```pseudocode
current.next = new ListNode(sum % 10)
current = current.next
```

Here's where we build our result list:

- sum % 10 gives us the ones digit of our sum (0-9), which is what we want for our current result digit.
- We create a new node with this value and attach it to our result list.
- We move our current pointer to this new node, preparing for the next iteration.

**f) Carry Update:**

```pseudocode
carry = sum / 10  (integer division)
```

This step prepares the carry for the next iteration:

- Integer division by 10 gives us the tens digit of our sum (0 or 1).
- This becomes the carry for the next column, just like in manual addition.



**When we add two decimal numbers:**  We add digits in each place value (ones, tens, hundreds, etc.) separately and If the sum in any place value is 10 or greater, we keep the ones digit in that place and carry the tens digit to the next place value.

Our algorithm mimics this process:
>- sum % 10 gives us the ones digit (0-9) for our current place value.
>- sum / 10 (integer division) gives us the carry (0 or 1) for the next place value.

This approach works because:
$(a + b)$ % 10 = (($a$ % 10) + ($b$ % 10)) % 10

This property allows us to process each digit independently, carrying over any excess to the next digit.



Our algorithm naturally handles several edge cases:

>**a) Lists of Different Lengths:**
By checking if each list is null before adding its digit, we effectively treat exhausted lists as having 0 in each subsequent place value. This eliminates the need for separate logic to handle different list lengths.

>**b) Carry Propagation:**
Including carry != 0 in our loop condition ensures we continue adding nodes even if both lists are exhausted but we still have a carry. This handles cases like:
  999 + 1 = 1000

>**c) Single-Digit Numbers:**
Our algorithm works seamlessly for single-digit numbers, including zero, without any special cases.

>**d) Large Numbers:**
By processing digits one at a time and using a linked list for the result, we avoid integer overflow issues that could occur if we tried to convert the entire number to an integer before adding.










# Complexity

**Time Complexity: O(max(N, M))**

Where N and M are the lengths of the input lists.

Why? We traverse both lists once. The number of operations is determined by the length of the longer list. If one list is longer, we'll keep going until we reach its end.

**Space Complexity: O(max(N, M))**

We create a new list for our result. In the worst case (like 999 + 1), our result list will be one node longer than the longer input list.

These complexities are optimal for this problem. We need to look at every digit at least once (hence the time complexity), and we need to store the result (hence the space complexity).

In practical terms: *Doubling the input size will roughly double the execution time and memory usage. The algorithm scales linearly, which is efficient for this type of problem.*

---

# Code
```java []
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int sum = carry;

            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }

            current.next = new ListNode(sum % 10);
            current = current.next;
            carry = sum / 10;
        }

        return dummy.next;
    }
}
```

```C++ []
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;
        
        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            int sum = carry;
            
            if (l1 != nullptr) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                sum += l2->val;
                l2 = l2->next;
            }
            
            carry = sum / 10;
            current->next = new ListNode(sum % 10);
            current = current->next;
        }
        
        ListNode* result = dummy->next;
        delete dummy;  // Free the dummy node
        return result;
    }
};
```

```Python []
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            sum = carry
            
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
        
        return dummy.next
        
```
```JavaScript []
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let dummy = new ListNode(0);
    let current = dummy;
    let carry = 0;
    
    while (l1 || l2 || carry) {
        let sum = carry;
        
        if (l1) {
            sum += l1.val;
            l1 = l1.next;
        }
        if (l2) {
            sum += l2.val;
            l2 = l2.next;
        }
        
        carry = Math.floor(sum / 10);
        current.next = new ListNode(sum % 10);
        current = current.next;
    }
    
    return dummy.next;
};
```

```Go []
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummy := &ListNode{Val: 0}
    current := dummy
    carry := 0
    
    for l1 != nil || l2 != nil || carry != 0 {
        sum := carry
        
        if l1 != nil {
            sum += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            sum += l2.Val
            l2 = l2.Next
        }
        
        carry = sum / 10
        current.Next = &ListNode{Val: sum % 10}
        current = current.Next
    }
    
    return dummy.Next
}
```
```Rust []

impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode::new(0));
        let mut current = &mut dummy;
        let mut carry = 0;
        let mut p = l1;
        let mut q = l2;
        
        while p.is_some() || q.is_some() || carry != 0 {
            let mut sum = carry;
            
            if let Some(node) = p {
                sum += node.val;
                p = node.next;
            }
            if let Some(node) = q {
                sum += node.val;
                q = node.next;
            }
            
            carry = sum / 10;
            current.next = Some(Box::new(ListNode::new(sum % 10)));
            current = current.next.as_mut().unwrap();
        }
        
        dummy.next
    }
}

```
---

# Follow-up: Non-Reversed Order Linked Lists

In this variation, the digits are stored in forward order. So now:
(3→4→2) represents 342
(4→6→5) represents 465

Our goal is to add these and produce (8→0→7) representing 807.

# New Challenges

This change introduces some new challenges:
1. We can't start adding from the head of the lists anymore, as these are now the most significant digits.
2. We don't know if we need to carry a digit until we've processed all less significant digits.
3. The lengths of the lists might be different, and we need to align the numbers properly.

# Approach

We can solve this problem with the following approach:

1. Reverse both input lists.
2. Apply our original solution to the reversed lists.
3. Reverse the result.

Alternatively, we could use a recursive approach or a stack-based approach to process the digits from least significant to most significant without actually reversing the lists.

Let's outline the recursive approach:

1. Find the lengths of both lists.
2. Pad the shorter list with leading zeros to make both lists equal length.
3. Use recursion to traverse to the end of both lists.
4. As we return from recursion, perform the addition.
5. Handle any final carry.

# Implementation

Here's how we could implement this recursive approach:

```java []
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int len1 = getLength(l1);
        int len2 = getLength(l2);
        
        // Pad the shorter list with leading zeros
        if (len1 < len2) {
            l1 = padList(l1, len2 - len1);
        } else if (len2 < len1) {
            l2 = padList(l2, len1 - len2);
        }
        
        CarryNode result = addListsRecursive(l1, l2);
        
        if (result.carry != 0) {
            ListNode newHead = new ListNode(result.carry);
            newHead.next = result.node;
            return newHead;
        }
        
        return result.node;
    }
    
    private CarryNode addListsRecursive(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) {
            return new CarryNode(null, 0);
        }
        
        CarryNode result = addListsRecursive(l1.next, l2.next);
        
        int sum = l1.val + l2.val + result.carry;
        ListNode newNode = new ListNode(sum % 10);
        newNode.next = result.node;
        
        return new CarryNode(newNode, sum / 10);
    }
    
    private int getLength(ListNode head) {
        int length = 0;
        while (head != null) {
            length++;
            head = head.next;
        }
        return length;
    }
    
    private ListNode padList(ListNode head, int padding) {
        while (padding > 0) {
            ListNode newNode = new ListNode(0);
            newNode.next = head;
            head = newNode;
            padding--;
        }
        return head;
    }
    
    private class CarryNode {
        ListNode node;
        int carry;
        
        CarryNode(ListNode node, int carry) {
            this.node = node;
            this.carry = carry;
        }
    }
}
```

```Python []
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1 = self.getLength(l1)
        len2 = self.getLength(l2)
        
        if len1 < len2:
            l1 = self.padList(l1, len2 - len1)
        elif len2 < len1:
            l2 = self.padList(l2, len1 - len2)
        
        result = self.addListsRecursive(l1, l2)
        if result[1] != 0:
            new_head = ListNode(result[1])
            new_head.next = result[0]
            return new_head
        return result[0]
    
    def addListsRecursive(self, l1, l2):
        if not l1 and not l2:
            return None, 0
        next_node, carry = self.addListsRecursive(l1.next, l2.next)
        sum_val = l1.val + l2.val + carry
        new_node = ListNode(sum_val % 10)
        new_node.next = next_node
        return new_node, sum_val // 10
    
    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def padList(self, head, padding):
        while padding > 0:
            new_node = ListNode(0)
            new_node.next = head
            head = new_node
            padding -= 1
        return head
```
```C++ []
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int len1 = getLength(l1);
        int len2 = getLength(l2);
        
        if (len1 < len2) {
            l1 = padList(l1, len2 - len1);
        } else if (len2 < len1) {
            l2 = padList(l2, len1 - len2);
        }
        
        auto result = addListsRecursive(l1, l2);
        if (result.carry != 0) {
            auto newHead = new ListNode(result.carry);
            newHead->next = result.node;
            return newHead;
        }
        return result.node;
    }

private:
    struct CarryNode {
        ListNode* node;
        int carry;
        CarryNode(ListNode* n, int c) : node(n), carry(c) {}
    };
    
    CarryNode addListsRecursive(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr && l2 == nullptr) {
            return CarryNode(nullptr, 0);
        }
        auto result = addListsRecursive(l1->next, l2->next);
        int sum = l1->val + l2->val + result.carry;
        auto newNode = new ListNode(sum % 10);
        newNode->next = result.node;
        return CarryNode(newNode, sum / 10);
    }
    
    int getLength(ListNode* head) {
        int length = 0;
        while (head != nullptr) {
            length++;
            head = head->next;
        }
        return length;
    }
    
    ListNode* padList(ListNode* head, int padding) {
        while (padding > 0) {
            auto newNode = new ListNode(0);
            newNode->next = head;
            head = newNode;
            padding--;
        }
        return head;
    }
};
```
```JavaScript []
var addTwoNumbers = function(l1, l2) {
    const getLength = (head) => {
        let length = 0;
        while (head) {
            length++;
            head = head.next;
        }
        return length;
    };
    
    const padList = (head, padding) => {
        while (padding > 0) {
            const newNode = new ListNode(0);
            newNode.next = head;
            head = newNode;
            padding--;
        }
        return head;
    };
    
    const addListsRecursive = (l1, l2) => {
        if (!l1 && !l2) {
            return { node: null, carry: 0 };
        }
        const result = addListsRecursive(l1.next, l2.next);
        const sum = l1.val + l2.val + result.carry;
        const newNode = new ListNode(sum % 10);
        newNode.next = result.node;
        return { node: newNode, carry: Math.floor(sum / 10) };
    };
    
    const len1 = getLength(l1);
    const len2 = getLength(l2);
    
    if (len1 < len2) {
        l1 = padList(l1, len2 - len1);
    } else if (len2 < len1) {
        l2 = padList(l2, len1 - len2);
    }
    
    const result = addListsRecursive(l1, l2);
    if (result.carry !== 0) {
        const newHead = new ListNode(result.carry);
        newHead.next = result.node;
        return newHead;
    }
    return result.node;
};
```
```Go []
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    len1 := getLength(l1)
    len2 := getLength(l2)
    
    if len1 < len2 {
        l1 = padList(l1, len2 - len1)
    } else if len2 < len1 {
        l2 = padList(l2, len1 - len2)
    }
    
    result := addListsRecursive(l1, l2)
    if result.carry != 0 {
        newHead := &ListNode{Val: result.carry, Next: result.node}
        return newHead
    }
    return result.node
}

type CarryNode struct {
    node *ListNode
    carry int
}

func addListsRecursive(l1 *ListNode, l2 *ListNode) CarryNode {
    if l1 == nil && l2 == nil {
        return CarryNode{nil, 0}
    }
    result := addListsRecursive(l1.Next, l2.Next)
    sum := l1.Val + l2.Val + result.carry
    newNode := &ListNode{Val: sum % 10, Next: result.node}
    return CarryNode{newNode, sum / 10}
}

func getLength(head *ListNode) int {
    length := 0
    for head != nil {
        length++
        head = head.Next
    }
    return length
}

func padList(head *ListNode, padding int) *ListNode {
    for padding > 0 {
        newNode := &ListNode{Val: 0, Next: head}
        head = newNode
        padding--
    }
    return head
}
```

# Complexity Analysis

**Time Complexity: O(max(N, M))**, where N and M are the lengths of the input lists.
- We traverse each list once to find its length.
- We traverse again during the recursive calls.
- Each node is processed once during addition.

**Space Complexity: O(max(N, M))**
- The recursion stack will go as deep as the length of the longer list.
- The result list will be at most one node longer than the longer input list.

# Key Differences from the Original Problem

1. **Pre-processing:** We need to find list lengths and potentially pad the shorter list.
2. **Recursion:** We use recursion to effectively process digits from right to left.
3. **Carry Handling:** We propagate the carry as we return from recursive calls.
4. **Result Construction:** We build our result list from right to left as we return from recursion.

This approach maintains the same time and space complexity as the original problem, but with a more complex implementation to handle the forward-order representation.
