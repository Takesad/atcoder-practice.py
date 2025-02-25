N = int(input())

if(N < 42):
    if(N < 10):
        print(f"AGC00{N}", end='')
    else:
        print(f"AGC0{N}", end='')

else:
        print(f"AGC0{N+1}", end='')