T = int(input())
for _ in range(T):
    N = int(input())
    max_school = ""
    max_bottle = 0
    for _ in range(N):
        school_name, bottle = input().split()
        bottle = int(bottle)
        if max_bottle < bottle:
            max_bottle = bottle 
            max_school = school_name
    print(max_school)    
    

        
        