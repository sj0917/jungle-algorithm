N = int(input())

if N == 0 :
    print(1)

else: 
    N_fac = N
    for i in range(1, N) :
        N_fac = N_fac * (N - i)

    print(N_fac)