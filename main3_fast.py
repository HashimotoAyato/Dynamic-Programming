import numpy as np

n = int(input())
wv = list(map(int, input().split()))
w, v = wv[0::2], wv[1::2]
W = int(input())

dp = np.zeros((n+1, W+1), dtype=int)

for i in range(n):
    for j in range(W+1):
        if j < w[i]:
            dp[i+1, j] = dp[i, j]
        else:
            dp[i+1, j] = max(dp[i, j], dp[i+1, j-w[i]] + v[i])

print(dp)
print(dp[n,W])