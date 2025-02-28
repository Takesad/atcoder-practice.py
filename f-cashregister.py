S = input().strip()

ans = 0
while S:
    back = S[-1]
    S = S[:-1]  # 最後の文字を取り除く
    if back == '0' and S and S[-1] == '0':
        # S が 100 の倍数なら、さらに 1 文字消す
        S = S[:-1]
    ans += 1

print(ans)