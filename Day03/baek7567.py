# 입력
# 첫 줄에는 괄호문자로만 이루어진 문자열이 주어진다. 입력 문자열에서 열린 괄호 ‘(’은 바로 놓인 그릇, 닫힌 괄호 ‘)’
# 은 거꾸로 놓인 그릇을 나타난다. 문자열의 길이는 3이상 50 이하이다.

# 출력
# 여러분은 그릇 방향이 괄호 문자로 표시된 문자열을 읽어서 그 최종의 높이를 정수로 출력해야 한다.

bowl = input()
bowl_list = list(bowl)
sum = 0
bowlTemp = ''
for b in bowl_list:
    if b == bowlTemp:
        sum += 5
        bowlTemp = b
    elif b != bowlTemp:
        sum += 10
        bowlTemp = b 

print(sum)