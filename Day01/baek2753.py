#윤년은 연도가 4의 배우이면서(&&) 100의 배수가 아니고 400의 배수일때
year = int(input())  #윤년이면 1 아니면 0 출력
if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(1)
else:
    print(0)