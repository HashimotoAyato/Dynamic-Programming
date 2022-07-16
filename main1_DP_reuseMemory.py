# For文が順方向となるような解法

import numpy as np

n = int(input())
wv = list(map(int, input().split()))
w, v = wv[0::2], wv[1::2]
W = int(input())

dp = np.zeros((W+1), dtype = int)

for i in range(n):
    # 同じ品物を複数入れないよう後ろからループ
    for j in range(W,w[i]-1,-1):
        dp[j] = max(dp[j], dp[j-w[i]]+v[i])

print(dp[W])