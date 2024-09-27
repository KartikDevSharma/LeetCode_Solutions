### Appraoch 1


```Java []
class Solution {
    public int[] arrayRankTransform(int[] arr) {
        if (arr == null || arr.length == 0) {
            return new int[0];
        }

        // Find min and max values
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int num : arr) {
            min = Math.min(min, num);
            max = Math.max(max, num);
        }

        // Create a count array
        int range = max - min + 1;
        if (range > 2_000_000) {
            // Fall back to sorting method if range is too large
            return sortingMethod(arr);
        }

        boolean[] count = new boolean[range];
        for (int num : arr) {
            count[num - min] = true;
        }

        // Calculate ranks
        int[] ranks = new int[range];
        int rank = 1;
        for (int i = 0; i < range; i++) {
            if (count[i]) {
                ranks[i] = rank++;
            }
        }

        // Assign ranks to original array
        for (int i = 0; i < arr.length; i++) {
            arr[i] = ranks[arr[i] - min];
        }

        return arr;
    }

    private int[] sortingMethod(int[] arr) {
        int[] sortedArr = Arrays.copyOf(arr, arr.length);
        Arrays.sort(sortedArr);
        
        Map<Integer, Integer> rankMap = new HashMap<>();
        int rank = 1;
        for (int num : sortedArr) {
            if (!rankMap.containsKey(num)) {
                rankMap.put(num, rank++);
            }
        }
        
        int[] result = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            result[i] = rankMap.get(arr[i]);
        }
        
        return result;
    }
}
```

```C++ []
class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        if (arr.empty()) return {};

        // Find min and max values
        auto [min_it, max_it] = minmax_element(arr.begin(), arr.end());
        int min_val = *min_it;
        int max_val = *max_it;

        // Create a count array
        int range = max_val - min_val + 1;
        if (range > 2'000'000) {
            // Fall back to sorting method if range is too large
            return sortingMethod(arr);
        }

        vector<bool> count(range, false);
        for (int num : arr) {
            count[num - min_val] = true;
        }

        // Calculate ranks
        vector<int> ranks(range);
        int rank = 1;
        for (int i = 0; i < range; i++) {
            if (count[i]) {
                ranks[i] = rank++;
            }
        }

        // Assign ranks to original array
        for (int& num : arr) {
            num = ranks[num - min_val];
        }

        return arr;
    }

private:
    vector<int> sortingMethod(vector<int>& arr) {
        vector<int> sortedArr = arr;
        sort(sortedArr.begin(), sortedArr.end());
        
        unordered_map<int, int> rankMap;
        int rank = 1;
        for (int num : sortedArr) {
            if (rankMap.find(num) == rankMap.end()) {
                rankMap[num] = rank++;
            }
        }
        
        vector<int> result(arr.size());
        for (int i = 0; i < arr.size(); i++) {
            result[i] = rankMap[arr[i]];
        }
        
        return result;
    }
};
```

```Python []
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        # Find min and max values
        min_val, max_val = min(arr), max(arr)

        # Create a count array
        range_val = max_val - min_val + 1
        if range_val > 2_000_000:
            # Fall back to sorting method if range is too large
            return self.sortingMethod(arr)

        count = [False] * range_val
        for num in arr:
            count[num - min_val] = True

        # Calculate ranks
        ranks = [0] * range_val
        rank = 1
        for i in range(range_val):
            if count[i]:
                ranks[i] = rank
                rank += 1

        # Assign ranks to original array
        return [ranks[num - min_val] for num in arr]

    def sortingMethod(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        rank_map = {num: i + 1 for i, num in enumerate(sorted_arr)}
        return [rank_map[num] for num in arr]
```

### Approach 2

```Java []
class Solution {
    public int[] arrayRankTransform(int[] arr) {
        if (arr == null || arr.length == 0) {
            return new int[0];
        }

        // Step 1: Create a copy of the original array
        int n = arr.length;
        int[] sortedArr = Arrays.copyOf(arr, n);

        // Step 2: Sort the copy
        Arrays.sort(sortedArr);

        // Step 3: Use a map to assign ranks
        Map<Integer, Integer> rankMap = new HashMap<>();
        int rank = 1;

        for (int num : sortedArr) {
            if (!rankMap.containsKey(num)) {
                rankMap.put(num, rank++);
            }
        }

        // Step 4: Create the result array using the rankMap
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = rankMap.get(arr[i]);
        }

        return result;
    }
}
```
```C++ []

```
```Python []

```
