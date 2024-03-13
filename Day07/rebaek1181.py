n = int(input())
lst = []
for _ in range(n):
    str = input()
    lst.append(str)
lst_set = set(lst)
lst = list(lst_set)
lst.sort()
lst.sort(key=len)
for k in lst:
    print(k)