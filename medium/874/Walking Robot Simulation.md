

# Code
```Java []
class Solution {
    private static final int[] DIRECTION_X = {0, 1, 0, -1};
    private static final int[] DIRECTION_Y = {1, 0, -1, 0};

    public int robotSim(int[] instructions, int[][] barriers) {
        MobileRobot robot = new MobileRobot();
        Set<Long> barrierSet = new HashSet<>();
        for (int[] barrier : barriers) {
            barrierSet.add(encodePosition(barrier[0], barrier[1]));
        }
        for (int instruction : instructions) {
            robot.executeInstruction(instruction, barrierSet);
        }
        return robot.maxDistanceSquared;
    }

    private static long encodePosition(int x, int y) {
        return ((long) x << 32) | (y & 0xFFFFFFFFL);
    }

    private static class MobileRobot {
        private int positionX = 0, positionY = 0, orientation = 0, maxDistanceSquared = 0;

        private void executeInstruction(int instruction, Set<Long> barriers) {
            if (instruction == -2) {
                orientation = (orientation + 3) % 4;
            } else if (instruction == -1) {
                orientation = (orientation + 1) % 4;
            } else {
                moveForward(instruction, barriers);
            }
        }

        private void moveForward(int steps, Set<Long> barriers) {
            for (int i = 0; i < steps; i++) {
                int nextX = positionX + DIRECTION_X[orientation];
                int nextY = positionY + DIRECTION_Y[orientation];
                if (!barriers.contains(encodePosition(nextX, nextY))) {
                    positionX = nextX;
                    positionY = nextY;
                    updateMaxDistance();
                } else {
                    break;
                }
            }
        }

        private void updateMaxDistance() {
            maxDistanceSquared = Math.max(positionX * positionX + positionY * positionY, maxDistanceSquared);
        }
    }
}
```
```cpp []
class Solution {
private:
    static const vector<int> DIRECTION_X;
    static const vector<int> DIRECTION_Y;

    static long long encodePosition(int x, int y) {
        return ((long long)x << 32) | (y & 0xFFFFFFFFLL);
    }

    class MobileRobot {
    private:
        int positionX = 0, positionY = 0, orientation = 0;
    public:
        int maxDistanceSquared = 0;

        void executeInstruction(int instruction, const unordered_set<long long>& barriers) {
            if (instruction == -2) {
                orientation = (orientation + 3) % 4;
            } else if (instruction == -1) {
                orientation = (orientation + 1) % 4;
            } else {
                moveForward(instruction, barriers);
            }
        }

    private:
        void moveForward(int steps, const unordered_set<long long>& barriers) {
            for (int i = 0; i < steps; i++) {
                int nextX = positionX + DIRECTION_X[orientation];
                int nextY = positionY + DIRECTION_Y[orientation];
                if (barriers.find(encodePosition(nextX, nextY)) == barriers.end()) {
                    positionX = nextX;
                    positionY = nextY;
                    updateMaxDistance();
                } else {
                    break;
                }
            }
        }

        void updateMaxDistance() {
            maxDistanceSquared = max(positionX * positionX + positionY * positionY, maxDistanceSquared);
        }
    };

public:
    int robotSim(vector<int>& instructions, vector<vector<int>>& obstacles) {
        MobileRobot robot;
        unordered_set<long long> barrierSet;
        for (const auto& obstacle : obstacles) {
            barrierSet.insert(encodePosition(obstacle[0], obstacle[1]));
        }
        for (int instruction : instructions) {
            robot.executeInstruction(instruction, barrierSet);
        }
        return robot.maxDistanceSquared;
    }
};

const vector<int> Solution::DIRECTION_X = {0, 1, 0, -1};
const vector<int> Solution::DIRECTION_Y = {1, 0, -1, 0};

static const int speedup = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();

//https://leetcode.com/problems/walking-robot-simulation/submissions/1366929417/
```
```Python []
class Solution:
    DIRECTION_X = [0, 1, 0, -1]
    DIRECTION_Y = [1, 0, -1, 0]

    def robotSim(self, instructions: List[int], obstacles: List[List[int]]) -> int:
        robot = self.MobileRobot()
        barrier_set = set((x, y) for x, y in obstacles)
        
        for instruction in instructions:
            robot.execute_instruction(instruction, barrier_set)
        
        return robot.max_distance_squared

    class MobileRobot:
        def __init__(self):
            self.position_x = 0
            self.position_y = 0
            self.orientation = 0
            self.max_distance_squared = 0

        def execute_instruction(self, instruction, barriers):
            if instruction == -2:
                self.orientation = (self.orientation + 3) % 4
            elif instruction == -1:
                self.orientation = (self.orientation + 1) % 4
            else:
                self.move_forward(instruction, barriers)

        def move_forward(self, steps, barriers):
            for _ in range(steps):
                next_x = self.position_x + Solution.DIRECTION_X[self.orientation]
                next_y = self.position_y + Solution.DIRECTION_Y[self.orientation]
                if (next_x, next_y) not in barriers:
                    self.position_x, self.position_y = next_x, next_y
                    self.update_max_distance()
                else:
                    break

        def update_max_distance(self):
            self.max_distance_squared = max(self.position_x**2 + self.position_y**2, self.max_distance_squared)

def main():
    input_data = sys.stdin.read().strip()
    test_cases = input_data.split('\n')
    results = []
    
    for i in range(0, len(test_cases), 2):
        instructions = json.loads(test_cases[i])
        obstacles = json.loads(test_cases[i+1])
        results.append(Solution().robotSim(instructions, obstacles))
    
    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()
    exit(0)
#kartikdevsharmaa


```
```Go []

```
```Rust []
use std::collections::HashSet;
impl Solution {
    const DIRECTION_X: [i32; 4] = [0, 1, 0, -1];
    const DIRECTION_Y: [i32; 4] = [1, 0, -1, 0];

    pub fn robot_sim(instructions: Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {
        let mut robot = MobileRobot::new();
        let barrier_set: HashSet<i64> = obstacles
            .iter()
            .map(|obstacle| Self::encode_position(obstacle[0], obstacle[1]))
            .collect();

        for instruction in instructions {
            robot.execute_instruction(instruction, &barrier_set);
        }

        robot.max_distance_squared
    }

    fn encode_position(x: i32, y: i32) -> i64 {
        ((x as i64) << 32) | (y as i64 & 0xFFFFFFFF)
    }
}

struct MobileRobot {
    position_x: i32,
    position_y: i32,
    orientation: usize,
    max_distance_squared: i32,
}

impl MobileRobot {
    fn new() -> Self {
        MobileRobot {
            position_x: 0,
            position_y: 0,
            orientation: 0,
            max_distance_squared: 0,
        }
    }

    fn execute_instruction(&mut self, instruction: i32, barriers: &HashSet<i64>) {
        match instruction {
            -2 => self.orientation = (self.orientation + 3) % 4,
            -1 => self.orientation = (self.orientation + 1) % 4,
            steps => self.move_forward(steps, barriers),
        }
    }

    fn move_forward(&mut self, steps: i32, barriers: &HashSet<i64>) {
        for _ in 0..steps {
            let next_x = self.position_x + Solution::DIRECTION_X[self.orientation];
            let next_y = self.position_y + Solution::DIRECTION_Y[self.orientation];
            if !barriers.contains(&Solution::encode_position(next_x, next_y)) {
                self.position_x = next_x;
                self.position_y = next_y;
                self.update_max_distance();
            } else {
                break;
            }
        }
    }

    fn update_max_distance(&mut self) {
        self.max_distance_squared = self.max_distance_squared.max(
            self.position_x * self.position_x + self.position_y * self.position_y
        );
    }
}

//https://leetcode.com/problems/walking-robot-simulation/submissions/1366945147/
```
```JavaScript []

```
