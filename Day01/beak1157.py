# str = input().upper()
# str_list = list(set(str))
# cnt = []

# for i in str_list:
#     count = str.count(i)
#     cnt.append(count)

# if cnt.count(max(cnt)) > 1:
#     print("?")
# else:
#     print(str_list[(cnt.index(max(cnt)))])
str = input().upper()
str_list = list(set(str))
cnt = []

for i in str_list:
    count = str.count(i)
    cnt.append(count)
if cnt.count(max(cnt) > 2):
    print("?")
else:
    print(str_list[cnt.index(max(cnt))])


str = input().upper()
str_list = sorted(str)
cnt = []

for i in str_list:
    count = str.count(i)
    cnt.append(count)
if cnt.count(max(cnt) > 2):
    print("?")    
else:
    print(str_list[cnt.index(max(cnt))])