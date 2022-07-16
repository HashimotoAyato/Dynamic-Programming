import numpy as np

n = int(input())
wv = list(map(int, input().split()))
w, v = wv[0::2], wv[1::2]
W = int(input())

dp = np.zeros(W+1, dtype = 1)

for i in range(n):
    j = w[i]
    while j <= W:
        dp[j] = max(dp[j], dp[j-w[i]] + v[i])
        j += 1

print(dp)
print(dp[W])