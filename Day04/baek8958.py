N = int(input())

for i in range(N):
    str = input()
    score = 0
    score_sum = 0
    for j in str:
        if j == "O":
            score +=1
        else:
            score = 0
        score_sum += score 
    print(score_sum)
    