# 漸化式を用いた動的計画法

n = int(input())
wv = list(map(int, input().split()))
w, v = wv[0::2], wv[1::2]
W = int(input())
# DP用メモリ(未探索フラグ-1で初期化)
dp = [[0 for i in range(W+1)] for j in range(n+1)]

for i in reversed(range(n)):
    for j in range(W+1):
        if j < w[i]:
            dp[i][j] = dp[i+1][j]
        else:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j-w[i]]+v[i])

print(dp[0][W])