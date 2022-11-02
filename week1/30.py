N = int(input())

number = [None] * N

for i in range(len(number)) :
    number[i] = int(input())

list.sort(number) 

for i in range(len(number)) :
    print(number[i])