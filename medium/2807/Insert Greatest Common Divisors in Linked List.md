```Java []
class Solution {
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode current = head;
        while (current.next != null) {
            int gcdValue = calculateGCD(current.val, current.next.val);
            insertNodeWithValue(current, gcdValue);
            current = current.next.next;
        }

        return head;
    }

    private void insertNodeWithValue(ListNode node, int value) {
        ListNode newNode = new ListNode(value);
        newNode.next = node.next;
        node.next = newNode;
    }

    private int calculateGCD(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}

```
```C++ []
class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if (!head || !head->next) return head;

        ListNode* current = head;
        while (current->next) {
            int gcdValue = calculateGCD(current->val, current->next->val);
            insertNodeWithValue(current, gcdValue);
            current = current->next->next;
        }

        return head;
    }

private:
    void insertNodeWithValue(ListNode* node, int value) {
        ListNode* newNode = new ListNode(value);
        newNode->next = node->next;
        node->next = newNode;
    }

    int calculateGCD(int a, int b) {
        while (b) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
};
static const int __ = []() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();
```
```Python []
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        current = head
        while current.next:
            gcd_value = self.calculate_gcd(current.val, current.next.val)
            self.insert_node_with_value(current, gcd_value)
            current = current.next.next

        return head

    def insert_node_with_value(self, node: ListNode, value: int) -> None:
        new_node = ListNode(value)
        new_node.next = node.next
        node.next = new_node

    def calculate_gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

```
```Go []
func insertGreatestCommonDivisors(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }

    current := head
    for current.Next != nil {
        gcdValue := calculateGCD(current.Val, current.Next.Val)
        insertNodeWithValue(current, gcdValue)
        current = current.Next.Next
    }

    return head
}

func insertNodeWithValue(node *ListNode, value int) {
    newNode := &ListNode{Val: value, Next: node.Next}
    node.Next = newNode
}

func calculateGCD(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}

```
```Rust []
impl Solution {
    pub fn insert_greatest_common_divisors(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() || head.as_ref().unwrap().next.is_none() {
            return head;
        }

        let mut head = head;
        let mut current = &mut head;

        while let Some(node) = current {
            if let Some(next) = &node.next {
                let gcd_value = Self::calculate_gcd(node.val, next.val);
                Self::insert_node_with_value(node, gcd_value);
                current = &mut node.next.as_mut().unwrap().next;
            } else {
                break;
            }
        }

        head
    }

    fn insert_node_with_value(node: &mut Box<ListNode>, value: i32) {
        let new_node = Box::new(ListNode {
            val: value,
            next: node.next.take(),
        });
        node.next = Some(new_node);
    }

    fn calculate_gcd(mut a: i32, mut b: i32) -> i32 {
        while b != 0 {
            let temp = b;
            b = a % b;
            a = temp;
        }
        a
    }
}

```
```JavaSCript []
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var insertGreatestCommonDivisors = function(head) {
    if (!head || !head.next) return head;

    let current = head;
    while (current.next) {
        const gcdValue = calculateGCD(current.val, current.next.val);
        insertNodeWithValue(current, gcdValue);
        current = current.next.next;
    }

    return head;
};

function insertNodeWithValue(node, value) {
    const newNode = new ListNode(value);
    newNode.next = node.next;
    node.next = newNode;
}

function calculateGCD(a, b) {
    while (b) {
        [a, b] = [b, a % b];
    }
    return a;
}

```
