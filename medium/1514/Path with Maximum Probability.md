Approach 1
```Java []
class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        vector<double> prob(n, 0.0);
        prob[start_node] = 1.0;
        
        int i = 0;
        while (i < n - 1) {
            bool updated = false;
            int j = 0;
            while (j < edges.size()) {
                int a = edges[j][0], b = edges[j][1];
                double p = succProb[j];
                
                switch (prob[a] * p > prob[b]) {
                    case true:
                        prob[b] = prob[a] * p;
                        updated = true;
                        break;
                    case false:
                        switch (prob[b] * p > prob[a]) {
                            case true:
                                prob[a] = prob[b] * p;
                                updated = true;
                                break;
                        }
                        break;
                }
                j++;
            }
            switch (updated) {
                case false:
                    goto end_loop;
            }
            i++;
        }
        end_loop:
        
        return prob[end_node];
    }
};
```
```C++ []
class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        vector<double> prob(n, 0.0);
        prob[start_node] = 1.0;
        
        int i = 0;
        while (i < n - 1) {
            bool updated = false;
            int j = 0;
            while (j < edges.size()) {
                int a = edges[j][0], b = edges[j][1];
                double p = succProb[j];
                
                switch (prob[a] * p > prob[b]) {
                    case true:
                        prob[b] = prob[a] * p;
                        updated = true;
                        break;
                    case false:
                        switch (prob[b] * p > prob[a]) {
                            case true:
                                prob[a] = prob[b] * p;
                                updated = true;
                                break;
                        }
                        break;
                }
                j++;
            }
            switch (updated) {
                case false:
                    goto end_loop;
            }
            i++;
        }
        end_loop:
        
        return prob[end_node];
    }
};
static const int ktkdvshrm = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();
```
```Python []
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        prob = [0.0] * n
        prob[start_node] = 1.0
        
        i = 0
        while i < n - 1:
            updated = False
            j = 0
            while j < len(edges):
                a, b = edges[j]
                p = succProb[j]
                
                if prob[a] * p > prob[b]:
                    prob[b] = prob[a] * p
                    updated = True
                elif prob[b] * p > prob[a]:
                    prob[a] = prob[b] * p
                    updated = True
                
                j += 1
            
            if not updated:
                break
            
            i += 1
        
        return prob[end_node]

def main():
    inputs = map(loads, sys.stdin)
    results = []

    while True:
        try:
            n = next(inputs)
            edges = next(inputs)
            succProb = next(inputs)
            start_node = next(inputs)
            end_node = next(inputs)
            
            result = Solution().maxProbability(n, edges, succProb, start_node, end_node)
            results.append(result)
        except StopIteration:
            break

    with open("user.out", "w") as f:
        for result in results:
            print(f"{result:.5f}", file=f)

if __name__ == "__main__":
    main()
    sys.exit(0)


```


Approach 2
```Java []
class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        double[] p = new double[n];
        p[start_node] = 1.0;
        Map<Integer, List<int[]>> g = new HashMap<>();
        PriorityQueue<double[]> heap = new PriorityQueue<>((a, b) -> Double.compare(b[0], a[0]));
        heap.offer(new double[]{1.0, start_node});
        
        for (int i = 0; i < edges.length; i++) {
            int a = edges[i][0], b = edges[i][1];
            g.computeIfAbsent(a, k -> new ArrayList<>()).add(new int[]{b, i});
            g.computeIfAbsent(b, k -> new ArrayList<>()).add(new int[]{a, i});
        }
        
        while (!heap.isEmpty()) {
            double[] curr = heap.poll();
            double prob = curr[0];
            int node = (int) curr[1];
            
            if (node == end_node) return prob;
            
            if (g.containsKey(node)) {
                for (int[] neighbor : g.get(node)) {
                    double newProb = prob * succProb[neighbor[1]];
                    if (newProb > p[neighbor[0]]) {
                        p[neighbor[0]] = newProb;
                        heap.offer(new double[]{newProb, neighbor[0]});
                    }
                }
            }
        }
        
        return 0.0;
    }
}


```
```C++ []
class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        vector<double> p(n, 0.0);
        p[start_node] = 1.0;
        unordered_map<int, vector<pair<int, int>>> g;
        priority_queue<pair<double, int>> heap;
        heap.push({1.0, start_node});
        
        for (int i = 0; i < edges.size(); ++i) {
            int a = edges[i][0], b = edges[i][1];
            g[a].push_back({b, i});
            g[b].push_back({a, i});
        }
        
        while (!heap.empty()) {
            auto [prob, node] = heap.top();
            heap.pop();
            
            if (node == end_node) return prob;
            
            for (auto [neighbor, i] : g[node]) {
                double new_prob = prob * succProb[i];
                if (new_prob > p[neighbor]) {
                    p[neighbor] = new_prob;
                    heap.push({new_prob, neighbor});
                }
            }
        }
        
        return 0.0;
    }
};

static const int ktkdvshrm = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();

```
```Python []
def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    p = [0.0] * n
    p[start_node] = 1.0
    g = defaultdict(list)
    heap = [(-1.0, start_node)]
    
    for i, (a, b) in enumerate(edges):
        g[a].append((b, i))
        g[b].append((a, i))
    
    while heap:
        prob, node = heapq.heappop(heap)
        if node == end_node:
            return -prob
        
        for neighbor, i in g[node]:
            new_prob = -prob * succProb[i]
            if new_prob > p[neighbor]:
                p[neighbor] = new_prob
                heapq.heappush(heap, (-new_prob, neighbor))
    
    return 0.0

def main():
    with open("user.out", "w") as sys.stdout:
        inputs = zip(*[map(loads, sys.stdin)] * 5)
        for params in inputs:
            result = maxProbability(*params)
            print(f"{result:.5f}")

if __name__ == "__main__":
    main()
    sys.exit(0)

```
