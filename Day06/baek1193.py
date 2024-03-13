n = int(input())
a = 0
b = 1
for _ in range(n):
    if a == b:
        b += 1
        a = 1
    elif a < b:
        a += 1     
print(a, "/", b)