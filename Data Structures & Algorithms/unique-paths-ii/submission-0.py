class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        dp[1][1] = 1

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if i == 1 and j == 1:
                    continue
                if obstacleGrid[i-1][j-1]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[rows][cols]