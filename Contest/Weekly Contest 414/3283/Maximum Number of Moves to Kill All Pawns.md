```Java []
class Solution {
    private static final int[][] KNIGHT_MOVES = {{1,2},{2,1},{2,-1},{1,-2},{-1,-2},{-2,-1},{-2,1},{-1,2}};
    private static final int BOARD_SIZE = 50;
    private int[][] distances;
    private int[][] pawns;
    private int[][] memo;

    public int maxMoves(int kx, int ky, int[][] positions) {
        pawns = new int[positions.length + 1][2];
        System.arraycopy(positions, 0, pawns, 0, positions.length);
        pawns[positions.length] = new int[]{kx, ky};
        
        precomputeDistances();
        memo = new int[1 << pawns.length][pawns.length];
        for (int[] row : memo) Arrays.fill(row, -1);
        
        return dp(0, pawns.length - 1);
    }

    private void precomputeDistances() {
        distances = new int[pawns.length][pawns.length];
        for (int i = 0; i < pawns.length; i++) {
            int[] dist = bfs(pawns[i][0], pawns[i][1]);
            for (int j = 0; j < pawns.length; j++) {
                distances[i][j] = dist[pawns[j][0] * BOARD_SIZE + pawns[j][1]];
            }
        }
    }

    private int[] bfs(int startX, int startY) {
        int[] dist = new int[BOARD_SIZE * BOARD_SIZE];
        Arrays.fill(dist, -1);
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(startX * BOARD_SIZE + startY);
        dist[startX * BOARD_SIZE + startY] = 0;

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            int x = curr / BOARD_SIZE, y = curr % BOARD_SIZE;

            for (int[] move : KNIGHT_MOVES) {
                int nx = x + move[0], ny = y + move[1];
                if (nx >= 0 && nx < BOARD_SIZE && ny >= 0 && ny < BOARD_SIZE && dist[nx * BOARD_SIZE + ny] == -1) {
                    dist[nx * BOARD_SIZE + ny] = dist[curr] + 1;
                    queue.offer(nx * BOARD_SIZE + ny);
                }
            }
        }
        return dist;
    }

    private int dp(int mask, int last) {
        if (mask == (1 << (pawns.length - 1)) - 1) return 0;
        if (memo[mask][last] != -1) return memo[mask][last];

        boolean isAliceTurn = Integer.bitCount(mask) % 2 == 0;
        int result = isAliceTurn ? 0 : Integer.MAX_VALUE;

        for (int i = 0; i < pawns.length - 1; i++) {
            if ((mask & (1 << i)) == 0) {
                int newMask = mask | (1 << i);
                int moveCount = dp(newMask, i) + distances[last][i];
                
                if (isAliceTurn) {
                    result = Math.max(result, moveCount);
                } else {
                    result = Math.min(result, moveCount);
                }
            }
        }

        memo[mask][last] = result;
        return result;
    }
}
```
```C++ []
class Solution {
private:
    static const int KNIGHT_MOVES[8][2];
    static const int BOARD_SIZE = 50;
    std::vector<std::vector<int>> distances;
    std::vector<std::vector<int>> pawns;
    std::vector<std::vector<int>> memo;

public:
    int maxMoves(int kx, int ky, std::vector<std::vector<int>>& positions) {
        pawns = positions;
        pawns.push_back({kx, ky});
        
        precomputeDistances();
        memo = std::vector<std::vector<int>>(1 << pawns.size(), std::vector<int>(pawns.size(), -1));
        
        return dp(0, pawns.size() - 1);
    }

private:
    void precomputeDistances() {
        distances.resize(pawns.size(), std::vector<int>(pawns.size()));
        for (int i = 0; i < pawns.size(); i++) {
            std::vector<int> dist = bfs(pawns[i][0], pawns[i][1]);
            for (int j = 0; j < pawns.size(); j++) {
                distances[i][j] = dist[pawns[j][0] * BOARD_SIZE + pawns[j][1]];
            }
        }
    }

    std::vector<int> bfs(int startX, int startY) {
        std::vector<int> dist(BOARD_SIZE * BOARD_SIZE, -1);
        std::queue<int> queue;
        queue.push(startX * BOARD_SIZE + startY);
        dist[startX * BOARD_SIZE + startY] = 0;

        while (!queue.empty()) {
            int curr = queue.front();
            queue.pop();
            int x = curr / BOARD_SIZE, y = curr % BOARD_SIZE;

            for (const auto& move : KNIGHT_MOVES) {
                int nx = x + move[0], ny = y + move[1];
                if (nx >= 0 && nx < BOARD_SIZE && ny >= 0 && ny < BOARD_SIZE && dist[nx * BOARD_SIZE + ny] == -1) {
                    dist[nx * BOARD_SIZE + ny] = dist[curr] + 1;
                    queue.push(nx * BOARD_SIZE + ny);
                }
            }
        }
        return dist;
    }

    int dp(int mask, int last) {
        if (mask == (1 << (pawns.size() - 1)) - 1) return 0;
        if (memo[mask][last] != -1) return memo[mask][last];

        bool isAliceTurn = __builtin_popcount(mask) % 2 == 0;
        int result = isAliceTurn ? 0 : INT_MAX;

        for (int i = 0; i < pawns.size() - 1; i++) {
            if ((mask & (1 << i)) == 0) {
                int newMask = mask | (1 << i);
                int moveCount = dp(newMask, i) + distances[last][i];
                
                if (isAliceTurn) {
                    result = std::max(result, moveCount);
                } else {
                    result = std::min(result, moveCount);
                }
            }
        }

        memo[mask][last] = result;
        return result;
    }
};

const int Solution::KNIGHT_MOVES[8][2] = {{1,2},{2,1},{2,-1},{1,-2},{-1,-2},{-2,-1},{-2,1},{-1,2}};


static const auto kds = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();
```
```Python []
class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        N, M = 50, 50
        MOVES = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        
        # Precompute distances
        @cache
        def bfs_distance(sx, sy):
            dist = [[-1] * M for _ in range(N)]
            dist[sx][sy] = 0
            queue = deque([(sx, sy)])
            while queue:
                x, y = queue.popleft()
                for dx, dy in MOVES:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
            return dist

        # Precompute all distances
        distances = {(x, y): bfs_distance(x, y) for x, y in positions + [(kx, ky)]}

        n = len(positions)
        ALL_CAPTURED = (1 << n) - 1

        @cache
        def dp(x: int, y: int, mask: int, is_alice: bool) -> int:
            if mask == ALL_CAPTURED:
                return 0
            
            best = float('-inf') if is_alice else float('inf')
            curr_dist = distances[(x, y)]

            for i, (px, py) in enumerate(positions):
                if mask & (1 << i):
                    continue
                
                moves = curr_dist[px][py]
                new_score = moves + dp(px, py, mask | (1 << i), not is_alice)
                
                if is_alice:
                    best = max(best, new_score)
                else:
                    best = min(best, new_score)

            return best

        return dp(kx, ky, 0, True)
```
