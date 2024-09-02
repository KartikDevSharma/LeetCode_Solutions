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
# Approach and Implementation: Solving the Bus Route Problem

## Overview of the Solution

Our solution to the bus route problem employs an iterative relaxation approach, which is inspired by the Bellman-Ford algorithm for finding shortest paths in a graph. The core idea is to repeatedly update the minimum number of buses required to reach each stop until we reach a stable state where no further improvements are possible.

Let's break down the solution into its key components and explore each in detail.

## 1. Initialization

Before we start our main algorithm, we need to set up our data structures and initial state.

```
function numBusesToDestination(busRoutes, start, end):
    if start == end:
        return 0
    
    maxBusStop = findMaxBusStop(busRoutes)
    if maxBusStop < end or start > maxBusStop or end > maxBusStop:
        return -1
    
    routeCount = length(busRoutes)
    minBusesToReach = array of size (maxBusStop + 1) filled with (routeCount + 1)
    minBusesToReach[start] = 0
```

### Key Points:

1. We first handle the trivial case where the start and end stops are the same, returning 0 as no buses are needed.

2. We find the maximum bus stop number. This is crucial for two reasons:
   - It allows us to create an array of the correct size to store our minimum bus counts.
   - It helps us quickly identify if the start or end stops are out of range.

3. We initialize our `minBusesToReach` array. This array is the heart of our algorithm:
   - The index represents a bus stop number.
   - The value at each index represents the minimum number of buses needed to reach that stop.
   - We initially set all values to `routeCount + 1`, which serves as our "infinity" value. We use `routeCount + 1` because it's impossible to need more buses than there are routes.
   - We set `minBusesToReach[start] = 0` because we're already at the start stop.

### Mathematical Insight:

The initialization step sets up our dynamic programming array. In essence, we're saying: "We don't know how to reach any stop except the start, and we know we can reach the start with 0 buses." This creates our base case for the iterative process that follows.

## 2. The Main Algorithm: Iterative Relaxation

The core of our solution is an iterative process where we repeatedly update our estimates of the minimum number of buses needed to reach each stop.

```
do:
    updated = false
    for each route in busRoutes:
        minBusesForRoute = findMinBusesForRoute(route, minBusesToReach)
        updated = updateMinBuses(route, minBusesForRoute, minBusesToReach) or updated
while updated

return minBusesToReach[end] > routeCount ? -1 : minBusesToReach[end]
```

### Key Points:

1. We continue iterating as long as we make updates in an iteration. This ensures we explore all possible improvements.

2. For each route, we:
   a. Find the minimum number of buses needed to reach any stop on that route.
   b. Update all stops on that route with this new minimum (if it's an improvement).

3. After the iterations complete, we check if we can reach the end stop. If `minBusesToReach[end]` is still greater than `routeCount`, it means we couldn't reach the end stop, so we return -1.

### Mathematical Insight:

This process is a form of dynamic programming and shares similarities with the Bellman-Ford algorithm. The key idea is the principle of relaxation: if we can improve our estimate for reaching any stop, we do so, and this improvement might lead to further improvements in subsequent iterations.

The mathematical justification for this approach lies in the optimal substructure of the problem:
- If the optimal path to stop B goes through stop A, then the optimal path to B consists of the optimal path to A plus one more bus ride.
- By iteratively applying this principle, we eventually find the optimal path to all reachable stops.

## 3. Finding the Minimum Buses for a Route

A crucial subroutine in our algorithm is finding the minimum number of buses needed to reach any stop on a given route.

```
function findMinBusesForRoute(route, minBusesToReach):
    min = INFINITY
    for each stop in route:
        min = minimum(minBusesToReach[stop], min)
    return min + 1
```

### Key Points:

1. We iterate through all stops on the route, finding the minimum `minBusesToReach` value among them.

2. We return this minimum value plus 1. Why? Because if we can reach any stop on this route with `X` buses, we can reach all other stops on this route with `X + 1` buses.

### Mathematical Insight:

This function embodies a key insight of our solution: the connectivity within a single bus route. Once we're on a bus, we can reach any stop on its route without changing buses. Therefore, the "cost" to reach any stop on a route is the minimum cost to reach any stop on that route, plus one bus ride.

## 4. Updating Minimum Buses

After finding the minimum number of buses for a route, we need to update our estimates for all stops on that route.

```
function updateMinBuses(route, minBuses, minBusesToReach):
    updated = false
    for each stop in route:
        if minBusesToReach[stop] > minBuses:
            minBusesToReach[stop] = minBuses
            updated = true
    return updated
```

### Key Points:

1. We iterate through all stops on the route.

2. If our new `minBuses` value is less than the current `minBusesToReach` value for a stop, we update it.

3. We keep track of whether we made any updates, as this informs our main loop whether to continue iterating.

### Mathematical Insight:

This function implements the relaxation step of our algorithm. In graph theory terms, we're "relaxing" the edges of our graph, updating the shortest path estimates whenever we find a better path.

The reason this works is due to the principle of optimality in dynamic programming: the optimal solution to a problem depends on the optimal solutions to its subproblems. By continually updating our estimates with better values, we're building up our optimal solution piece by piece.

## 5. Finding the Maximum Bus Stop

An important initialization step is finding the maximum bus stop number, which determines the size of our `minBusesToReach` array.

```
function findMaxBusStop(routes):
    max = -1
    for each route in routes:
        for each stop in route:
            max = maximum(max, stop)
    return max
```

### Key Points:

1. We iterate through all routes and all stops, keeping track of the highest stop number we encounter.

2. This function allows our solution to dynamically adjust to the input size, rather than assuming a fixed maximum stop number.

### Mathematical Insight:

While this function might seem simple, it plays a crucial role in the space complexity of our solution. By finding the true maximum stop number, we ensure that our `minBusesToReach` array is no larger than necessary. This is important because the problem constraints allow for up to 10^6 possible stop numbers, but any given input might use a much smaller range.

## Putting It All Together: The Complete Algorithm

Now that we've explored each component of our solution, let's look at how they fit together:

1. We start by handling the trivial case and initializing our data structures.
2. We enter a loop where we repeatedly:
   a. Examine each bus route.
   b. Find the minimum number of buses needed to reach any stop on that route.
   c. Update our estimates for all stops on that route if we've found a better path.
3. We continue this process until we make no more updates in a full iteration.
4. Finally, we check if we've found a path to the end stop and return the result.

This approach ensures that we explore all possible paths through the bus network, always keeping track of the minimum number of buses needed to reach each stop.

## Why This Approach Works

Our solution works because it systematically explores all possible paths through the bus network, always maintaining the minimum number of buses needed to reach each stop. Here's why this is effective:

1. **Completeness**: By repeatedly iterating through all routes, we ensure that we consider all possible paths through the network. This guarantees that if a path exists, we'll find it.

2. **Optimality**: Our update process always maintains the minimum number of buses needed. If we find a better path to a stop, we immediately update our estimate. This ensures that our final result is the optimal (minimum) number of buses needed.

3. **Handling Cycles**: Bus routes often form cycles, but our approach naturally handles this. Even if a route loops back on itself, we only update our estimates if we find a path with fewer buses.

4. **Efficiency**: While we may need to iterate multiple times, each iteration potentially improves our estimates for multiple stops simultaneously. This is generally more efficient than exploring paths one at a time.

5. **Adaptability**: This approach can easily handle various network structures, whether the bus system is sparse or dense, tree-like or heavily interconnected.

## Time and Space Complexity

Let's analyze the time and space complexity of our solution:

**Time Complexity**: 
- In the worst case, we might need to iterate through all routes for each possible number of bus changes. 
- The number of iterations is bounded by the number of routes, as we can't use more buses than there are routes.
- Within each iteration, we examine each stop on each route.
- Therefore, the time complexity is O(N * M), where N is the total number of stops across all routes, and M is the number of routes.

**Space Complexity**:
- Our main data structure is the `minBusesToReach` array, which has a size equal to the maximum bus stop number plus one.
- Therefore, the space complexity is O(K), where K is the maximum bus stop number.

This analysis shows that our solution is efficient in terms of both time and space, scaling well with the size of the input.

## Conclusion

The bus route problem is a fascinating example of how graph theory and dynamic programming concepts can be applied to real-world optimization challenges. Our solution demonstrates the power of iterative improvement algorithms, where we start with a simple initial state and progressively refine our solution until we reach optimality.

Key takeaways from this approach include:
1. The importance of proper problem modeling (viewing bus stops as nodes and routes as edges in a graph).
2. The effectiveness of the relaxation principle in finding shortest paths.
3. The value of maintaining and updating global state (our `minBusesToReach` array) throughout the solution process.

By understanding this solution deeply, we gain insights that can be applied to a wide range of network optimization problems, from transportation planning to data routing in computer networks.

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


## From Iteration to Bidirectional Search

In our previous discussion, we explored an iterative relaxation approach to solving the bus route problem. While that method was intuitive and comprehensive, it had some limitations, particularly when dealing with large networks. As we delve deeper into the problem, let's explore how our thinking evolved, leading us to a more efficient solution.

## Revisiting the Challenge

Recall that we're trying to find the minimum number of bus changes required to get from a source stop to a target stop in a complex bus network. Our previous approach treated this as a graph problem, using an iterative method to explore all possible paths. While this method guaranteed finding the optimal solution, it could be inefficient for large networks.

## The Evolution of Our Approach

### Step 1: Recognizing the Need for Efficiency

Our first "aha" moment came when we realized that our initial approach, while thorough, was potentially examining many irrelevant paths. In a large city with hundreds of bus routes and thousands of stops, we might be wasting time exploring areas of the network far from both our source and target.

Question we asked ourselves: "How can we focus our search on the most relevant parts of the network?"

### Step 2: Introducing Breadth-First Search (BFS)

This question led us to consider a Breadth-First Search (BFS) approach. BFS explores a graph level by level, which aligns perfectly with our goal of finding the path with the fewest bus changes.

Key Insight: Each "level" in our BFS corresponds to one bus change. By exploring in this manner, we ensure that we find the shortest path (in terms of bus changes) as soon as we reach our target.

### Step 3: The Bidirectional Breakthrough

While BFS was an improvement, we had another crucial realization: we don't just know our starting point; we also know our destination. This led to our most significant breakthrough – the idea of bidirectional search.

Analogy: Imagine you're trying to find a path through a maze. You could start at the entrance and explore until you find the exit. But what if you could also start at the exit and work backwards? You'd likely find the path much faster by meeting in the middle.

## The Bidirectional BFS Approach

Let's break down this new approach and understand why it's superior:

1. **Two-Pronged Exploration**: We start our search from both the source and the target simultaneously. This dramatically reduces the search space.

2. **Meeting in the Middle**: We're looking for the point where our two searches intersect. This point represents the optimal path from source to target.

3. **Efficient Space Coverage**: By exploring from both ends, we cover the most relevant parts of the network much faster than a single-direction search.

Mathematical Insight: The time complexity of BFS is O(b^d), where b is the branching factor (average number of next stops from each stop) and d is the depth (number of bus changes). In bidirectional search, we're essentially reducing this to O(b^(d/2) + b^(d/2)), which is significantly smaller than O(b^d) for large d.

## Key Components of the Solution

### 1. Building a Stop-to-Routes Map

One crucial optimization is preprocessing our data to create a map from stops to the routes that serve them. 

Question we asked: "How can we quickly find all routes that pass through a given stop?"

This map allows us to efficiently find all routes connected to a stop, which is essential for our bidirectional BFS.

### 2. Balancing the Two Searches

A key insight in our approach is always expanding the smaller frontier. 

Mathematical justification: By always expanding the smaller set, we minimize the total number of nodes explored. If one frontier is much larger than the other, it's more efficient to expand the smaller one, as it has a higher chance of quickly reaching the intersection point.

### 3. Tracking Visited Routes

To avoid redundant exploration, we keep track of visited routes rather than visited stops. 

Logical reasoning: Once we've explored a route, we don't need to explore it again from a different stop. This significantly reduces the number of redundant explorations, especially in networks with long routes.

## Handling Edge Cases and Potential Pitfalls

1. **Source = Target**: We handle this trivial case right at the beginning, returning 0 if the source and target are the same.

2. **Disconnected Network**: If the source and target are in disconnected parts of the network, our bidirectional search will exhaust all possibilities without finding an intersection. We return -1 in this case.

3. **Single-Stop Routes**: Our approach naturally handles routes with only one stop, as these will be represented in our stop-to-routes map just like any other route.

4. **Overlapping Routes**: Multiple routes serving the same stops are handled efficiently through our stop-to-routes map, ensuring we don't double-count or miss any connections.

## Mathematical Formulation

Let's formalize our bidirectional BFS approach:

1. Let S be the set of stops reachable from the source in i steps.
2. Let T be the set of stops reachable from the target in j steps.
3. We're looking for the minimum value of i + j such that S ∩ T ≠ ∅.

At each step, we expand the smaller of S or T, adding all stops reachable in one more bus change. This process continues until we find an intersection or exhaust all possibilities.

## Advantages of the Bidirectional BFS Approach

1. **Efficiency**: By searching from both ends, we dramatically reduce the search space, making the algorithm much faster for large networks.

2. **Optimality**: Like our previous approach, this method guarantees finding the optimal solution if one exists.

3. **Space Efficiency**: We only need to keep track of the current frontiers and visited routes, not the entire network state.

4. **Flexibility**: This approach can be easily adapted to handle additional constraints or optimize for different criteria.

5. **Scalability**: The bidirectional approach scales well with network size, making it suitable for very large bus systems.

## Conclusion: The Power of Perspective Shift

Our journey from an iterative relaxation approach to a bidirectional BFS showcases the power of shifting perspectives in problem-solving. By looking at the problem from both ends simultaneously, we transformed a potentially slow algorithm into a highly efficient solution.

This evolution in our approach demonstrates several key problem-solving principles:

1. **Question Assumptions**: Our initial assumption of needing to explore the entire network led to an inefficient solution. By questioning this, we opened the door to more targeted approaches.

2. **Leverage All Available Information**: Recognizing that we knew both the start and end points was crucial in developing our bidirectional approach.

3. **Balance Thoroughness and Efficiency**: While our first approach guaranteed finding a solution, our final approach maintains this guarantee while significantly improving efficiency.

4. **Preprocess Strategically**: Building the stop-to-routes map upfront saves considerable time during the actual search process.

As we move from this intuition to implementation, the key will be translating these concepts into efficient code while carefully handling the bidirectional search process and managing the frontiers effectively.

This evolved approach not only solves the bus route problem more efficiently but also provides a template for tackling similar network traversal problems in various domains, from transportation to social networks and beyond.
### Approach 2
# Comprehensive Explanation: Bidirectional BFS for Bus Route Problem

## Introduction

The bus route problem requires finding the minimum number of bus changes needed to travel from a source stop to a target stop in a complex bus network. Our solution employs a bidirectional Breadth-First Search (BFS) approach, which offers significant efficiency improvements over traditional single-direction BFS, especially for large networks.

## Core Algorithm: Bidirectional BFS

The heart of our solution is the bidirectional BFS algorithm. Let's break it down into its key components and understand the logic behind each part.

### 1. Preprocessing: Building the Stop-to-Routes Map

Before we begin our search, we preprocess the input data to create a map that allows us to quickly find all routes passing through a given stop.

```pseudo
function buildStopToRoutesMap(routes):
    stopToRoutes = empty map
    for i = 0 to length(routes) - 1:
        for stop in routes[i]:
            if stop not in stopToRoutes:
                stopToRoutes[stop] = empty set
            add i to stopToRoutes[stop]
    return stopToRoutes
```

This preprocessing step is crucial for the efficiency of our algorithm. It allows us to quickly find all routes connected to a given stop during our BFS, avoiding the need to search through all routes repeatedly.

**Time Complexity**: O(N), where N is the total number of stops across all routes.
**Space Complexity**: O(N), as in the worst case, each stop could be on every route.

### 2. Main Bidirectional BFS Algorithm

Now, let's look at the core bidirectional BFS algorithm:

```pseudo
function numBusesToDestination(routes, source, target):
    if source == target:
        return 0

    stopToRoutes = buildStopToRoutesMap(routes)
    
    sourceStops = set containing only source
    targetStops = set containing only target
    visitedRoutes = empty set
    steps = 0

    while sourceStops is not empty and targetStops is not empty:
        if size(sourceStops) > size(targetStops):
            swap sourceStops and targetStops

        nextStops = empty set
        steps = steps + 1

        for stop in sourceStops:
            for route in stopToRoutes[stop]:
                if route not in visitedRoutes:
                    add route to visitedRoutes
                    for nextStop in routes[route]:
                        if nextStop in targetStops:
                            return steps
                        add nextStop to nextStops

        sourceStops = nextStops

    return -1
```

Let's break down the key components of this algorithm:

#### Initialization
We start by handling the trivial case where the source and target are the same. Then, we initialize our search frontiers (`sourceStops` and `targetStops`), our set of visited routes, and a counter for the number of steps (bus changes).

#### The Main Loop
The core of the algorithm is a while loop that continues as long as both frontiers have stops to explore. In each iteration:

1. We choose to expand the smaller frontier. This is a crucial optimization that significantly reduces the search space.

2. We increment our step counter, representing one bus change.

3. We explore all stops in the current frontier:
   - For each stop, we look at all routes passing through it.
   - For each unvisited route, we mark it as visited and explore all stops on that route.
   - If any of these stops are in the opposite frontier, we've found a meeting point and can return the current number of steps.
   - Otherwise, we add these stops to the next frontier.

4. We update our current frontier to the new set of stops we've discovered.

If the loop completes without finding a meeting point, we return -1 to indicate no path was found.

## Mathematical and Logical Concepts

### 1. Graph Representation

Although we don't explicitly construct a graph, our problem can be viewed as a graph problem:
- Vertices: Bus stops
- Edges: Connections between stops served by the same route

Our stop-to-routes map effectively represents this graph in a format optimized for our bidirectional search.

### 2. Breadth-First Search Properties

BFS explores vertices in order of their distance from the starting point. In our context, this translates to exploring stops in order of the number of bus changes required to reach them. This property ensures that we find the path with the minimum number of bus changes.

### 3. Bidirectional Search Optimization

The bidirectional approach provides a significant speedup over traditional BFS. If d is the shortest path length, unidirectional BFS explores O(b^d) vertices, where b is the branching factor. Bidirectional BFS explores O(b^(d/2)) from each end, resulting in O(b^(d/2) + b^(d/2)) total vertices explored.

This is a substantial improvement because b^(d/2) + b^(d/2) << b^d for large d.

### 4. Set Operations for Efficiency

We use set data structures extensively in our algorithm:
- For quick membership tests (e.g., checking if a route has been visited)
- For efficient union operations (e.g., building the next frontier)
- For easy swapping of frontiers

These operations are typically O(1) or O(n) where n is the size of the set, which is generally much smaller than the total number of stops or routes.

## Key Design Decisions and Their Rationale

1. **Bidirectional Search**: By searching from both ends, we significantly reduce the search space. This is particularly effective when the source and target are far apart in a large network.

2. **Stop-to-Routes Map**: This precomputed map allows us to quickly find all routes passing through a stop. Without this, we'd need to search through all routes for each stop we explore, significantly increasing time complexity.

3. **Tracking Visited Routes**: We mark routes as visited, not individual stops. This is because once we've explored a route, we don't need to explore it again from a different stop. This significantly reduces redundant explorations.

4. **Expanding Smaller Frontier**: Always expanding the smaller frontier minimizes the total number of stops explored. This is because the smaller frontier has a higher chance of quickly reaching the intersection point.

5. **Set-based Operations**: Using sets for our frontiers and visited routes allows for efficient membership tests and updates, which are frequent operations in our algorithm.

## Edge Cases and How They're Handled

1. **Source = Target**: Handled at the beginning by returning 0.
2. **No Path Exists**: If the while loop completes without finding a path, we return -1.
3. **Single-Stop Routes**: Handled naturally by our stop-to-routes map.
4. **Multiple Routes Between Stops**: Handled efficiently through our stop-to-routes map, ensuring we don't double-count or miss any connections.

## Time and Space Complexity Analysis

**Time Complexity**: O(N * M), where N is the total number of stops across all routes, and M is the number of routes. In the worst case, we might need to explore all stops and check all routes for each stop.

**Space Complexity**: O(N), dominated by the stop-to-routes map. The visited routes set and frontiers are generally smaller than N.

## Conclusion

This bidirectional BFS approach offers an efficient solution to the bus route problem. By leveraging the properties of BFS and the optimization of bidirectional search, we can quickly find the minimum number of bus changes required, even in large, complex bus networks.

The key to this solution's efficiency lies in its strategic use of data structures (particularly the stop-to-routes map and set operations) and the bidirectional nature of the search. By always expanding the smaller frontier and marking entire routes as visited, we minimize redundant explorations and focus our search on the most promising areas of the network.

This approach demonstrates how classical graph algorithms can be adapted and optimized for specific problem domains, providing a template for solving similar network traversal problems in various fields beyond just transportation networks.

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
