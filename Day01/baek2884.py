#45분씩 일찍 알람 설정 원래 설정되어 있는 알람을 45분 앞서는 시간 
#10 10 -> 9 25
#0 30 -> 23 45
#23 40 -> 22 55
# H, M = map(int, input().split())

# if M < 45:
#     if H == 0:
#         H = 23
#         M += 60
#     else:
#         H -= 1
#         M += 60
# print(H, M-45)
h, m = map(int, input().split())
if m < 45:
    if h == 0:
        h += 23
        m += 60
    else:
        h -= 1
        m += 60
print(h , (m - 45))