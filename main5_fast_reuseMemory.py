# DPデーブルに

import numpy as np

n = int(input()) # 数の種類
a = list(map(int, input().split())) # n個の数
m = list(map(int, input().split())) # aがそれぞれ何個あるか
K = int(input()) # 目標の総和

dp = np.zeros((K+1), int) # DPテーブル(jが作れない場合-1，作れる場合はa[i]の残りの個数)
dp[:] = -1
dp[0] = 0

for i in range(n):
    for j in range(K+1):
        if dp[j] >= 0:
            dp[j] = m[i]
        elif j < a[i] or dp[j-a[i]] <= 0:
            dp[j] = -1
        else:
            dp[j] = dp[j-a[i]] - 1
            
print(dp)
if dp[K] >= 0:
    print('True')
else:
    print('False')