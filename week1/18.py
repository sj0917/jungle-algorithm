str = input()

count = 0
for alphabet in str :
    if alphabet == ' ' :
        count += 1

if str[0] == ' ' :
    count = count - 1

if not str[len(str)-1] == ' ' :
    count = count + 1

print(count)