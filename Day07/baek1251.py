word = list(input()) #mobitel
answer = []
temp = []

for i in range(1, len(word) - 1): #1~ 6
    for j in range(i+1, len(word)): #2~7
        a = word[:i] #1 a = m 
        b = word[i:j]#1~2 = b
        c = word[j:] #2~  = bitel
        a.reverse() # oa
        b.reverse() #bo
        c.reverse() #itel
        temp.append(a + b + c) # temp = [oa, bo, itel]
        
for a in temp:
    answer.append(''.join(a))

print(sorted(answer)[0])