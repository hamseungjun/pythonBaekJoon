# 1/1
# 1/2, 2/1
# 3/1, 2/2, 1/3
# 1/4, 2/3, 3/2, 4/1
# 5/1, 4/2, 3/3, 2/4, 1/5
# 
line = 1
n = int(input())
while n > line:
    n -= line 
    line += 1

if line%2 == 0:
    a = n
    b = line - n +1
elif line % 2 == 1:
    a = line - n +1
    b = n

print(f'{a}/{b}')