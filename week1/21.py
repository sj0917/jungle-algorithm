N = int(input())
N_list = list(input().split())

decimal_count = 0
for i in N_list :
    count = 0
    number = int(i)
    for n in range(number) :
        if int (number/(n+1)) == number/(n+1) :
            count += 1
    if count == 2 :
        decimal_count += 1

print(decimal_count)