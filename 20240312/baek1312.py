a, b, n =map(int, input().split()) #25, 7, 5
for _ in range(n):
    a = (a%b)*10    #a = 40
    result = a//b # result = 5

print(result)
