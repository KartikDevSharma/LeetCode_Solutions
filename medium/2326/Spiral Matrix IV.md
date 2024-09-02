```Python []
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, rows: int, columns: int, head: ListNode) -> list[list[int]]:
        matrix = [[-1] * columns for _ in range(rows)]

        topRow, bottomRow = 0, rows - 1
        leftColumn, rightColumn = 0, columns - 1

        while head:
            for col in range(leftColumn, rightColumn + 1):
                if head:
                    matrix[topRow][col] = head.val
                    head = head.next
            topRow += 1

            for row in range(topRow, bottomRow + 1):
                if head:
                    matrix[row][rightColumn] = head.val
                    head = head.next
            rightColumn -= 1

            for col in range(rightColumn, leftColumn - 1, -1):
                if head:
                    matrix[bottomRow][col] = head.val
                    head = head.next
            bottomRow -= 1

            for row in range(bottomRow, topRow - 1, -1):
                if head:
                    matrix[row][leftColumn] = head.val
                    head = head.next
            leftColumn += 1

        return matrix




def format_output(result):
    return '[' + ','.join(str(row).replace(' ', '') for row in result) + ']'

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines) // 3
    results = []

    for i in range(num_test_cases):
        m = int(lines[i*3])
        n = int(lines[i*3 + 1])
        head_values = json.loads(lines[i*3 + 2])
        
        if not head_values:
            head = None
        else:
            head = ListNode(head_values[0])
            current = head
            for value in head_values[1:]:
                current.next = ListNode(value)
                current = current.next
        
        result = Solution().spiralMatrix(m, n, head)
        formatted_result = format_output(result)
        results.append(formatted_result)

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)

#kartikdevsharmaa

```
```c++ []
class Solution {
public:
    vector<vector<int>> spiralMatrix(int rows, int columns, ListNode* head) {
        vector<vector<int>> matrix(rows, vector<int>(columns, -1));

        int topRow = 0, bottomRow = rows - 1;
        int leftColumn = 0, rightColumn = columns - 1;

        while (head) {
            for (int col = leftColumn; col <= rightColumn && head; col++) {
                matrix[topRow][col] = head->val;
                head = head->next;
            }
            topRow++;

            for (int row = topRow; row <= bottomRow && head; row++) {
                matrix[row][rightColumn] = head->val;
                head = head->next;
            }
            rightColumn--;

            for (int col = rightColumn; col >= leftColumn && head; col--) {
                matrix[bottomRow][col] = head->val;
                head = head->next;
            }
            bottomRow--;

            for (int row = bottomRow; row >= topRow && head; row--) {
                matrix[row][leftColumn] = head->val;
                head = head->next;
            }
            leftColumn++;
        }

        return matrix;
    }
};
static const int kds = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();

```
```c# []
public class Solution {
    public int[][] SpiralMatrix(int rows, int columns, ListNode head) {
        int[][] matrix = new int[rows][];
        for (int i = 0; i < rows; i++) {
            matrix[i] = new int[columns];
            Array.Fill(matrix[i], -1);
        }

        int topRow = 0, bottomRow = rows - 1;
        int leftColumn = 0, rightColumn = columns - 1;

        while (head != null) {
            for (int col = leftColumn; col <= rightColumn && head != null; col++) {
                matrix[topRow][col] = head.val;
                head = head.next;
            }
            topRow++;

            for (int row = topRow; row <= bottomRow && head != null; row++) {
                matrix[row][rightColumn] = head.val;
                head = head.next;
            }
            rightColumn--;

            for (int col = rightColumn; col >= leftColumn && head != null; col--) {
                matrix[bottomRow][col] = head.val;
                head = head.next;
            }
            bottomRow--;

            for (int row = bottomRow; row >= topRow && head != null; row--) {
                matrix[row][leftColumn] = head.val;
                head = head.next;
            }
            leftColumn++;
        }

        return matrix;
    }
}

//kartikdevsharmaa

```
```Java []
class Solution {
    public int[][] spiralMatrix(int rows, int columns, ListNode head) {
        int[][] matrix = new int[rows][];
        for (int i = 0; i < rows; i++) {
            matrix[i] = new int [columns];
            Arrays.fill(matrix[i], -1);
        }

        int topRow = 0, bottomRow = rows - 1, leftColumn = 0, rightColumn = columns - 1;
        while (head != null) {
        
            for (int col = leftColumn; col <= rightColumn && head != null; col++) {
                matrix[topRow][col] = head.val;
                head = head.next;
            }
            topRow++;

        
            for (int row = topRow; row <= bottomRow && head != null; row++) {
                matrix[row][rightColumn] = head.val;
                head = head.next;
            }
            rightColumn--;

 
            for (int col = rightColumn; col >= leftColumn && head != null; col--) {
                matrix[bottomRow][col] = head.val;
                head = head.next;
            }
            bottomRow--;

       
            for (int row = bottomRow; row >= topRow && head != null; row--) {
                matrix[row][leftColumn] = head.val;
                head = head.next;
            }
            leftColumn++;
        }

        return matrix;
    }
}

//kartikdevsharmaa

```
```Go []
func spiralMatrix(rows int, columns int, head *ListNode) [][]int {
    matrix := make([][]int, rows)
    for i := range matrix {
        matrix[i] = make([]int, columns)
        for j := range matrix[i] {
            matrix[i][j] = -1
        }
    }

    topRow, bottomRow := 0, rows-1
    leftColumn, rightColumn := 0, columns-1

    for head != nil {
        for col := leftColumn; col <= rightColumn && head != nil; col++ {
            matrix[topRow][col] = head.Val
            head = head.Next
        }
        topRow++

        for row := topRow; row <= bottomRow && head != nil; row++ {
            matrix[row][rightColumn] = head.Val
            head = head.Next
        }
        rightColumn--

        for col := rightColumn; col >= leftColumn && head != nil; col-- {
            matrix[bottomRow][col] = head.Val
            head = head.Next
        }
        bottomRow--

        for row := bottomRow; row >= topRow && head != nil; row-- {
            matrix[row][leftColumn] = head.Val
            head = head.Next
        }
        leftColumn++
    }

    return matrix
}

//kartikdevsharmaa

```

```Kotlin []
class Solution {
    fun spiralMatrix(rows: Int, columns: Int, head: ListNode?): Array<IntArray> {
        val matrix = Array(rows) { IntArray(columns) { -1 } }

        var topRow = 0
        var bottomRow = rows - 1
        var leftColumn = 0
        var rightColumn = columns - 1

        var current = head

        while (current != null) {
            for (col in leftColumn..rightColumn) {
                if (current != null) {
                    matrix[topRow][col] = current.`val`
                    current = current.next
                }
            }
            topRow++

            for (row in topRow..bottomRow) {
                if (current != null) {
                    matrix[row][rightColumn] = current.`val`
                    current = current.next
                }
            }
            rightColumn--

            for (col in rightColumn downTo leftColumn) {
                if (current != null) {
                    matrix[bottomRow][col] = current.`val`
                    current = current.next
                }
            }
            bottomRow--

            for (row in bottomRow downTo topRow) {
                if (current != null) {
                    matrix[row][leftColumn] = current.`val`
                    current = current.next
                }
            }
            leftColumn++
        }

        return matrix
    }
}

//kartikdevsharmaa

```
```TypeScript []
function  spiralMatrix(rows: number, columns: number, head: ListNode | null): number[][] {
        const matrix: number[][] = Array.from({ length: rows }, () => Array(columns).fill(-1));

        let topRow = 0, bottomRow = rows - 1;
        let leftColumn = 0, rightColumn = columns - 1;

        while (head) {
            for (let col = leftColumn; col <= rightColumn && head; col++) {
                matrix[topRow][col] = head.val;
                head = head.next;
            }
            topRow++;

            for (let row = topRow; row <= bottomRow && head; row++) {
                matrix[row][rightColumn] = head.val;
                head = head.next;
            }
            rightColumn--;

            for (let col = rightColumn; col >= leftColumn && head; col--) {
                matrix[bottomRow][col] = head.val;
                head = head.next;
            }
            bottomRow--;

            for (let row = bottomRow; row >= topRow && head; row--) {
                matrix[row][leftColumn] = head.val;
                head = head.next;
            }
            leftColumn++;
        }

        return matrix;
    }



```
```JavaScript []
/**
 * @param {number} m
 * @param {number} n
 * @param {ListNode} head
 * @return {number[][]}
 */
var spiralMatrix = function(m, n, head) {
    const matrix = Array.from({ length: m }, () => Array(n).fill(-1));

    let topRow = 0, bottomRow = m - 1;
    let leftColumn = 0, rightColumn = n - 1;

    while (head) {
        for (let col = leftColumn; col <= rightColumn && head; col++) {
            matrix[topRow][col] = head.val;
            head = head.next;
        }
        topRow++;

        for (let row = topRow; row <= bottomRow && head; row++) {
            matrix[row][rightColumn] = head.val;
            head = head.next;
        }
        rightColumn--;

        for (let col = rightColumn; col >= leftColumn && head; col--) {
            matrix[bottomRow][col] = head.val;
            head = head.next;
        }
        bottomRow--;

        for (let row = bottomRow; row >= topRow && head; row--) {
            matrix[row][leftColumn] = head.val;
            head = head.next;
        }
        leftColumn++;
    }

    return matrix;
};


```
