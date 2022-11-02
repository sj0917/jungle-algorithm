T = int(input())
for case in range(T):
    case = list(input().split())
    R = int(case[0])

    S = ""
    for chr in case[1] :
        
        a = chr*R
        S = S + a

    print(S)

