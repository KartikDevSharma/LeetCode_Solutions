

### Intuition

When I first looked at this problem, a few things jumped out at me:

1. We're dealing with multiple sorted arrays. That's always interesting because sorted arrays have some special properties we can take advantage of.

2. We need to find the maximum distance between any two numbers from different arrays. This screams "find the extremes" to me.

3. The fact that we're looking for the absolute difference means we're essentially trying to find the biggest gap between the smallest and largest numbers across all these arrays.

4. Since each array is sorted, we know the smallest number in each array is at the beginning, and the largest is at the end. That's a huge help!

5. The challenge here is that we can't just find the overall minimum and maximum across all arrays because they need to come from different arrays.

So, my initial thought was: "We need to keep track of the smallest and largest numbers we've seen, but in a way that lets us compare them with numbers from other arrays."

### Approach

Let's break down the approach step by step

1. First off, we need to handle some edge cases. If we have null input or less than two arrays, we can't find a distance between two arrays, so we return 0.

2. We start by looking at the first array. We'll use this as our initial reference point.
   - We set the global minimum to the first element of the first array.
   - We set the global maximum to the last element of the first array.
   - Why? Because these are our current extremes, and we'll compare everything else to these.

3. We initialize our result to 0. This will keep track of the maximum distance we've found so far.

4. Now, here's where it gets interesting. We loop through all the remaining arrays, starting from the second one (index 1).

5. For each array, we do the following:
   - Find the local minimum (first element of the current array)
   - Find the local maximum (last element of the current array)
   
   Now, why do we care about these local min and max? Because they give us two opportunities to update our maximum distance:

    - a) We can calculate the distance between the current array's maximum and the global minimum we've seen so far.
    - b) We can calculate the distance between the global maximum we've seen so far and the current array's minimum.

   The larger of these two distances is a candidate for our new maximum distance.

6. After calculating these distances, we update our result if we've found a new maximum distance.

7. Before moving to the next array, we update our global minimum and maximum.
   - If the current array's minimum is smaller than our global minimum, it becomes the new global minimum.
   - If the current array's maximum is larger than our global maximum, it becomes the new global maximum.

8. We repeat steps 5-7 for all remaining arrays.

9. Once we've gone through all arrays, our result variable will hold the maximum distance we found.

Now, let's look at why this approach works:

- By always comparing the current array's extremes with the global extremes we've seen so far, we ensure we're always considering the maximum possible distance that includes the current array.
- Updating the global min and max after each array ensures that for the next array, we're comparing against the most extreme values we've seen so far.
- This approach cleverly avoids the need to compare every number in every array with every number in every other array, which would be much slower.

Let's walk through this with an example:

Suppose we have these arrays: [[1,4,7], [2,5,8], [3,6,9]]

1. We start with the first array [1,4,7].
   Global min = 1, Global max = 7, Result = 0

2. We move to [2,5,8].
   - Local min = 2, Local max = 8
   - We calculate:
     8 - 1 = 7 (local max - global min)
     7 - 2 = 5 (global max - local min)
   - The larger of these is 7, so Result = 7
   - We update: Global min = 1 (unchanged), Global max = 8

3. We move to [3,6,9].
   - Local min = 3, Local max = 9
   - We calculate:
     9 - 1 = 8 (local max - global min)
     8 - 3 = 5 (global max - local min)
   - The larger of these is 8, so Result = 8
   

4. We've gone through all arrays, so we return 8 as our result.



### Complexity


**Time Complexity: O(n)**

Here's why:
- We iterate through each array exactly once.
- For each array, we perform a constant number of operations (getting the first and last elements, doing some comparisons and math).
- If we have m arrays and the total number of elements across all arrays is n, our time complexity is O(m).
- However, we're told that m <= 10^5 and the total number of elements across all arrays is also at most 10^5.
- This means m is linear with respect to n in the worst case.
- Therefore, our time complexity simplifies to O(n).

This linear time complexity is fantastic because it means our solution scales well even with large inputs. Whether we have 100 or 100,000 elements in total, our algorithm will handle it efficiently.

**Space Complexity: O(1)**

Here's why:
- We only use a fixed number of variables (globalMin, globalMax, result) regardless of the input size.
- We don't create any data structures that grow with the input.
- All our operations are done in-place on the input data.

This constant space complexity is ideal because it means our solution uses the same amount of extra memory regardless of whether we're dealing with 10 or 10,000,000 elements.



---
### Code

```Java []
class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        if (arrays == null || arrays.size() < 2) return 0;

        int globalMin = arrays.get(0).get(0);
        int globalMax = arrays.get(0).get(arrays.get(0).size() - 1);
        int result = 0;

        for (int i = 1; i < arrays.size(); i++) {
            List<Integer> curr = arrays.get(i);
            int localMin = curr.get(0);
            int localMax = curr.get(curr.size() - 1);

            result = Math.max(result, Math.max(localMax - globalMin, globalMax - localMin));

            globalMin = Math.min(globalMin, localMin);
            globalMax = Math.max(globalMax, localMax);
        }

        return result;
    }
}
```

```C++ []
class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        cout.tie(nullptr);

        if (arrays.size() < 2) return 0;

        int globalMin = arrays[0][0];
        int globalMax = arrays[0].back();
        int result = 0;

        for (int i = 1; i < arrays.size(); ++i) {
            result = max({result, 
                          abs(arrays[i].back() - globalMin),
                          abs(globalMax - arrays[i][0])});
            
            globalMin = min(globalMin, arrays[i][0]);
            globalMax = max(globalMax, arrays[i].back());
        }

        return result;
    }
};
```

```Python []
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if len(arrays) < 2:
            return 0

        global_min, global_max = arrays[0][0], arrays[0][-1]
        result = 0

        for arr in arrays[1:]:
            local_min, local_max = arr[0], arr[-1]
            result = max(result, max(local_max - global_min, global_max - local_min))
            global_min = min(global_min, local_min)
            global_max = max(global_max, local_max)

        return result
```

```Go []
func maxDistance(arrays [][]int) int {
    if len(arrays) < 2 {
        return 0
    }

    globalMin, globalMax := arrays[0][0], arrays[0][len(arrays[0])-1]
    result := 0

    for _, arr := range arrays[1:] {
        localMin, localMax := arr[0], arr[len(arr)-1]
        result = max(result, max(localMax-globalMin, globalMax-localMin))
        globalMin = min(globalMin, localMin)
        globalMax = max(globalMax, localMax)
    }

    return result
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```

```Rust []
impl Solution {
    pub fn max_distance(arrays: Vec<Vec<i32>>) -> i32 {
        if arrays.len() < 2 {
            return 0;
        }

        let mut global_min = arrays[0][0];
        let mut global_max = *arrays[0].last().unwrap();
        let mut result = 0;

        for arr in arrays.iter().skip(1) {
            let local_min = arr[0];
            let local_max = *arr.last().unwrap();

            result = result.max((local_max - global_min).abs().max((global_max - local_min).abs()));

            global_min = global_min.min(local_min);
            global_max = global_max.max(local_max);
        }

        result
    }
}
```
```JavaScript []
/**
 * @param {number[][]} arrays
 * @return {number}
 */
var maxDistance = function(arrays) {
    if (arrays.length < 2) return 0;

    let globalMin = arrays[0][0];
    let globalMax = arrays[0][arrays[0].length - 1];
    let result = 0;

    for (let i = 1; i < arrays.length; i++) {
        const localMin = arrays[i][0];
        const localMax = arrays[i][arrays[i].length - 1];

        result = Math.max(result, Math.max(localMax - globalMin, globalMax - localMin));

        globalMin = Math.min(globalMin, localMin);
        globalMax = Math.max(globalMax, localMax);
    }

    return result;
};
```
