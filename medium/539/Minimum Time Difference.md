```Java []

class Solution {
    public int findMinDifference(List<String> timePoints) {
        if (timePoints.size() > 1440) return 0; 

        boolean[] seen = new boolean[1440]; 
        
        for (String time : timePoints) {
            int minutes = convertToMinutes(time);
            if (seen[minutes]) return 0; 
            seen[minutes] = true;
        }
        
        int first = Integer.MAX_VALUE, prev = Integer.MAX_VALUE;
        int minDiff = Integer.MAX_VALUE;
        
        for (int i = 0; i < 1440; i++) {
            if (seen[i]) {
                if (first == Integer.MAX_VALUE) {
                    first = i;
                } else {
                    minDiff = Math.min(minDiff, i - prev);
                }
                prev = i;
            }
        }
        

        minDiff = Math.min(minDiff, 1440 - prev + first);
        
        return minDiff;
    }
    
    private int convertToMinutes(String time) {
        return ((time.charAt(0) - '0') * 10 + (time.charAt(1) - '0')) * 60 
             + (time.charAt(3) - '0') * 10 + (time.charAt(4) - '0');
    }
}
//Kartikdevsharmaa
```


```cpp []
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        if (timePoints.size() > 1440) return 0;
        
        vector<bool> seen(1440, false);
        
        for (const string& time : timePoints) {
            int minutes = convertToMinutes(time);
            if (seen[minutes]) return 0;
            seen[minutes] = true;
        }
        
        int first = INT_MAX, prev = INT_MAX;
        int minDiff = INT_MAX;
        
        for (int i = 0; i < 1440; i++) {
            if (seen[i]) {
                if (first == INT_MAX) {
                    first = i;
                } else {
                    minDiff = min(minDiff, i - prev);
                }
                prev = i;
            }
        }
        
        minDiff = min(minDiff, 1440 - prev + first);
        return minDiff;
    }
    
private:
    int convertToMinutes(const string& time) {
        return ((time[0] - '0') * 10 + (time[1] - '0')) * 60
             + (time[3] - '0') * 10 + (time[4] - '0');
    }
};

```



```python []
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        
        seen = [False] * 1440
        
        for time in timePoints:
            minutes = self.convertToMinutes(time)
            if seen[minutes]:
                return 0
            seen[minutes] = True
        
        first = float('inf')
        prev = float('inf')
        min_diff = float('inf')
        
        for i in range(1440):
            if seen[i]:
                if first == float('inf'):
                    first = i
                else:
                    min_diff = min(min_diff, i - prev)
                prev = i
        
        min_diff = min(min_diff, 1440 - prev + first)
        return min_diff
    
    def convertToMinutes(self, time: str) -> int:
        return int(time[:2]) * 60 + int(time[3:])

```


```go []
func findMinDifference(timePoints []string) int {
    if len(timePoints) > 1440 {
        return 0
    }
    
    seen := make([]bool, 1440)
    
    for _, time := range timePoints {
        minutes := convertToMinutes(time)
        if seen[minutes] {
            return 0
        }
        seen[minutes] = true
    }
    
    first := 1440
    prev := 1440
    minDiff := 1440
    
    for i := 0; i < 1440; i++ {
        if seen[i] {
            if first == 1440 {
                first = i
            } else {
                minDiff = min(minDiff, i - prev)
            }
            prev = i
        }
    }
    
    minDiff = min(minDiff, 1440 - prev + first)
    return minDiff
}

func convertToMinutes(time string) int {
    return ((int(time[0]) - '0') * 10 + int(time[1]) - '0') * 60 +
           (int(time[3]) - '0') * 10 + int(time[4]) - '0'
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

```


```rust []
impl Solution {
    pub fn find_min_difference(time_points: Vec<String>) -> i32 {
        if time_points.len() > 1440 {
            return 0;
        }
        
        let mut seen = vec![false; 1440];
        
        for time in time_points.iter() {
            let minutes = Self::convert_to_minutes(time);
            if seen[minutes] {
                return 0;
            }
            seen[minutes] = true;
        }
        
        let mut first = i32::MAX;
        let mut prev = i32::MAX;
        let mut min_diff = i32::MAX;
        
        for i in 0..1440 {
            if seen[i] {
                if first == i32::MAX {
                    first = i as i32;
                } else {
                    min_diff = min_diff.min(i as i32 - prev);
                }
                prev = i as i32;
            }
        }
        
        min_diff = min_diff.min(1440 - prev + first);
        min_diff
    }
    
    fn convert_to_minutes(time: &str) -> usize {
        let hours = time[0..2].parse::<usize>().unwrap();
        let minutes = time[3..5].parse::<usize>().unwrap();
        hours * 60 + minutes
    }
}

```



```javascript []
/**
 * @param {string[]} timePoints
 * @return {number}
 */
var findMinDifference = function(timePoints) {
    if (timePoints.length > 1440) return 0;
    
    const seen = new Array(1440).fill(false);
    
    for (const time of timePoints) {
        const minutes = convertToMinutes(time);
        if (seen[minutes]) return 0;
        seen[minutes] = true;
    }
    
    let first = Infinity;
    let prev = Infinity;
    let minDiff = Infinity;
    
    for (let i = 0; i < 1440; i++) {
        if (seen[i]) {
            if (first === Infinity) {
                first = i;
            } else {
                minDiff = Math.min(minDiff, i - prev);
            }
            prev = i;
        }
    }
    
    minDiff = Math.min(minDiff, 1440 - prev + first);
    return minDiff;
};

function convertToMinutes(time) {
    return parseInt(time.slice(0, 2)) * 60 + parseInt(time.slice(3));
}

```

