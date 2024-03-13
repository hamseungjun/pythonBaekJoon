lst = []
n = int(input())
for _ in range(n):
    str = input()
    lst.append(str)
set_list = set(lst)
lst = list(set_list)
lst.sort()
lst.sort(key=len)
for k in lst:
    print(k)