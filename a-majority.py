N = int(input())
S = [input().strip() for _ in range(N)]

a, b = 0, 0

for i in range(N):
    if S[i] == "For":
        a += 1
    else:
        b += 1

if a > b:
    print("Yes")
else:
    print("No")