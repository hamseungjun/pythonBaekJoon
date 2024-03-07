# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
diceArr = list(map(int, input().split()))
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
     
print(reward)

