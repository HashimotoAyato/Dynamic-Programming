import numpy as np

n, m, M = map(int, input().split())

# iのj分割
dp = np.zeros((n+1, m+1), int)
dp[0,0] = 1

for i in range(n+1):
    for j in range(1,m+1):
        if i < j:
            dp[i,j] = dp[i,j-1]
        else:
            dp[i,j] = dp[i-j][j] + dp[i,j-1]

print(dp)
print(dp[n,m])
