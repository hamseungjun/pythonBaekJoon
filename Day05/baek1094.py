# 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
# 만약, 위에서 자른 막대의 절반 중 하나를 버리고 남아있는 막대의 길이의 합이 X보다 크거나 같다면, 위에서 자른 막대의 절반 중 하나를 버린다.
# 이제, 남아있는 모든 막대를 풀로 붙여서 Xcm를 만든다.
X = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]
cnt = 0
for i in stick:
    if X >= i:
        cnt += 1
        X -= i
    if X == 0:
        break
print(cnt)