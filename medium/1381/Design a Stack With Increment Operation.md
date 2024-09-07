```Java []
class CustomStack {
    private int[] stack;    
    private int[] add;     
    private int index;    

    public CustomStack(int maxSize) {
        stack = new int[maxSize];  
        add = new int[maxSize];    
        index = 0;                 
    }


    public void push(int x) {
        if (index < stack.length) {
            stack[index++] = x;    
        }
    }

    
    public int pop() {
        if (index == 0) {
            return -1;             
        }
        index--;                   
        int result = stack[index] + add[index];  
        
        if (index > 0) {           
            add[index - 1] += add[index]; 
        }
        
        add[index] = 0;           
        return result;         
    }

    public void increment(int k, int val) {
        if (index > 0) {
            int incIndex = Math.min(k, index) - 1;  
            add[incIndex] += val; 
        }
    }
}
//kartikdevsharmaa
```
```C++ []

class CustomStack {
    vector<int> stack;
    vector<int> add;
    int index;
    int maxSize;

public:
    CustomStack(int maxSize) : maxSize(maxSize), index(0) {
        stack.resize(maxSize);
        add.resize(maxSize, 0);
    }

    void push(int x) {
        if (index < maxSize) {
            stack[index] = x;
            index++;
        }
    }

    int pop() {
        if (index == 0) {
            return -1;
        }
        index--;
        int result = stack[index] + add[index];
        if (index > 0) {
            add[index - 1] += add[index];
        }
        add[index] = 0;
        return result;
    }

    void increment(int k, int val) {
        if (index > 0) {
            int incIndex = min(k, index) - 1;
            add[incIndex] += val;
        }
    }
};

static const int kds = []{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();


//Kartikdevsharmaa
```
```Python []
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.add = [0] * maxSize
        self.index = 0

    def push(self, x: int) -> None:
        if self.index < len(self.stack):
            self.stack[self.index] = x
            self.index += 1

    def pop(self) -> int:
        if self.index == 0:
            return -1
        self.index -= 1
        result = self.stack[self.index] + self.add[self.index]
        if self.index > 0:
            self.add[self.index - 1] += self.add[self.index]
        self.add[self.index] = 0
        return result

    def increment(self, k: int, val: int) -> None:
        if self.index > 0:
            incIndex = min(k, self.index) - 1
            self.add[incIndex] += val

#kartikdevsharmaa
```
