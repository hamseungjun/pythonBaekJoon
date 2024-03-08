n = int(input())
result = input()

result_arr = list('d' for i in range(n))
result_arr = list(result)

resultA = result_arr.count('A')
resultB = result_arr.count('B')

if resultA > resultB:
    print('A')
elif resultB > resultA:
    print('B')
elif resultA == resultB:
    print('Tie')
else:
    print('you fucking wrong insert')



