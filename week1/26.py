import sys  

sys.setrecursionlimit(10**8)

N = int(input())

def hanoi(N, i, n) -> None :
    count = 0
    if N > 1 :
        hanoi(N - 1, i, 6 - i - n) 
        print(i, n)
        hanoi(N - 1, 6 - i - n, n)

    else : 
        print(i, n)

def hanoi_count(N) :
    if N > 1 :
        return hanoi_count(N-1) * 2 + 1
    else : 
        return 1
    
if N > 20 : 
    print(hanoi_count(N))
else : 
    print(hanoi_count(N))
    hanoi(N, 1, 3)