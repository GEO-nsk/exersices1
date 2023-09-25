'''
Задание 9.
Дано предложение. В нем только два слова одинаковые. Найти эти слова.
'''

ptr = str(input())

s = []

for i in ptr.split():
    s.append(i)


for i in range(len(s)):
    for x in range(i+1,len(s)):
        if s[i] == s[x]:
            print(s[i])
