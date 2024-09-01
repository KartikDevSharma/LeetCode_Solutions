```Python []
class Solution:
    def numBusesToDestination(self, busRoutes: List[List[int]], start: int, end: int) -> int:
        if start == end:
            return 0
        
        max_bus_stop = self.find_max_bus_stop(busRoutes)
        if max_bus_stop < end or start > max_bus_stop or end > max_bus_stop:
            return -1
        
       
        stop_to_routes = defaultdict(set)
        for route_index, route in enumerate(busRoutes):
            for stop in route:
                stop_to_routes[stop].add(route_index)
        
    
        queue = deque([(start, 0)])  
        visited_stops = set()
        visited_routes = set()
        
        while queue:
            current_stop, buses_taken = queue.popleft()
            if current_stop == end:
                return buses_taken
            
          
            for route_index in stop_to_routes[current_stop]:
                if route_index in visited_routes:
                    continue
                visited_routes.add(route_index)
                for next_stop in busRoutes[route_index]:
                    if next_stop in visited_stops:
                        continue
                    visited_stops.add(next_stop)
                    queue.append((next_stop, buses_taken + 1))
        
        return -1
    
    def find_max_bus_stop(self, routes):
        return max(max(route) for route in routes)




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
```C++ []

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
