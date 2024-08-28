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
