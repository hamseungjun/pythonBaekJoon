n = int(input())
arr = []
for i in range(n):
    rs = int(input())
    arr.append(rs)
cute = arr.count(1)
noCute = arr.count(0)
if cute > noCute:
    print('Junhee is cute!')
elif noCute > cute:
    print('Junhee is not cute!')