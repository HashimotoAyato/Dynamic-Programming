import numpy as np

n, m = map(int, input().split())
a = list(map(int, input().split()))
M = int(input())

dp = np.zeros((n+1, m+1), int)

# 何も選ばないのみの1通り
dp[:,0] = 1
for i in range(n):
    for j in range(1,m+1):
        if j-1 >= a[i]:
            # 負の値にならないようにMを足している。
            dp[i+1, j] = (dp[i+1, j-1] + dp[i, j] - dp[i, j-1-a[i]] + M) % M
        else:
            dp[i+1, j] = (dp[i+1,j-1] + dp[i, j]) % M

print(dp)
print(dp[n,m])