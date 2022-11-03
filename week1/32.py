N = int(input())

word = [None] * N

for i in range(len(word)) :
    word[i] = input()

word.sort()                 # 사전 순으로 정렬하기

for _ in range(len(word)) :                     # 길이 순으로 정렬하기
    for i in range(len(word) - 1) :
        if len(word[i]) > len(word[i + 1]) :
            word[i], word[i + 1] = word[i + 1], word[i]

word_length = len(word)
            
for i in range(word_length - 1) :                   # 중복 단어 삭제       
    if word[word_length - i - 2] == word[word_length - i -1] :
        del(word[word_length - i - 1])
    

for i in word :
    print(i)