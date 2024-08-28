```Java []
class Solution {
    public int numComponents(ListNode head, int[] nums) {
        boolean[] db = new boolean[10001];
        for (int num : nums) {
            db[num] = true;
        }
        
        int components = 0;
        while (head != null) {
            if (db[head.val] && (head.next == null || !db[head.next.val])) {
                components++;
            }
            head = head.next;
        }
        
        return components;
    }
}

```

```C++ []
class Solution {
public:
    int numComponents(ListNode* head, vector<int>& nums) {
       
        bool db[10001] = {false};
        for (int num : nums) {
            db[num] = true;
        }

        int components = 0;
        while (head != nullptr) {
            if (db[head->val] && (head->next == nullptr || !db[head->next->val])) {
                components++;
            }
            head = head->next;
        }

        return components;
    }
};
static const auto speedup = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();

//https://leetcode.com/problems/linked-list-components/submissions/1371051801/

```
```Python []
class Solution:
    def numComponents(self, head: ListNode, nums: list[int]) -> int:
        db = [False] * 10001
        for num in nums:
            db[num] = True

        components = 0
        while head:
            if db[head.val] and (head.next is None or not db[head.next.val]):
                components += 1
            head = head.next

        return components

def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def main():
    input_data = sys.stdin.read().strip().splitlines()
    results = []

    for i in range(0, len(input_data), 2):
        head_list = json.loads(input_data[i])
        nums = json.loads(input_data[i + 1])
        
        if isinstance(head_list, list) and isinstance(nums, list):
            head = create_linked_list(head_list)
            result = Solution().numComponents(head, nums)
            results.append(result)
        else:
            print(f"Invalid data format for test case starting at line {i + 1}")

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()
    exit(0)

#https://leetcode.com/problems/linked-list-components/submissions/1371055468/
```
