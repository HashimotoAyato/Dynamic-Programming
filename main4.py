import numpy as np

n = int(input())
wv = list(map(int, input().split()))
w, v = wv[0::2], wv[1::2]
W = int(input())

MAX_V = n*100

dp = np.zeros((n+1, MAX_V+1))
dp[0,:] = np.inf
dp[0,0] = 0

for i in range(n):
    for j in range(MAX_V+1):
        if j < v[i]:
            dp[i+1, j] = dp[i, j]
        else:
            dp[i+1, j] = min(dp[i, j], dp[i, j-v[i]] + w[i])

ans = 0
for i in range(MAX_V):
    if dp[n][i] <= W:
        ans = i
    
print(dp[:,:10])
print("ans = {}".format(ans))