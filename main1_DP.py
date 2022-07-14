# 再帰関数を用いた動的計画法

n = int(input())
wv = list(map(int, input().split()))
w, v = wv[0::2], wv[1::2]
W = int(input())
# DP用メモリ(未探索フラグ0で初期化)
dp = [[0 for i in range(W+1)] for j in range(n+1)]

def rec(index, w_limit):
    global dp
    # すでに探索済みか
    if -1 < dp[index][w_limit]:
        return dp[index][w_limit]

    # 終了条件(全ての品物を探索した)
    if index == n:
        # 木構造の末端で呼ばれる(つまりはじめに返される初期値)
        dp[index][w_limit] = 0
        return dp[index][w_limit]

    # 品物が入らない
    if w_limit < w[index]:
        dp[index][w_limit] = rec(index+1, w_limit)
        return dp[index][w_limit]

    # 品物を入れない場合、品物を入れる場合の両方を試す
    else:
        dp[index][w_limit] = max(rec(index+1,w_limit), rec(index+1, w_limit - w[index]) + v[index])
        return dp[index][w_limit]

print(rec(0,W))