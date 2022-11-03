import sys

N = int(sys.stdin.readline())

number = [0] * 10001

for _ in range(N) : 
    number[int(sys.stdin.readline())] += 1
   

for i in range(10001) :
    if number[i] != 0 :
        for n in range(number[i]) :
            print(i)