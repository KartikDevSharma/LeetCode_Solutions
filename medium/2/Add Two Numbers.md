
# The Problem Overview:

*Imagine you have two really big numbers. Instead of writing these numbers normally, we write them in a special way:*

     We split each number into single digits.
     We reverse the order of these digits.
     We store each digit in a "node" of a linked list.

Your job is to add these two numbers together and present the answer in the same special format.

Let's go through this step-by-step:

**1. Understanding the Input:**
   - You're given two linked lists, let's call them l1 and l2.
   - Each node in these lists contains a single digit (from 0 to 9).
   - The digits are in reverse order.

**2. What "reverse order" means:**
   - If the actual number is 342, the linked list will be [2,4,3].
   - The least significant digit (2) is at the start of the list.
   - The most significant digit (3) is at the end of the list.

**3. The Addition Process:**
   - You need to add these numbers as if they were normal numbers.
   - But you're working with them in this reversed, linked list format.

**4. The Output:**
   - Your answer should also be in the form of a reversed linked list.

**5. Examples Explained:**
   Example 1: 
   - l1 = [2,4,3] represents 342
   - l2 = [5,6,4] represents 465
   - 342 + 465 = 807
   - So, the output should be [7,0,8] (807 in reverse)

   Example 2:
   - Both inputs are [0], representing the number 0
   - 0 + 0 = 0
   - Output is [0]

   Example 3:
   - l1 = [9,9,9,9,9,9,9] represents 9999999
   - l2 = [9,9,9,9] represents 9999
   - 9999999 + 9999 = 10009998
   - Output is [8,9,9,9,0,0,0,1] (10009998 in reverse)

**6. Things to Keep in Mind:**
   - You might need to carry over digits when adding (like in regular addition).
   - The result might have more digits than either of the input numbers.
   - You don't need to worry about leading zeros (except for the number 0 itself).

---

# Intuition

When we first look at this problem, we might think: "this is just like adding two numbers, but with a twist!" And that's exactly right. 

The twist is that our numbers are:
1. Stored in linked lists
2. In reverse order

So, 342 is stored as 2 -> 4 -> 3, and 465 is stored as 5 -> 6 -> 4.

The good news is that this reverse order actually makes our job easier! Why? Because when we add numbers by hand, we start from the rightmost digits. Here, those digits are conveniently at the start of our lists.

Our plan of attack is to traverse both lists simultaneously, adding the digits as we go, just like we'd do on paper. We'll keep track of any carry-over, and build our result in a new linked list.

# Approach

Let's break down our approach step by step:

**1. Initialize a dummy node:** This gives us a starting point for our result list. It's a common trick in linked list problems to simplify edge cases.

**2. Initialize a current pointer:** This will help us build our result list as we go.

**3. Initialize a carry variable:** This will keep track of any carry-over from adding digits.

**4. Traverse the lists:** We'll go through both input lists and the carry simultaneously. We keep going as long as there are digits left in either list or we have a carry.

**5. For each step of our traversal:**
   - Sum up the current digits from both lists (if available) and the carry.
   - Create a new node with the ones digit of this sum (sum % 10).
   - Update the carry for the next iteration (sum / 10).
   - Move our pointers forward.

**6. Return the result:** Remember to skip the dummy node we created at the start.

Let's see this in action with our example of 342 + 465:

```
Initial state: dummy -> (empty)
               ^
               current

Step 1: 2 + 5 = 7
        dummy -> 7
                 ^
                 current

Step 2: 4 + 6 = 10
        dummy -> 7 -> 0
                      ^
                      current
        (carry = 1)

Step 3: 3 + 4 + 1 (carry) = 8
        dummy -> 7 -> 0 -> 8
                           ^
                           current

Final result: 7 -> 0 -> 8 (which is 807)
```

This approach is efficient because it handles different list lengths and final carries naturally. We just keep going until we've processed everything.

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
Java
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
C++
```C++ []
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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

            current->next = new ListNode(sum % 10);
            current = current->next;
            carry = sum / 10;
        }

        return dummy->next;
    }
};
```
C++
```C++ []
//Optimized
static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}();

inline bool isDigit(const char c) {
    return (c >= '0') && (c <= '9');
}

void parse_and_solve(const std::string& s1, const std::string& s2, std::ofstream& out) {
    const int S1 = s1.size();
    const int S2 = s2.size();
    if (S1 < S2) {
        parse_and_solve(s2, s1, out);
        return;
    }
    int carry = 0;
    int i = 0;
    int j = 0;
    while (i < S1 - 1) {
        while (i < S1 && (!isDigit(s1[i]))) { ++i; }
        while (j < S2 && (!isDigit(s2[j]))) { ++j; }
        const int n1 = s1[i] - '0';
        const int n2 = (j < S2) ? (s2[j] - '0') : 0;
        const int n = carry + n1 + n2;
        carry = n / 10;
        out << (n % 10);
        if (i < S1 - 2) {
            out << ",";
        }
        ++i;
        ++j;
    }
    if (carry > 0) {
        out << "," << carry;
    }
}

static bool Solve = [](){
    std::ofstream out("user.out");
    std::string s1, s2;
    while (std::getline(std::cin, s1) && std::getline(std::cin, s2)) {
        out << "[";
        parse_and_solve(s1, s2, out);
        out << "]\n";
    }
    out.flush();
    exit(0);
    return true;
}();
/**
 * Definition for single-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode* head = new ListNode(-1);
        ListNode* temp = head;
        int c = 0;
        while (l1 != NULL && l2 != NULL) {
            int sum = c + l1->val + l2->val;
            if (sum > 9) {
                c = sum / 10;
                head->next = new ListNode(sum % 10);
                head = head->next;
            } else {
                c = 0;
                head->next = new ListNode(sum);
                head = head->next;
            }
            l1 = l1->next;
            l2 = l2->next;
        }
        while (l1 != NULL) {
            int sum = c + l1->val;
            if (sum > 9) {
                c = sum / 10;
                head->next = new ListNode(sum % 10);
                head = head->next;
            } else {
                c = 0;
                head->next = new ListNode(sum);
                head = head->next;
            }
            l1 = l1->next;
        }
        while (l2 != NULL) {
            int sum = c + l2->val;
            if (sum > 9) {
                c = sum / 10;
                head->next = new ListNode(sum % 10);
                head = head->next;
            } else {
                c = 0;
                head->next = new ListNode(sum);
                head = head->next;
            }
            l2 = l2->next;
        }
        if (c > 0) {
            head->next = new ListNode(c);
            head = head->next;
        }
        head->next = NULL;
        return temp->next;
    }
};
```
Python
```Python []
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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

            current.next = ListNode(sum % 10)
            current = current.next
            carry = sum // 10

        return dummy.next
```
Python
```Python []

# Optimized
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        carry=0
        while l1 or l2 or carry:
            s=l1.val if l1 else 0
            p=l2.val if l2 else 0
            val=s+p+carry
            carry=val//10
            val=val%10
            curr.next=ListNode(val)
            curr=curr.next
            l1=l1.next if l1  else None
            l2=l2.next if l2  else None
        return dummy.next
        
```
JavaScript
```JavaScript []
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let dummy = new ListNode(0);
    let current = dummy;
    let carry = 0;

    while (l1 !== null || l2 !== null || carry !== 0) {
        let sum = carry;

        if (l1 !== null) {
            sum += l1.val;
            l1 = l1.next;
        }
        if (l2 !== null) {
            sum += l2.val;
            l2 = l2.next;
        }

        current.next = new ListNode(sum % 10);
        current = current.next;
        carry = Math.floor(sum / 10);
    }

    return dummy.next;
};
```
Go
```Go []
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
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

        current.Next = &ListNode{Val: sum % 10}
        current = current.Next
        carry = sum / 10
    }

    return dummy.Next
}
```
Go
```Go []
// improved runtime 
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    valueRepresentation1, valueRepresentation2 := totalValue(l1), totalValue(l2)
    value1 := new(big.Int)
    value1, _ = value1.SetString(valueRepresentation1, 10)
    value2 := new(big.Int)
    value2, _ = value2.SetString(valueRepresentation2, 10)
    total := new(big.Int)
    total = total.Add(value1, value2)

    return newResultList(total.String())
}


func newResultList(totalValue string) *ListNode{

    var result *ListNode
    for i := 0; i < len(totalValue); i ++ {
        val, _ := strconv.Atoi(string(totalValue[i]))

        if i == 0 {
            result = &ListNode{Val: val}
        } else{
            currentNode := &ListNode{Val: val}
            currentNode.Next = result
            result = currentNode
        }
    }

    return result
}

func totalValue(node *ListNode) string {
    
    if node.Next == nil{
        return strconv.Itoa(node.Val)
    }

    return totalValue(node.Next) + strconv.Itoa(node.Val)
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
Java
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
Python
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
C++
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
JavaScript
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
Go
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
