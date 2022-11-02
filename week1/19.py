A, B = input().split()

A_rev = A[2]+A[1]+A[0]
B_rev = B[2]+B[1]+B[0]

if int(A_rev) > int(B_rev) :
    print(int(A_rev))
else :
    print(int(B_rev))