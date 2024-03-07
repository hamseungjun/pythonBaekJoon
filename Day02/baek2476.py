def diceFunction(diceArr):
    reward = 0
    for i in range(1, 7):
        if diceArr.count(i) == 3:
            reward = 10000 + (i*1000)
            break
        
        elif diceArr.count(i) == 2:
            reward = 1000 + (i * 100)
            break
        
        elif diceArr.count(i) == 1:
            reward = max(diceArr) * 100
        
    return reward

cnt = int(input())
temp = 0
for i in range(cnt):
    diceArr = list(map(int, input().split()))
    i = diceFunction(diceArr)
    if i > temp:
        temp = i

print(temp)
