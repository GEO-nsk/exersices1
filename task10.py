'''
Задание 10.
Дано предложение. Выведите на экран те слова, которые отличны от первого слова,
и в слове нет повторяющихся букв.
'''
import sre_parse

ptr = str(input())

s = []
cnt = 0

for i in ptr.split():
    word = i
    break

for i in ptr.split():
    s.append(i)

for i in range(1,len(s)):
    if word != s[i]:
        for x in word:
            if x in s[i]:
                cnt += 1
        if cnt == 0:
            print(s[i])
        else:
            cnt = 0