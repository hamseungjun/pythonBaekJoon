word = input()

reverseList = list(word)
reverseList.reverse()
reverseWord = ''.join(reverseList)

if word == reverseWord:
    print(1)
elif word != reverseWord:
    print(0)

print(8 % 16)