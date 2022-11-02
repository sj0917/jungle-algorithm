dwarf = [None]*9
seven_dwarf = [None]*7

sum = 0
for i in range(9) :   
    dwarf[i] = int(input())  #난쟁이 키 입력
    sum = sum + dwarf[i]    #난쟁이 키 합 구하기


for i in range(8) :
    sum_1 = sum
    sum_1 = sum_1 - dwarf[i]
    for n in range(i+1, 9) :
        sum_2 = sum_1
        sum_2 = sum_2 - dwarf[n]
        if sum_2 == 100 :
            fake_1 = dwarf[i]
            fake_2 = dwarf[n]

for i in range(len(dwarf)) :
    if dwarf[i] == fake_1 :
        dwarf[i] = 0
    elif dwarf[i] == fake_2 :
        dwarf[i] = 0

for n in range(len(dwarf)-1) :

    for i in range(len(dwarf)-n-1) :
        if dwarf[i] > dwarf[i+1] :
            dwarf[i], dwarf[i+1] = dwarf[i+1], dwarf[i]

for i in range(len(dwarf)-2) :
   print(dwarf[i+2])