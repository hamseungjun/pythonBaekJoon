num = int(input())
for _ in range(num):
    adv = list(map(int, input().split()))
    advAfter = adv[1] - adv[2]
    if advAfter > adv[0]:
        print("advertise")
    elif advAfter == adv[0]:
        print("does not matter")
    elif advAfter < adv[0]:
        print("do not advertise")