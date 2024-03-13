str = list(input())
result = []
temp = []
for i in range(1, len(str)-1):
    for j in range(i+1, len(str)):
        a = str[:i]
        b = str[i:j]
        c = str[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        temp.append(a + b +c)
for a in temp:
    result.append(''.join(a))
print(sorted(result)[0])
