N = int(input())
c  = s = 100
for i in range(N):
    a, b = map(int, input().split())
    if a>b:
        s -= a 
    elif a < b:
        c -= b 
print(c)
print(s)
