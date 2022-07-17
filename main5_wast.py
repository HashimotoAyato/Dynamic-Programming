# 無駄の多い解法

import numpy as np

n = int(input()) # 数の種類
a = list(map(int, input().split())) # n個の数
m = list(map(int, input().split())) # aがそれぞれ何個あるか
K = int(input()) # 目標の総和

dp = np.zeros((n+1, K+1), bool) # DPテーブル(jが作れるか)
dp[0,0] = True
for i in range(n):
    for j in range(K+1):
        for k in range(m[i]+1):
            if k * a[i] <= j:
                dp[i+1, j] = dp[i+1, j] or dp[i, j-k*a[i]]
            
print(dp)
print('ans = {}'.format(dp[n,K]))