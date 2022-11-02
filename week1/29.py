N = int(input())

number = [None] * N

for i in range(len(number)) :
    number[i] = int(input())


for n in range(len(number)-1) :

    for i in range(len(number)-n-1) :
        if number[i] > number[i+1] :
            number[i], number[i+1] = number[i+1], number[i]

for i in number :
    print(i)