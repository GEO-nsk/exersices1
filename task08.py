'''
Задание 8.
Дано предложение. Напечатать все его слова в порядке неубывания их длин.
'''

ptr = str(input())

s = []
cnt = 11110
word = ''

for i in ptr.split():
    s.append(i)

for x in range(len(s)):
    for i in s:
        if cnt >= len(i):
            word = i
            cnt = len(i)
    s.pop(s.index(word))
    print(word)
    cnt = 100000