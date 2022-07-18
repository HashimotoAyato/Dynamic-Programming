import numpy as np

n = int(input())
a = list(map(int, input().split()))

# a[i]で終わる部分列の最長の長さ
dp = np.zeros(n, int)
ans = 0
for i in range(n):
    # a[i]のみからなる部分列
    dp[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    ans = max(ans, np.max(dp))
        
print(ans)