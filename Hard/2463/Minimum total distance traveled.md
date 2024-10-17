```Java []

class Solution {
    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
        // Sort robots and factories
        Collections.sort(robot);
        Arrays.sort(factory, (a, b) -> Integer.compare(a[0], b[0]));
        
        int m = robot.size();
        long[] dp = new long[m + 1];
        Arrays.fill(dp, Long.MAX_VALUE / 2);
        dp[0] = 0;
        
        for (int[] f : factory) {
            int pos = f[0], limit = f[1];
            for (int i = m; i > 0; i--) {
                long cost = 0;
                for (int j = 1; j <= Math.min(i, limit); j++) {
                    cost += Math.abs(robot.get(i - j) - pos);
                    dp[i] = Math.min(dp[i], dp[i - j] + cost);
                }
            }
        }
        
        return dp[m];
    }
}
//KDS
```
