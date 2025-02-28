from collections import Counter

def max_pyramid_size(N, A):
    # 項目のカウント
    counter = Counter(A)
    
    # ピラミッド数列の最大サイズを求める二分探索
    left, right = 1, N
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        needed = [0] * (mid + 1)
        
        # 必要な数のカウント
        for num, count in counter.items():
            if num <= mid:
                needed[num] += count
        
        # ピラミッド数列が作れるか判定
        possible = True
        for i in range(1, mid):
            if needed[i] < 1:
                possible = False
                break
        if possible:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result
