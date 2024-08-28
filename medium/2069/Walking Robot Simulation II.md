### Intuition
The problem presents us with a grid-based world where a robot must move and turn according to specific rules. Simply put, this is a problem of spatial reasoning and pattern recognition.

To begin, we need to understand what the question is really asking. We're dealing with a rectangular grid where the robot starts in the bottom-left corner, facing east. The robot can move forward and turn left when it hits a boundary. Our task is to track its position and orientation after a series of movements.

The constraints given are improtant. The grid size is limited (2 <= width, height <= 100), which means we're not dealing with an infinitely large space. The number of steps per move can be quite large (up to 10^5), and we might have to handle up to 10^4 calls to our methods. These constraints hint that a naive simulation approach might not be efficient enough.

As we start to think about solutions, a few key observations come to mind:

>1. The robot's movement forms a predictable pattern around the perimeter of the grid.
>2. After a certain number of steps, the robot's position and direction will repeat.
>3. The total perimeter of the grid is a crucial value in understanding the robot's behavior.

Initially, we might consider a straightforward simulation approach. We could maintain the robot's current position and direction, updating them step-by-step as we process each movement instruction. This would work, but it would be inefficient for large numbers of steps. We'd essentially be recreating the entire path of the robot, even when we only care about its final position.

But we don't need to simulate every single step. Instead, we can think about the robot's movement in terms of cycles around the perimeter of the grid.

Picture the robot's path: it moves east along the bottom edge, then north up the right edge, west across the top edge, and finally south down the left edge before starting over. This forms a rectangle that exactly matches the perimeter of our grid.

Now, let's consider what happens when we ask the robot to take a large number of steps. It might complete several full cycles around the grid, plus some partial distance into the next cycle. This observation is important because it means we can break down any number of steps into:
>1. Complete cycles around the perimeter
>2. Remaining steps into the next incomplete cycle

This insight allows us to make a significant optimization. Instead of simulating every step, we can use modular arithmetic to immediately calculate the robot's position after any number of steps.

Let's define the perimeter of the grid as P = 2 * (width + height - 2). This represents one complete cycle of the robot's movement. For any given number of steps S, we can calculate:
- Complete cycles: S / P (integer division)
- Remaining steps: S % P

The complete cycles don't affect the robot's final position (it ends up where it started), so we can ignore them. We only need to consider the remaining steps to determine the robot's final location and orientation.

This realization transforms our problem from a step-by-step simulation into a mathematical calculation. We're no longer tracking the robot's movement, but instead computing its final state directly.

Now, let's think about how we can determine the robot's position and direction based on these remaining steps. We can divide the perimeter into four segments, corresponding to each edge of the grid:
>1. Bottom edge (moving east): 0 to width - 1 steps
>2. Right edge (moving north): width to width + height - 2 steps
>3. Top edge (moving west): width + height - 1 to 2 * width + height - 3 steps
>4. Left edge (moving south): 2 * width + height - 2 to P - 1 steps

By comparing our remaining steps to these ranges, we can immediately determine which edge the robot is on and calculate its exact position.

This approach solves our efficiency problem. No matter how many steps the robot takes, we can compute its final state in constant time. We've transformed a potentially O(n) operation (where n is the number of steps) into an O(1) operation.

We need to consider some edge cases:
1. What if the robot completes exactly one full cycle?
2. How do we handle the initial state when no steps have been taken?

These edge cases require careful handling in our implementation. For instance, if the robot completes exactly one full cycle, it will be at (0, 0) facing south, not east as it was initially.

If you think, you might realize that we can further simplify our logic by treating the initial state (0 steps) as a special case. This allows us to handle all other cases, including complete cycles, with the same logic.
In terms of implementation, we realize that we only need to store the total number of steps taken. Everything else can be calculated on demand. This leads to a very memory-efficient solution, using only a few variables regardless of the grid size or number of steps taken.



```Java []
class Robot {
    private final int width, height;
    private long steps;
    private static final String[] DIRECTIONS = {"East", "North", "West", "South"};

    public Robot(int width, int height) {
        this.width = width;
        this.height = height;
        this.steps = 0;
    }

    public void step(int num) {
        steps += num;
    }

    public int[] getPos() {
        int perimeter = 2 * (width + height - 2);
        long effectiveSteps = steps % perimeter;
        
        if (effectiveSteps == 0 && steps != 0) {
            return new int[]{0, 0};
        }
        
        if (effectiveSteps < width) return new int[]{(int)effectiveSteps, 0};
        effectiveSteps -= width - 1;
        if (effectiveSteps < height) return new int[]{width - 1, (int)effectiveSteps};
        effectiveSteps -= height - 1;
        if (effectiveSteps < width) return new int[]{width - 1 - (int)effectiveSteps, height - 1};
        effectiveSteps -= width - 1;
        return new int[]{0, height - 1 - (int)effectiveSteps};
    }

    public String getDir() {
        if (steps == 0) return "East";
        int perimeter = 2 * (width + height - 2);
        long effectiveSteps = steps % perimeter;
        if (effectiveSteps == 0) return "South";
        if (effectiveSteps < width) return "East";
        if (effectiveSteps < width + height - 1) return "North";
        if (effectiveSteps < 2 * width + height - 2) return "West";
        return "South";
    }
}

```
```C++ []
class Robot {
private:
    int width, height;
    long long steps;
    const std::vector<std::string> DIRECTIONS = {"East", "North", "West", "South"};

public:
    Robot(int width, int height) : width(width), height(height), steps(0) {}
    
    void step(int num) {
        steps += num;
    }
    
    std::vector<int> getPos() {
        int perimeter = 2 * (width + height - 2);
        long long effectiveSteps = steps % perimeter;
        
        if (effectiveSteps == 0 && steps != 0) {
            return {0, 0};
        }
        
        if (effectiveSteps < width) return {(int)effectiveSteps, 0};
        effectiveSteps -= width - 1;
        if (effectiveSteps < height) return {width - 1, (int)effectiveSteps};
        effectiveSteps -= height - 1;
        if (effectiveSteps < width) return {width - 1 - (int)effectiveSteps, height - 1};
        effectiveSteps -= width - 1;
        return {0, height - 1 - (int)effectiveSteps};
    }
    
    std::string getDir() {
        if (steps == 0) return "East";
        int perimeter = 2 * (width + height - 2);
        long long effectiveSteps = steps % perimeter;
        if (effectiveSteps == 0) return "South";
        if (effectiveSteps < width) return "East";
        if (effectiveSteps < width + height - 1) return "North";
        if (effectiveSteps < 2 * width + height - 2) return "West";
        return "South";
    }
};

static const auto speedup = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();
```
```Python []
class Robot:
    DIRECTIONS = ["East", "North", "West", "South"]

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.steps = 0

    def step(self, num: int) -> None:
        self.steps += num

    def getPos(self) -> List[int]:
        perimeter = 2 * (self.width + self.height - 2)
        effective_steps = self.steps % perimeter
        
        if effective_steps == 0 and self.steps != 0:
            return [0, 0]
        
        if effective_steps < self.width:
            return [effective_steps, 0]
        effective_steps -= self.width - 1
        if effective_steps < self.height:
            return [self.width - 1, effective_steps]
        effective_steps -= self.height - 1
        if effective_steps < self.width:
            return [self.width - 1 - effective_steps, self.height - 1]
        effective_steps -= self.width - 1
        return [0, self.height - 1 - effective_steps]

    def getDir(self) -> str:
        if self.steps == 0:
            return "East"
        perimeter = 2 * (self.width + self.height - 2)
        effective_steps = self.steps % perimeter
        if effective_steps == 0:
            return "South"
        if effective_steps < self.width:
            return "East"
        if effective_steps < self.width + self.height - 1:
            return "North"
        if effective_steps < 2 * self.width + self.height - 2:
            return "West"
        return "South"
```
```Go []
type Robot struct {
    width, height int
    steps         int64
    directions    []string
}

func Constructor(width int, height int) Robot {
    return Robot{
        width:      width,
        height:     height,
        steps:      0,
        directions: []string{"East", "North", "West", "South"},
    }
}

func (this *Robot) Step(num int) {
    this.steps += int64(num)
}

func (this *Robot) GetPos() []int {
    perimeter := 2 * (this.width + this.height - 2)
    effectiveSteps := this.steps % int64(perimeter)

    if effectiveSteps == 0 && this.steps != 0 {
        return []int{0, 0}
    }

    if effectiveSteps < int64(this.width) {
        return []int{int(effectiveSteps), 0}
    }
    effectiveSteps -= int64(this.width - 1)
    if effectiveSteps < int64(this.height) {
        return []int{this.width - 1, int(effectiveSteps)}
    }
    effectiveSteps -= int64(this.height - 1)
    if effectiveSteps < int64(this.width) {
        return []int{this.width - 1 - int(effectiveSteps), this.height - 1}
    }
    effectiveSteps -= int64(this.width - 1)
    return []int{0, this.height - 1 - int(effectiveSteps)}
}

func (this *Robot) GetDir() string {
    if this.steps == 0 {
        return "East"
    }
    perimeter := 2 * (this.width + this.height - 2)
    effectiveSteps := this.steps % int64(perimeter)
    if effectiveSteps == 0 {
        return "South"
    }
    if effectiveSteps < int64(this.width) {
        return "East"
    }
    if effectiveSteps < int64(this.width+this.height-1) {
        return "North"
    }
    if effectiveSteps < int64(2*this.width+this.height-2) {
        return "West"
    }
    return "South"
}
```
```Rust []
struct Robot {
    width: i32,
    height: i32,
    steps: i64,
    directions: Vec<String>,
}

impl Robot {
    fn new(width: i32, height: i32) -> Self {
        Robot {
            width,
            height,
            steps: 0,
            directions: vec!["East".to_string(), "North".to_string(), "West".to_string(), "South".to_string()],
        }
    }
    
    fn step(&mut self, num: i32) {
        self.steps += num as i64;
    }
    
    fn get_pos(&self) -> Vec<i32> {
        let perimeter = 2 * (self.width + self.height - 2);
        let mut effective_steps = self.steps % (perimeter as i64);
        
        if effective_steps == 0 && self.steps != 0 {
            return vec![0, 0];
        }
        
        if effective_steps < self.width as i64 {
            return vec![effective_steps as i32, 0];
        }
        effective_steps -= (self.width - 1) as i64;
        if effective_steps < self.height as i64 {
            return vec![self.width - 1, effective_steps as i32];
        }
        effective_steps -= (self.height - 1) as i64;
        if effective_steps < self.width as i64 {
            return vec![self.width - 1 - effective_steps as i32, self.height - 1];
        }
        effective_steps -= (self.width - 1) as i64;
        vec![0, self.height - 1 - effective_steps as i32]
    }
    
    fn get_dir(&self) -> String {
        if self.steps == 0 {
            return "East".to_string();
        }
        let perimeter = 2 * (self.width + self.height - 2);
        let effective_steps = self.steps % (perimeter as i64);
        if effective_steps == 0 {
            return "South".to_string();
        }
        if effective_steps < self.width as i64 {
            return "East".to_string();
        }
        if effective_steps < (self.width + self.height - 1) as i64 {
            return "North".to_string();
        }
        if effective_steps < (2 * self.width + self.height - 2) as i64 {
            return "West".to_string();
        }
        "South".to_string()
    }
}
```
```JavaScript []
/**
 * @param {number} width
 * @param {number} height
 */
var Robot = function(width, height) {
    this.width = width;
    this.height = height;
    this.steps = 0n;
    this.DIRECTIONS = ["East", "North", "West", "South"];
};

/** 
 * @param {number} num
 * @return {void}
 */
Robot.prototype.step = function(num) {
    this.steps += BigInt(num);
};

/**
 * @return {number[]}
 */
Robot.prototype.getPos = function() {
    const perimeter = 2n * BigInt(this.width + this.height - 2);
    let effectiveSteps = this.steps % perimeter;
    
    if (effectiveSteps === 0n && this.steps !== 0n) {
        return [0, 0];
    }
    
    if (effectiveSteps < BigInt(this.width)) {
        return [Number(effectiveSteps), 0];
    }
    effectiveSteps -= BigInt(this.width - 1);
    if (effectiveSteps < BigInt(this.height)) {
        return [this.width - 1, Number(effectiveSteps)];
    }
    effectiveSteps -= BigInt(this.height - 1);
    if (effectiveSteps < BigInt(this.width)) {
        return [this.width - 1 - Number(effectiveSteps), this.height - 1];
    }
    effectiveSteps -= BigInt(this.width - 1);
    return [0, this.height - 1 - Number(effectiveSteps)];
};

/**
 * @return {string}
 */
Robot.prototype.getDir = function() {
    if (this.steps === 0n) return "East";
    const perimeter = 2n * BigInt(this.width + this.height - 2);
    const effectiveSteps = this.steps % perimeter;
    if (effectiveSteps === 0n) return "South";
    if (effectiveSteps < BigInt(this.width)) return "East";
    if (effectiveSteps < BigInt(this.width + this.height - 1)) return "North";
    if (effectiveSteps < BigInt(2 * this.width + this.height - 2)) return "West";
    return "South";
};
```
