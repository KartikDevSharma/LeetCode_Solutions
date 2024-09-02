Apprroach 1

```Java []
class Solution {
    public int numBusesToDestination(int[][] busRoutes, int start, int end) {
        if (start == end) return 0;

        int maxBusStop = findMaxBusStop(busRoutes);
        if (maxBusStop < end || start > maxBusStop || end > maxBusStop) {
            return -1;
        }

        int routeCount = busRoutes.length;
        int[] minBusesToReach = new int[maxBusStop + 1];
        Arrays.fill(minBusesToReach, routeCount + 1);
        minBusesToReach[start] = 0;

        boolean updated;
        do {
            updated = false;
            for (int[] route : busRoutes) {
                int minBusesForRoute = findMinBusesForRoute(route, minBusesToReach);
                updated |= updateMinBuses(route, minBusesForRoute, minBusesToReach);
            }
        } while (updated);

        return minBusesToReach[end] > routeCount ? -1 : minBusesToReach[end];
    }

    private int findMaxBusStop(int[][] routes) {
        int max = -1;
        for (int[] route : routes) {
            for (int stop : route) {
                max = Math.max(max, stop);
            }
        }
        return max;
    }

    private int findMinBusesForRoute(int[] route, int[] minBusesToReach) {
        int min = Integer.MAX_VALUE;
        for (int stop : route) {
            min = Math.min(minBusesToReach[stop], min);
        }
        return min + 1;
    }

    private boolean updateMinBuses(int[] route, int minBuses, int[] minBusesToReach) {
        boolean updated = false;
        for (int stop : route) {
            if (minBusesToReach[stop] > minBuses) {
                minBusesToReach[stop] = minBuses;
                updated = true;
            }
        }
        return updated;
    }
}

```
```c++ []
class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& busRoutes, int start, int end) {
        if (start == end) return 0;

        int maxBusStop = findMaxBusStop(busRoutes);
        if (maxBusStop < end || start > maxBusStop || end > maxBusStop) {
            return -1;
        }

        int routeCount = busRoutes.size();
        vector<int> minBusesToReach(maxBusStop + 1, routeCount + 1);
        minBusesToReach[start] = 0;

        bool updated;
        do {
            updated = false;
            for (const auto& route : busRoutes) {
                int minBusesForRoute = findMinBusesForRoute(route, minBusesToReach);
                updated |= updateMinBuses(route, minBusesForRoute, minBusesToReach);
            }
        } while (updated);

        return minBusesToReach[end] > routeCount ? -1 : minBusesToReach[end];
    }

private:
    int findMaxBusStop(const vector<vector<int>>& routes) {
        int max = -1;
        for (const auto& route : routes) {
            for (int stop : route) {
                max = std::max(max, stop);
            }
        }
        return max;
    }

    int findMinBusesForRoute(const vector<int>& route, const vector<int>& minBusesToReach) {
        int min = INT_MAX;
        for (int stop : route) {
            min = std::min(minBusesToReach[stop], min);
        }
        return min + 1;
    }

    bool updateMinBuses(const vector<int>& route, int minBuses, vector<int>& minBusesToReach) {
        bool updated = false;
        for (int stop : route) {
            if (minBusesToReach[stop] > minBuses) {
                minBusesToReach[stop] = minBuses;
                updated = true;
            }
        }
        return updated;
    }
};
static const int kds = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();

```
```python []
class Solution:
    def numBusesToDestination(self, busRoutes: List[List[int]], start: int, end: int) -> int:
        if start == end:
            return 0
        
        max_bus_stop = self.find_max_bus_stop(busRoutes)
        if max_bus_stop < end or start > max_bus_stop or end > max_bus_stop:
            return -1
        
        route_count = len(busRoutes)
        min_buses_to_reach = [route_count + 1] * (max_bus_stop + 1)
        min_buses_to_reach[start] = 0
        
        updated = True
        while updated:
            updated = False
            for route in busRoutes:
                min_buses_for_route = self.find_min_buses_for_route(route, min_buses_to_reach)
                updated |= self.update_min_buses(route, min_buses_for_route, min_buses_to_reach)
        
        return min_buses_to_reach[end] if min_buses_to_reach[end] <= route_count else -1
    
    def find_max_bus_stop(self, routes):
        return max(max(route) for route in routes)
    
    def find_min_buses_for_route(self, route, min_buses_to_reach):
        return min(min_buses_to_reach[stop] for stop in route) + 1
    
    def update_min_buses(self, route, min_buses, min_buses_to_reach):
        updated = False
        for stop in route:
            if min_buses_to_reach[stop] > min_buses:
                min_buses_to_reach[stop] = min_buses
                updated = True
        return updated


def format_output(result):
    return str(result)

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    results = []
    i = 0
    while i < len(lines):

        routes = json.loads(lines[i])
        i += 1

        source = int(lines[i])
        i += 1

        target = int(lines[i])
        i += 1
        

        result = Solution().numBusesToDestination(routes, source, target)
        formatted_result = format_output(result)
        results.append(formatted_result)
    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)

```

```Go []
func numBusesToDestination(busRoutes [][]int, start int, end int) int {
	if start == end {
		return 0
	}

	maxBusStop := findMaxBusStop(busRoutes)
	if maxBusStop < end || start > maxBusStop || end > maxBusStop {
		return -1
	}

	routeCount := len(busRoutes)
	minBusesToReach := make([]int, maxBusStop+1)
	for i := range minBusesToReach {
		minBusesToReach[i] = routeCount + 1
	}
	minBusesToReach[start] = 0

	updated := true
	for updated {
		updated = false
		for _, route := range busRoutes {
			minBusesForRoute := findMinBusesForRoute(route, minBusesToReach)
			updated = updated || updateMinBuses(route, minBusesForRoute, minBusesToReach)
		}
	}

	if minBusesToReach[end] > routeCount {
		return -1
	}
	return minBusesToReach[end]
}

func findMaxBusStop(routes [][]int) int {
	max := -1
	for _, route := range routes {
		for _, stop := range route {
			if stop > max {
				max = stop
			}
		}
	}
	return max
}

func findMinBusesForRoute(route []int, minBusesToReach []int) int {
	min := math.MaxInt32
	for _, stop := range route {
		if minBusesToReach[stop] < min {
			min = minBusesToReach[stop]
		}
	}
	return min + 1
}

func updateMinBuses(route []int, minBuses int, minBusesToReach []int) bool {
	updated := false
	for _, stop := range route {
		if minBusesToReach[stop] > minBuses {
			minBusesToReach[stop] = minBuses
			updated = true
		}
	}
	return updated
}


```
```c# []
public class Solution {
    public int NumBusesToDestination(int[][] busRoutes, int source, int target) {
        if (source == target) return 0;

        int maxBusStop = FindMaxBusStop(busRoutes);
        if (maxBusStop < target || source > maxBusStop || target > maxBusStop) {
            return -1;
        }

        int routeCount = busRoutes.Length;
        int[] minBusesToReach = new int[maxBusStop + 1];
        Array.Fill(minBusesToReach, routeCount + 1);
        minBusesToReach[source] = 0;

        bool updated;
        do {
            updated = false;
            foreach (var route in busRoutes) {
                int minBusesForRoute = FindMinBusesForRoute(route, minBusesToReach);
                updated |= UpdateMinBuses(route, minBusesForRoute, minBusesToReach);
            }
        } while (updated);

        return minBusesToReach[target] > routeCount ? -1 : minBusesToReach[target];
    }

    private int FindMaxBusStop(int[][] routes) {
        int max = -1;
        foreach (var route in routes) {
            foreach (int stop in route) {
                max = Math.Max(max, stop);
            }
        }
        return max;
    }

    private int FindMinBusesForRoute(int[] route, int[] minBusesToReach) {
        int min = int.MaxValue;
        foreach (int stop in route) {
            min = Math.Min(minBusesToReach[stop], min);
        }
        return min + 1;
    }

    private bool UpdateMinBuses(int[] route, int minBuses, int[] minBusesToReach) {
        bool updated = false;
        foreach (int stop in route) {
            if (minBusesToReach[stop] > minBuses) {
                minBusesToReach[stop] = minBuses;
                updated = true;
            }
        }
        return updated;
    }
}
```
```kotlin []
class Solution {
    fun numBusesToDestination(busRoutes: Array<IntArray>, source: Int, target: Int): Int {
        if (source == target) return 0

        val maxBusStop = findMaxBusStop(busRoutes)
        if (maxBusStop < target || source > maxBusStop || target > maxBusStop) {
            return -1
        }

        val routeCount = busRoutes.size
        val minBusesToReach = IntArray(maxBusStop + 1) { routeCount + 1 }
        minBusesToReach[source] = 0

        var updated: Boolean
        do {
            updated = false
            for (route in busRoutes) {
                val minBusesForRoute = findMinBusesForRoute(route, minBusesToReach)
                updated = updated || updateMinBuses(route, minBusesForRoute, minBusesToReach)
            }
        } while (updated)

        return if (minBusesToReach[target] > routeCount) -1 else minBusesToReach[target]
    }

    private fun findMaxBusStop(routes: Array<IntArray>): Int {
        var max = -1
        for (route in routes) {
            for (stop in route) {
                max = maxOf(max, stop)
            }
        }
        return max
    }

    private fun findMinBusesForRoute(route: IntArray, minBusesToReach: IntArray): Int {
        var min = Int.MAX_VALUE
        for (stop in route) {
            min = minOf(min, minBusesToReach[stop])
        }
        return min + 1
    }

    private fun updateMinBuses(route: IntArray, minBuses: Int, minBusesToReach: IntArray): Boolean {
        var updated = false
        for (stop in route) {
            if (minBusesToReach[stop] > minBuses) {
                minBusesToReach[stop] = minBuses
                updated = true
            }
        }
        return updated
    }
}
```
```Rust []
use std::cmp::{min, max};

impl Solution {
    pub fn num_buses_to_destination(bus_routes: Vec<Vec<i32>>, start: i32, end: i32) -> i32 {
        if start == end {
            return 0;
        }

        let max_bus_stop = Self::find_max_bus_stop(&bus_routes);
        if max_bus_stop < end || start > max_bus_stop || end > max_bus_stop {
            return -1;
        }

        let route_count = bus_routes.len();
        let mut min_buses_to_reach = vec![route_count as i32 + 1; (max_bus_stop + 1) as usize];
        min_buses_to_reach[start as usize] = 0;

        let mut updated = true;
        while updated {
            updated = false;
            for route in &bus_routes {
                let min_buses_for_route = Self::find_min_buses_for_route(route, &min_buses_to_reach);
                updated |= Self::update_min_buses(route, min_buses_for_route, &mut min_buses_to_reach);
            }
        }

        if min_buses_to_reach[end as usize] > route_count as i32 {
            return -1;
        }
        min_buses_to_reach[end as usize]
    }

    fn find_max_bus_stop(routes: &[Vec<i32>]) -> i32 {
        let mut max_stop = -1;
        for route in routes {
            for &stop in route {
                max_stop = max(max_stop, stop);
            }
        }
        max_stop
    }

    fn find_min_buses_for_route(route: &[i32], min_buses_to_reach: &[i32]) -> i32 {
        route.iter().map(|&stop| min_buses_to_reach[stop as usize]).min().unwrap_or(i32::MAX) + 1
    }

    fn update_min_buses(route: &[i32], min_buses: i32, min_buses_to_reach: &mut [i32]) -> bool {
        let mut updated = false;
        for &stop in route {
            if min_buses_to_reach[stop as usize] > min_buses {
                min_buses_to_reach[stop as usize] = min_buses;
                updated = true;
            }
        }
        updated
    }
}


```
```TypeScript []
function numBusesToDestination(busRoutes: number[][], source: number, target: number): number {
    if (source === target) return 0;

    const maxBusStop = findMaxBusStop(busRoutes);
    if (maxBusStop < target || source > maxBusStop || target > maxBusStop) {
        return -1;
    }

    const routeCount = busRoutes.length;
    const minBusesToReach = new Array(maxBusStop + 1).fill(routeCount + 1);
    minBusesToReach[source] = 0;

    let updated: boolean;
    do {
        updated = false;
        for (const route of busRoutes) {
            const minBusesForRoute = findMinBusesForRoute(route, minBusesToReach);
            updated = updated || updateMinBuses(route, minBusesForRoute, minBusesToReach);
        }
    } while (updated);

    return minBusesToReach[target] > routeCount ? -1 : minBusesToReach[target];
}

function findMaxBusStop(routes: number[][]): number {
    let max = -1;
    for (const route of routes) {
        for (const stop of route) {
            max = Math.max(max, stop);
        }
    }
    return max;
}

function findMinBusesForRoute(route: number[], minBusesToReach: number[]): number {
    let min = Number.MAX_SAFE_INTEGER;
    for (const stop of route) {
        min = Math.min(min, minBusesToReach[stop]);
    }
    return min + 1;
}

function updateMinBuses(route: number[], minBuses: number, minBusesToReach: number[]): boolean {
    let updated = false;
    for (const stop of route) {
        if (minBusesToReach[stop] > minBuses) {
            minBusesToReach[stop] = minBuses;
            updated = true;
        }
    }
    return updated;
}
```
```JavaScript []
/**
 * @param {number[][]} routes
 * @param {number} source
 * @param {number} target
 * @return {number}
 */
var numBusesToDestination = function(busRoutes, start, end) {
    if (start === end) return 0;

    const maxBusStop = findMaxBusStop(busRoutes);
    if (maxBusStop < end || start > maxBusStop || end > maxBusStop) {
        return -1;
    }

    const routeCount = busRoutes.length;
    const minBusesToReach = new Array(maxBusStop + 1).fill(routeCount + 1);
    minBusesToReach[start] = 0;

    let updated;
    do {
        updated = false;
        for (const route of busRoutes) {
            const minBusesForRoute = findMinBusesForRoute(route, minBusesToReach);
            updated = updated || updateMinBuses(route, minBusesForRoute, minBusesToReach);
        }
    } while (updated);

    return minBusesToReach[end] > routeCount ? -1 : minBusesToReach[end];
};

function findMaxBusStop(routes) {
    let max = -1;
    for (const route of routes) {
        for (const stop of route) {
            max = Math.max(max, stop);
        }
    }
    return max;
}

function findMinBusesForRoute(route, minBusesToReach) {
    let min = Infinity;
    for (const stop of route) {
        min = Math.min(min, minBusesToReach[stop]);
    }
    return min + 1;
}

function updateMinBuses(route, minBuses, minBusesToReach) {
    let updated = false;
    for (const stop of route) {
        if (minBusesToReach[stop] > minBuses) {
            minBusesToReach[stop] = minBuses;
            updated = true;
        }
    }
    return updated;
}


```
---






---
Approach 2
```Java []
class Solution {
    public int numBusesToDestination(int[][] routes, int source, int target) {
        if (source == target) return 0;

        // Build stop to routes map
        Map<Integer, Set<Integer>> stopToRoutes = new HashMap<>();
        for (int i = 0; i < routes.length; i++) {
            for (int stop : routes[i]) {
                stopToRoutes.computeIfAbsent(stop, k -> new HashSet<>()).add(i);
            }
        }

        // Two-way BFS
        Set<Integer> sourceStops = new HashSet<>(Arrays.asList(source));
        Set<Integer> targetStops = new HashSet<>(Arrays.asList(target));
        Set<Integer> visitedRoutes = new HashSet<>();
        int steps = 0;

        while (!sourceStops.isEmpty() && !targetStops.isEmpty()) {
            if (sourceStops.size() > targetStops.size()) {
                Set<Integer> temp = sourceStops;
                sourceStops = targetStops;
                targetStops = temp;
            }

            Set<Integer> nextStops = new HashSet<>();
            steps++;

            for (int stop : sourceStops) {
                for (int route : stopToRoutes.getOrDefault(stop, Collections.emptySet())) {
                    if (visitedRoutes.add(route)) {
                        for (int nextStop : routes[route]) {
                            if (targetStops.contains(nextStop)) return steps;
                            nextStops.add(nextStop);
                        }
                    }
                }
            }

            sourceStops = nextStops;
        }

        return -1;
    }
}

```
```c++ []
class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target) return 0;

        // Build stop to routes map
        unordered_map<int, unordered_set<int>> stopToRoutes;
        for (int i = 0; i < routes.size(); i++) {
            for (int stop : routes[i]) {
                stopToRoutes[stop].insert(i);
            }
        }

        // Two-way BFS
        unordered_set<int> sourceStops = {source};
        unordered_set<int> targetStops = {target};
        unordered_set<int> visitedRoutes;
        int steps = 0;

        while (!sourceStops.empty() && !targetStops.empty()) {
            if (sourceStops.size() > targetStops.size()) {
                swap(sourceStops, targetStops);
            }

            unordered_set<int> nextStops;
            steps++;

            for (int stop : sourceStops) {
                for (int route : stopToRoutes[stop]) {
                    if (visitedRoutes.insert(route).second) {
                        for (int nextStop : routes[route]) {
                            if (targetStops.count(nextStop)) return steps;
                            nextStops.insert(nextStop);
                        }
                    }
                }
            }

            sourceStops = move(nextStops);
        }

        return -1;
    }
};

static const int kds = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();


```
```python []
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Build stop to routes map
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        # Two-way BFS
        source_stops = {source}
        target_stops = {target}
        visited_routes = set()
        steps = 0

        while source_stops and target_stops:
            if len(source_stops) > len(target_stops):
                source_stops, target_stops = target_stops, source_stops

            next_stops = set()
            steps += 1

            for stop in source_stops:
                for route in stop_to_routes[stop]:
                    if route not in visited_routes:
                        visited_routes.add(route)
                        for next_stop in routes[route]:
                            if next_stop in target_stops:
                                return steps
                            next_stops.add(next_stop)

            source_stops = next_stops

        return -1


def format_output(result):
    return str(result)

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    results = []
    i = 0
    while i < len(lines):

        routes = json.loads(lines[i])
        i += 1

        source = int(lines[i])
        i += 1

        target = int(lines[i])
        i += 1
        

        result = Solution().numBusesToDestination(routes, source, target)
        formatted_result = format_output(result)
        results.append(formatted_result)
    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)

```
```Go []
func numBusesToDestination(routes [][]int, source int, target int) int {
    if source == target {
        return 0
    }

    // Build stop to routes map
    stopToRoutes := make(map[int][]int)
    for i, route := range routes {
        for _, stop := range route {
            stopToRoutes[stop] = append(stopToRoutes[stop], i)
        }
    }

    // Two-way BFS
    sourceStops := map[int]bool{source: true}
    targetStops := map[int]bool{target: true}
    visitedRoutes := map[int]bool{}
    steps := 0

    for len(sourceStops) > 0 && len(targetStops) > 0 {
        if len(sourceStops) > len(targetStops) {
            sourceStops, targetStops = targetStops, sourceStops
        }

        var nextStops = map[int]bool{}
        steps++

        for stop := range sourceStops {
            for _, route := range stopToRoutes[stop] {
                if !visitedRoutes[route] {
                    visitedRoutes[route] = true
                    for _, nextStop := range routes[route] {
                        if targetStops[nextStop] {
                            return steps
                        }
                        nextStops[nextStop] = true
                    }
                }
            }
        }

        sourceStops = nextStops
    }

    return -1
}
```
```c# []
public class Solution {
    public int NumBusesToDestination(int[][] routes, int source, int target) {
        if (source == target) return 0;

        // Build stop to routes map
        var stopToRoutes = new Dictionary<int, HashSet<int>>();
        for (int i = 0; i < routes.Length; i++) {
            foreach (int stop in routes[i]) {
                if (!stopToRoutes.ContainsKey(stop)) {
                    stopToRoutes[stop] = new HashSet<int>();
                }
                stopToRoutes[stop].Add(i);
            }
        }

        // Two-way BFS
        var sourceStops = new HashSet<int> { source };
        var targetStops = new HashSet<int> { target };
        var visitedRoutes = new HashSet<int>();
        int steps = 0;

        while (sourceStops.Count > 0 && targetStops.Count > 0) {
            if (sourceStops.Count > targetStops.Count) {
                (sourceStops, targetStops) = (targetStops, sourceStops);
            }

            var nextStops = new HashSet<int>();
            steps++;

            foreach (int stop in sourceStops) {
                foreach (int route in stopToRoutes.GetValueOrDefault(stop, new HashSet<int>())) {
                    if (visitedRoutes.Add(route)) {
                        foreach (int nextStop in routes[route]) {
                            if (targetStops.Contains(nextStop)) {
                                return steps;
                            }
                            nextStops.Add(nextStop);
                        }
                    }
                }
            }

            sourceStops = nextStops;
        }

        return -1;
    }
}
```
```kotlin []
class Solution {
    fun numBusesToDestination(routes: Array<IntArray>, source: Int, target: Int): Int {
        if (source == target) return 0

        // Build stop to routes map
        val stopToRoutes = mutableMapOf<Int, MutableSet<Int>>()
        for (i in routes.indices) {
            for (stop in routes[i]) {
                stopToRoutes.getOrPut(stop) { mutableSetOf() }.add(i)
            }
        }

        // Two-way BFS
        var sourceStops = mutableSetOf(source)
        var targetStops = mutableSetOf(target)
        val visitedRoutes = mutableSetOf<Int>()
        var steps = 0

        while (sourceStops.isNotEmpty() && targetStops.isNotEmpty()) {
            if (sourceStops.size > targetStops.size) {
                var temp = sourceStops
                sourceStops = targetStops
                targetStops = temp
            }

            val nextStops = mutableSetOf<Int>()
            steps++

            for (stop in sourceStops) {
                for (route in stopToRoutes[stop].orEmpty()) {
                    if (route !in visitedRoutes) {
                        visitedRoutes.add(route)
                        for (nextStop in routes[route]) {
                            if (nextStop in targetStops) return steps
                            nextStops.add(nextStop)
                        }
                    }
                }
            }

            sourceStops.clear()
            sourceStops.addAll(nextStops)
        }

        return -1
    }
}
```
```Rust []
use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn num_buses_to_destination(routes: Vec<Vec<i32>>, source: i32, target: i32) -> i32 {
        if source == target {
            return 0;
        }

        // Build stop to routes map
        let mut stop_to_routes = HashMap::new();
        for (route_id, route) in routes.iter().enumerate() {
            for &stop in route {
                stop_to_routes.entry(stop).or_insert_with(HashSet::new).insert(route_id);
            }
        }

        // Two-way BFS
        let mut source_stops = HashSet::new();
        source_stops.insert(source);
        let mut target_stops = HashSet::new();
        target_stops.insert(target);

        let mut visited_routes = HashSet::new();
        let mut steps = 0;

        let mut queue = VecDeque::new();
        queue.push_back((source_stops, target_stops, visited_routes));

        while let Some((mut source_stops, mut target_stops, mut visited_routes)) = queue.pop_front() {
            if source_stops.len() > target_stops.len() {
                std::mem::swap(&mut source_stops, &mut target_stops);
            }

            let mut next_stops = HashSet::new();
            steps += 1;

            for &stop in source_stops.iter() {
                if let Some(routes_set) = stop_to_routes.get(&stop) {
                    for &route in routes_set.iter() {
                        if visited_routes.insert(route) {
                            let route_stops = &routes[route]; // Access the route stops correctly
                            for &next_stop in route_stops.iter() {
                                if target_stops.contains(&next_stop) {
                                    return steps;
                                }
                                next_stops.insert(next_stop);
                            }
                        }
                    }
                }
            }

            if next_stops.is_empty() {
                continue;
            }

            queue.push_back((next_stops, target_stops, visited_routes));
        }

        -1
    }
}

```
```TypeScript []
function numBusesToDestination(routes: number[][], source: number, target: number): number {
    if (source === target) return 0;

    // Build stop to routes map
    const stopToRoutes: Map<number, Set<number>> = new Map();
    for (let i = 0; i < routes.length; i++) {
        for (const stop of routes[i]) {
            if (!stopToRoutes.has(stop)) {
                stopToRoutes.set(stop, new Set());
            }
            stopToRoutes.get(stop)!.add(i);
        }
    }

    // Two-way BFS
    let sourceStops: Set<number> = new Set([source]);
    let targetStops: Set<number> = new Set([target]);
    const visitedRoutes: Set<number> = new Set();
    let steps = 0;

    while (sourceStops.size > 0 && targetStops.size > 0) {
        if (sourceStops.size > targetStops.size) {
            let temp = sourceStops;
            sourceStops = targetStops;
            targetStops = temp;
        }

        const nextStops: Set<number> = new Set();
        steps++;

        for (const stop of sourceStops) {
            for (const route of stopToRoutes.get(stop) || []) {
                if (!visitedRoutes.has(route)) {
                    visitedRoutes.add(route);
                    for (const nextStop of routes[route]) {
                        if (targetStops.has(nextStop)) {
                            return steps;
                        }
                        nextStops.add(nextStop);
                    }
                }
            }
        }

        sourceStops = nextStops;
    }

    return -1;
}
```
```JavaScript []
/**
 * @param {number[][]} routes
 * @param {number} source
 * @param {number} target
 * @return {number}
 */
var numBusesToDestination = function(routes, source, target) {
    if (source === target) return 0;

    // Build stop to routes map
    const stopToRoutes = new Map();
    for (let i = 0; i < routes.length; i++) {
        for (const stop of routes[i]) {
            if (!stopToRoutes.has(stop)) {
                stopToRoutes.set(stop, new Set());
            }
            stopToRoutes.get(stop).add(i);
        }
    }

    // Two-way BFS
    let sourceStops = new Set([source]);
    let targetStops = new Set([target]);
    const visitedRoutes = new Set();
    let steps = 0;

    while (sourceStops.size > 0 && targetStops.size > 0) {
        if (sourceStops.size > targetStops.size) {
            [sourceStops, targetStops] = [targetStops, sourceStops];
        }

        const nextStops = new Set();
        steps++;

        for (const stop of sourceStops) {
            for (const route of (stopToRoutes.get(stop) || [])) {
                if (!visitedRoutes.has(route)) {
                    visitedRoutes.add(route);
                    for (const nextStop of routes[route]) {
                        if (targetStops.has(nextStop)) {
                            return steps;
                        }
                        nextStops.add(nextStop);
                    }
                }
            }
        }

        sourceStops = nextStops;
    }

    return -1;
};
```
