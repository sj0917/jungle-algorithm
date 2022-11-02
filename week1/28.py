N, r, c = map(int, input().split())


def two_square(n) :   # 2의 N제곱 구하는 함수
    square = 1
    for _ in range(n) :
        square = square*2
    return square-1


def z(N, r, c) :
    if N > 1 :
        if r <= (two_square(N) + 1)/2 -1 and c <= (two_square(N) + 1)/2 -1 : 
            
            return z(N-1, r, c)

        if r <= (two_square(N) + 1)/2 -1 and c > (two_square(N) + 1)/2 -1 :
            c = c - (two_square(N) + 1)/2
            return ((two_square(N) + 1)/2)*((two_square(N) + 1)/2) + z(N-1, r, c)

        if r > (two_square(N) + 1)/2 -1 and c <= (two_square(N) + 1)/2 -1 :
            r = r - (two_square(N) + 1)/2
            return ((two_square(N) + 1)/2)*((two_square(N) + 1)/2)*2 + z(N-1, r, c)

        if r > (two_square(N) + 1)/2 -1 and c > (two_square(N) + 1)/2 -1 :
            r = r - (two_square(N) + 1)/2
            c = c - (two_square(N) + 1)/2
            return ((two_square(N) + 1)/2)*((two_square(N) + 1)/2)*3 + z(N-1, r, c)
    else : 
        if r == 0 and c == 0 :
            return 1
        if r == 0 and c == 1 :
            return 2
        if r == 1 and c == 0 :
            return 3
        if r == 1 and c == 1 :
            return 4

print(z(N, r, c)-1)
