### Intuition


## Understanding the Challenge

Imagine you're in a bustling city with an intricate bus system. Each bus follows a fixed route, looping through a series of stops indefinitely. Your task is to figure out how to get from one point in the city (let's call it the source) to another (the target) using the fewest number of bus rides possible. It's like solving a puzzle where the pieces are bus routes, and you need to connect them in the most efficient way.

The challenge becomes more interesting when you consider the constraints:
- There could be up to 500 different bus routes.
- Each route could have up to 100,000 stops.
- The bus stop numbers could be quite large, up to 1,000,000.

These constraints tell us that we're dealing with a potentially vast transportation network. It's not just about finding any path from source to target; it's about finding the optimal path in a complex system.

## Reframing the Problem

To tackle this challenge, let's reframe it in a way that makes it more manageable:

1. **Graph Perspective**: Think of the bus system as a graph. Each bus stop is a node, and each bus route creates edges between the stops it serves. Our job is to find the shortest path in this graph, where the distance is measured in the number of bus changes, not physical distance.

2. **Connectivity Analysis**: We're not just looking for a route; we're analyzing the connectivity of the entire bus network. How do different routes intersect? Which stops serve as key transfer points?

3. **Optimization Challenge**: At its core, this is an optimization problem. We're trying to minimize a specific metric: the number of bus rides needed to reach our destination.

## Key Observations and Insights

As we start to think about solving this problem, several key insights emerge:

1. **Route Intersections are Crucial**: The points where different bus routes intersect are pivotal. These are our transfer points, and they'll be key in finding efficient paths through the network.

2. **Thinking in "Hops"**: Instead of physical distance, we need to think in terms of "hops" from one route to another. Each hop represents a bus change.

3. **Bidirectional Nature**: A bus route can be traveled in both directions. This means that if we can reach any stop on a route, we can reach all stops on that route with no additional bus changes.

4. **Initial State vs. Goal State**: We start at the source stop, not on any bus. Our goal is to reach the target stop. The path between these two states is what we need to optimize.

## Developing a Solution Strategy

Now that we've reframed the problem and made some key observations, let's think about how we might approach solving it:

1. **Mapping the Network**: Our first step could be to create a representation of the entire bus network. We need to know which stops are connected by which routes.

2. **Distance Metric**: In this problem, our "distance" isn't physical but is measured in the number of bus changes. How can we keep track of this as we explore the network?

3. **Exploration Strategy**: We need a way to systematically explore the network, starting from our source stop. What's an efficient way to do this that ensures we find the optimal path?

4. **Optimization Process**: As we explore, we need to continually update and optimize our paths. How can we ensure we're always working with the best known path to each stop?

5. **Termination Conditions**: When do we know we've found the best solution? Or when can we conclude that no solution exists?

## Mathematical Insights

Let's delve into some mathematical concepts that can help us formalize our approach:

1. **Graph Theory**: We can represent our bus network as a graph G = (V, E), where V is the set of all bus stops and E is the set of connections between stops (bus routes).

2. **Shortest Path Problem**: Our task is essentially finding the shortest path in a weighted graph, where the weight of each edge is 1 (representing one bus change).

3. **Breadth-First Search (BFS)**: The nature of our problem, where we're looking for the path with the fewest "hops," suggests that a BFS-like approach could be effective.

4. **Dynamic Programming**: As we explore the network, we can use dynamic programming principles to store and update the best known path to each stop.

## Proposed Approach: Iterative Relaxation

Based on our insights and mathematical understanding, let's consider an approach I'll call "Iterative Relaxation." Here's how it works:

1. **Initialize**: Start by assuming it takes an infinite number of buses to reach any stop except the source (which takes 0 buses to reach).

2. **Iterate through Routes**: For each bus route, look at all the stops on that route. If we can reach any stop on the route in fewer buses than we thought, update our estimate for all stops on that route.

3. **Repeat**: Keep iterating through all routes until we make no more updates. This means we've found the optimal number of buses to reach each stop.

4. **Check Result**: After we've finished iterating, check how many buses it takes to reach the target stop. If it's still "infinite," there's no path.

Why might this approach work? It's based on the idea that if we can reach one stop on a route, we can reach all stops on that route with at most one additional bus ride. By repeatedly applying this logic, we'll eventually find the shortest path to all reachable stops.

## Mathematical Formulation

Let's formalize this approach mathematically:

1. Let B[i] be the minimum number of buses needed to reach stop i.
2. Initialize B[source] = 0, and B[i] = ∞ for all other i.
3. For each route R:
   - Let m = min(B[i] for i in R)
   - For each stop j in R:
     - B[j] = min(B[j], m + 1)
4. Repeat step 3 until no changes are made.
5. The answer is B[target] if B[target] < ∞, else -1.

This formulation captures the essence of our iterative relaxation approach.

## Handling Edge Cases and Potential Pitfalls

As we develop this solution, we need to consider various edge cases and potential issues:

1. **Source = Target**: What if the source and target are the same? We need to handle this trivial case efficiently.

2. **Disconnected Network**: How do we detect and handle cases where there's no path from source to target?

3. **Large Networks**: With potentially millions of stops, how do we ensure our solution remains efficient?

4. **Cycles in Routes**: Our approach needs to handle the cyclic nature of bus routes correctly.

5. **Optimal Substructure**: Does our problem have optimal substructure? In other words, is the optimal solution to the whole problem composed of optimal solutions to subproblems?

## Advantages of this Approach

This iterative relaxation approach has several advantages:

1. **Completeness**: It explores all possible paths, ensuring we find the optimal solution if one exists.

2. **Simplicity**: The core idea is straightforward and intuitive, making it easier to implement and debug.

3. **Efficiency**: By updating estimates for all stops on a route at once, we potentially reduce the number of iterations needed.

4. **Flexibility**: This approach can be easily adapted to handle additional constraints or optimize for different criteria.

5. **Natural Handling of Cycles**: The cyclic nature of bus routes is implicitly handled without needing special treatment.

## Conclusion

Solving the bus route problem requires us to think about connectivity, optimization, and efficient exploration of complex networks. By reframing the problem in terms of graph theory and developing an iterative relaxation approach, we've created a solution that's both intuitive and mathematically sound.

This approach demonstrates how breaking down a complex problem into simpler components and applying systematic logic can lead to elegant solutions. It also showcases the power of iterative improvement in optimization problems.

As we move from intuition to implementation, the key will be translating these concepts into efficient code while carefully handling edge cases and maintaining the core logic of our approach.

### Apprroach 1

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

### Intuition
### Transitioning from the Previous Approach

In our earlier discussion, we approached the bus routes problem as a shortest-path challenge in a graph, where each bus stop was treated as a node and each bus route as a connection between nodes. We relied on an exhaustive exploration method that systematically relaxed each route until we found the minimum number of bus rides needed to reach the target. While this method ensured that all possible paths were considered, it had room for optimization, especially in terms of the number of iterations required to reach the solution.

### Why Consider a New Approach?

The exhaustive method we previously discussed works well for finding the shortest path, but it can be computationally expensive, especially when the routes and stops are numerous. The main drawback of the previous approach is its one-directional search, which may result in redundant explorations, particularly when the source and target are far apart on the bus route network. This is where a more efficient search strategy like **Bidirectional Breadth-First Search (BFS)** comes into play.

### Intuition Behind the Bidirectional BFS Approach

Bidirectional BFS is a powerful optimization over traditional BFS, especially in scenarios where the search space is large, as it allows us to explore from both the source and target simultaneously, reducing the overall number of steps needed to meet in the middle.

Here's how this strategy works:

1. **Initial Setup and Map Construction:** 
   - We begin by constructing a map (`stopToRoutes`) that records which routes pass through each bus stop. This mapping is crucial because it allows us to quickly identify all the routes that can be accessed from a particular stop.
   - For instance, if you’re at stop 5, and two routes (say, Route A and Route B) pass through this stop, the map will quickly tell us that from stop 5, you can board buses on either Route A or Route B.

2. **Bidirectional Search Initialization:**
   - We initialize two sets: one representing stops reachable from the `source` (`sourceStops`) and another representing stops reachable from the `target` (`targetStops`).
   - Additionally, we maintain a set of visited routes to avoid redundant checks and looping back through the same route.

3. **Two-Way Exploration:**
   - Instead of exploring the graph in a single direction from the source, we explore from both the source and the target. This significantly reduces the number of steps required to find a connection, as the search space is halved.
   - During each iteration, we always choose to expand the smaller of the two frontiers (either `sourceStops` or `targetStops`). This ensures that the number of nodes (stops) explored is minimized, further optimizing the search.

4. **Connecting Source and Target:**
   - For each stop in the current frontier (either `sourceStops` or `targetStops`), we explore all routes passing through that stop. If any route connects to a stop already visited by the other frontier, we've found the shortest path.
   - The BFS continues until the frontiers intersect, meaning we've successfully connected a stop reachable from the source to a stop reachable from the target using the minimum number of bus rides.

5. **Edge Cases:**
   - If the `source` and `target` are the same, the solution is immediate: no buses are needed.
   - If after exhausting all possible routes the frontiers never intersect, it means there's no way to reach the target from the source, and the function returns `-1`.

### Conclusion

This Bidirectional BFS approach offers a much more efficient way of solving the problem by taking advantage of simultaneous exploration from both the start and end points. By ensuring that the search progresses from the smaller frontier, the algorithm minimizes unnecessary explorations and quickly zeroes in on the shortest path. This method is particularly effective in large graphs, like a complex bus route network, where the traditional BFS might be too slow due to its unidirectional nature. Through this method, we achieve a solution that is both time-efficient and memory-efficient, making it a powerful tool for solving shortest-path problems in large search spaces.
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
