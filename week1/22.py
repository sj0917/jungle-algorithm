import sys

T = int(sys.stdin.readline())

decimal = 0
for T_case in range(T) :
    n = int(sys.stdin.readline())
    n_split = int(n/2)
    for i in range(n_split) :

        
        for number in range(2, n_split-i) :
            if int((n_split-i)/(number)) == (n_split-i)/(number) :
                decimal = 0
            else :
                decimal = n_split-i

        
        for number in range(2, n-decimal) :
            if int((n-decimal)/number) == (n-decimal)/number :
                continue
            print(n-decimal)
            decimal_2 = n-decimal
            break
        break
        
    print(decimal, end='')
    print(' ' + str(decimal_2))