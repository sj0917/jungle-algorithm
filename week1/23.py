N = int(input())

if N < 10 : 
    print(N)

elif 10 <= N < 100 :
    print(N - 1)

elif 100 <= N < 1000 :

    count = 0
    for i in range(100,N+1) :

        hundreds = int(str(i)[0])
        tens = int(str(i)[1])
        units = int(str(i)[2])        

        
        if hundreds + units == tens*2 :
            count += 1

    han = 99 + count
    print(han)

else :
    print(144)


