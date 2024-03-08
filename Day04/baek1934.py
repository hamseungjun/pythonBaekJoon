N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    list_a = []
    list_b = []
    result = 0
    for i in range(2, a+1):
        if a % i == 0:
            list_a.append(i)
    for i in range(2, b+1):
        if b % i == 0:
            list_b.append(i)
    print(list_a)
    print(list_b)
    for i in list_a:
        for j in list_b:
            if i*j % b == 0 and i*j % a == 0:
                result = i * j  
        print(result)
    