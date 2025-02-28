def is_palindrome(n):
    return str(n) == str(n)[::-1]  # 文字列で回文判定

def largest_palindromic_cube(N):
    max_cube = 0
    x = 1
    while (cube := x ** 3) <= N:  # 立方数を計算しながら探索
        if is_palindrome(cube):   # 回文なら最大値を更新
            max_cube = cube
        x += 1
    return max_cube

# 入力を受け取る
N = int(input())
print(largest_palindromic_cube(N))