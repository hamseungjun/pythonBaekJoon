def calculate(cnt):
    temp = 0
    for _ in range(3):
        m , n = map(int, input().split())
        if m > n:
            i = 2
            while m > 1:
                if m % i == 0:
                    if i > temp:
                        temp = i
                        m = m //temp  
                    else:
                        i += 1
            print(temp * n)
        else:
            i = 2
            while n > 1:
                if n % i == 0:
                    if i > temp:
                        temp = i
                        n = n //temp  
                    else:
                        i += 1
            print(temp * n)    

cnt = int(input())
calculate(cnt)     
                    
                    
