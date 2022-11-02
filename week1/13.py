case_count = int(input())
for _ in range(case_count) :
    case = list(map(int, input().split()))
    
    sum = 0
    for score in case :
        sum = sum + score
    average = (sum-case[0]) / case[0]
    
    count = 0
    for score in case :
        if score > average :
            count += 1
    
    if case[0] > average :
        count = count - 1
    
    student = case[0]   
    stu_per = count / student * 100 

    print(format(stu_per, ".3f") + '%')
