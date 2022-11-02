case_count = int(input())
for case in range(case_count) : 
    case = input()
    i = 0
    count = 0
    rep = 0
    for score in case :
        if score == "O" and score == case[count+1] :
            rep += 1
            i = i + rep + 1
            count += 1
        elif score == "O" :
            i = i + 1
            rep = 0
            count += 1
        else : 
            rep = 0
            count += 1
            
    print(i)
    
       
    
