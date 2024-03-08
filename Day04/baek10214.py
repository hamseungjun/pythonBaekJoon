T =int(input())
for i in range(T):
    yonsei_sum = 0
    korea_sum = 0
    for j in range(9):
        yonsei, korea = map(int, input().split())
        yonsei_sum += yonsei 
        yonsei_sum += korea 
    if yonsei_sum > korea_sum:
        print("Yonsei")
    elif yonsei_sum < korea_sum:
        print("Korea")
    else:
        print("draw")