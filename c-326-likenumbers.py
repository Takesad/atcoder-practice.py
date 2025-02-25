N = int(input())

def is_326_like_number(num):
    a = N // 100
    b = (num // 10) % 10
    c = num % 10

    return a * b == c

def find_next_326_like_number(N):
    num = N

    while not is_326_like_number(num):
        num += 1

    return num

result = find_next_326_like_number(N)

print(result)