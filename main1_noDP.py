# 動的計画法を用いいない単純な深さ優先探索

n = int(input())
wv = list(map(int, input().split()))
w, v = wv[0::2], wv[1::2]
W = int(input())

def rec(index, w_limit):

    # 終了条件(全ての品物を探索した)
    if index == n:
        # 木構造の末端で呼ばれる(つまりはじめに返される初期値)
        return 0

    # 品物が入らない
    if w_limit < w[index]:
        return rec(index+1, w_limit)

    # 品物を入れない場合、品物を入れる場合の両方を試す
    else:
        return max(rec(index+1,w_limit), rec(index+1, w_limit - w[index]) + v[index])

print(rec(0,W))