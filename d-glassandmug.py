K, G, M = map(int, input.split()) # 入力を一行で受け取る

a, b = 0, 0
# a = グラスの水量
# b = マグカップの水量

for i in range(K):
    if a == G: # グラスが満杯なら空にする
        a = 0

    elif b == 0: # マグカップが空なら満杯にする
        b = M

    else:
        transfer = min(G - a, b) # グラスが満杯になるか、マグカップが空になるまで水を移す
        a += transfer
        b -= transfer

print(a, b)