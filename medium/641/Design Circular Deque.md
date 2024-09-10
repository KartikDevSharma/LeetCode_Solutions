```Java []
class MyCircularDeque {
    private int[] deque;
    private int front, size;
    private final int capacity;

    public MyCircularDeque(int k) {
        deque = new int[k];
        front = 0;
        size = 0;
        capacity = k;
    }

    public boolean insertFront(int value) {
        if (isFull()) return false;
        front = (front - 1 + capacity) % capacity;
        deque[front] = value;
        size++;
        return true;
    }

    public boolean insertLast(int value) {
        if (isFull()) return false;
        int rear = (front + size) % capacity;
        deque[rear] = value;
        size++;
        return true;
    }

    public boolean deleteFront() {
        if (isEmpty()) return false;
        front = (front + 1) % capacity;
        size--;
        return true;
    }

    public boolean deleteLast() {
        if (isEmpty()) return false;
        size--;
        return true;
    }

    public int getFront() {
        if (isEmpty()) return -1;
        return deque[front];
    }

    public int getRear() {
        if (isEmpty()) return -1;
        return deque[(front + size - 1) % capacity];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == capacity;
    }
}
//KDS
```
```C++ []
class MyCircularDeque {
private:
    std::vector<int> deque;
    int front, size, capacity;

public:
    MyCircularDeque(int k) : deque(k), front(0), size(0), capacity(k) {}
    
    bool insertFront(int value) {
        if (isFull()) return false;
        front = (front - 1 + capacity) % capacity;
        deque[front] = value;
        size++;
        return true;
    }
    
    bool insertLast(int value) {
        if (isFull()) return false;
        int rear = (front + size) % capacity;
        deque[rear] = value;
        size++;
        return true;
    }
    
    bool deleteFront() {
        if (isEmpty()) return false;
        front = (front + 1) % capacity;
        size--;
        return true;
    }
    
    bool deleteLast() {
        if (isEmpty()) return false;
        size--;
        return true;
    }
    
    int getFront() {
        if (isEmpty()) return -1;
        return deque[front];
    }
    
    int getRear() {
        if (isEmpty()) return -1;
        return deque[(front + size - 1) % capacity];
    }
    
    bool isEmpty() {
        return size == 0;
    }
    
    bool isFull() {
        return size == capacity;
    }
};
static const auto kds = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();
//kartikdevsharmaa
```
```Python []
class MyCircularDeque:
    def __init__(self, k: int):
        self.deque = [0] * k
        self.front = 0
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        rear = (self.front + self.size) % self.capacity
        self.deque[rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.front + self.size - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

#kartikdevsharmaa
```
```Go []
type MyCircularDeque struct {
    deque    []int
    front    int
    size     int
    capacity int
}

func Constructor(k int) MyCircularDeque {
    return MyCircularDeque{
        deque:    make([]int, k),
        front:    0,
        size:     0,
        capacity: k,
    }
}

func (this *MyCircularDeque) InsertFront(value int) bool {
    if this.IsFull() {
        return false
    }
    this.front = (this.front - 1 + this.capacity) % this.capacity
    this.deque[this.front] = value
    this.size++
    return true
}

func (this *MyCircularDeque) InsertLast(value int) bool {
    if this.IsFull() {
        return false
    }
    rear := (this.front + this.size) % this.capacity
    this.deque[rear] = value
    this.size++
    return true
}

func (this *MyCircularDeque) DeleteFront() bool {
    if this.IsEmpty() {
        return false
    }
    this.front = (this.front + 1) % this.capacity
    this.size--
    return true
}

func (this *MyCircularDeque) DeleteLast() bool {
    if this.IsEmpty() {
        return false
    }
    this.size--
    return true
}

func (this *MyCircularDeque) GetFront() int {
    if this.IsEmpty() {
        return -1
    }
    return this.deque[this.front]
}

func (this *MyCircularDeque) GetRear() int {
    if this.IsEmpty() {
        return -1
    }
    return this.deque[(this.front+this.size-1)%this.capacity]
}

func (this *MyCircularDeque) IsEmpty() bool {
    return this.size == 0
}

func (this *MyCircularDeque) IsFull() bool {
    return this.size == this.capacity
}

//kartikdevsharmaa
```
```Rust []
struct MyCircularDeque {
    deque: Vec<i32>,
    front: usize,
    size: usize,
    capacity: usize,
}

impl MyCircularDeque {
    fn new(k: i32) -> Self {
        MyCircularDeque {
            deque: vec![0; k as usize],
            front: 0,
            size: 0,
            capacity: k as usize,
        }
    }
    
    fn insert_front(&mut self, value: i32) -> bool {
        if self.is_full() {
            return false;
        }
        self.front = (self.front + self.capacity - 1) % self.capacity;
        self.deque[self.front] = value;
        self.size += 1;
        true
    }
    
    fn insert_last(&mut self, value: i32) -> bool {
        if self.is_full() {
            return false;
        }
        let rear = (self.front + self.size) % self.capacity;
        self.deque[rear] = value;
        self.size += 1;
        true
    }
    
    fn delete_front(&mut self) -> bool {
        if self.is_empty() {
            return false;
        }
        self.front = (self.front + 1) % self.capacity;
        self.size -= 1;
        true
    }
    
    fn delete_last(&mut self) -> bool {
        if self.is_empty() {
            return false;
        }
        self.size -= 1;
        true
    }
    
    fn get_front(&self) -> i32 {
        if self.is_empty() {
            return -1;
        }
        self.deque[self.front]
    }
    
    fn get_rear(&self) -> i32 {
        if self.is_empty() {
            return -1;
        }
        self.deque[(self.front + self.size - 1) % self.capacity]
    }
    
    fn is_empty(&self) -> bool {
        self.size == 0
    }
    
    fn is_full(&self) -> bool {
        self.size == self.capacity
    }
}

//kartikdevsharmaa
```
```JavaScript []
class MyCircularDeque {
    constructor(k) {
        this.deque = new Array(k);
        this.front = 0;
        this.size = 0;
        this.capacity = k;
    }

    insertFront(value) {
        if (this.isFull()) return false;
        this.front = (this.front - 1 + this.capacity) % this.capacity;
        this.deque[this.front] = value;
        this.size++;
        return true;
    }

    insertLast(value) {
        if (this.isFull()) return false;
        const rear = (this.front + this.size) % this.capacity;
        this.deque[rear] = value;
        this.size++;
        return true;
    }

    deleteFront() {
        if (this.isEmpty()) return false;
        this.front = (this.front + 1) % this.capacity;
        this.size--;
        return true;
    }

    deleteLast() {
        if (this.isEmpty()) return false;
        this.size--;
        return true;
    }

    getFront() {
        if (this.isEmpty()) return -1;
        return this.deque[this.front];
    }

    getRear() {
        if (this.isEmpty()) return -1;
        return this.deque[(this.front + this.size - 1) % this.capacity];
    }

    isEmpty() {
        return this.size === 0;
    }

    isFull() {
        return this.size === this.capacity;
    }
}

//kartikdevsharmaa
```
