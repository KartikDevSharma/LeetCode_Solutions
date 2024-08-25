

# Complexity
- **Time complexity: O(N * M * K)**, where:

    N is the number of routes
M is the average number of stops per route
K is the number of iterations in the main loop (which is bounded by the number of routes in the worst case)

- **Space complexity:O(S)**, where S is the maximum bus stop number.


# Code

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
```cpp []
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
static const int speedup = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();


//https://leetcode.com/problems/bus-routes/submissions/1365454603/
```

```Python []
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
                min_buses_for_route = min(min_buses_to_reach[stop] for stop in route) + 1
                for stop in route:
                    if min_buses_to_reach[stop] > min_buses_for_route:
                        min_buses_to_reach[stop] = min_buses_for_route
                        updated = True
        
        return min_buses_to_reach[end] if min_buses_to_reach[end] <= route_count else -1
    
    def find_max_bus_stop(self, routes):
        return max(max(route) for route in routes)

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
```JavaScript []
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
