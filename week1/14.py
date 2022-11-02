A = int(input())
B = int(input())
C = int(input())
ABC = str(A*B*C)

for number in range(10) :

    count = 0
    for digit in ABC :
        if int(digit) == number :
            count += 1
    print(count)
