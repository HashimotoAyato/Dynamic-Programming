import numpy as np

n, m = map(int, input().split())
s = list(input())
t = list(input())

dp = np.zeros((n+1, m+1), dtype=int)

for i in range(n):
    for j in range(m):
        # 互いの探索範囲の末尾が同じ文字である場合
        if s[i] == t[j]:
            dp[i+1, j+1] = dp[i,j] + 1
        else:
            dp[i+1, j+1] = max(dp[i,j+1], dp[i+1,j])

print(dp[n][m])