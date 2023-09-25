'''
Задание 3.
Дан текст. Определить, сколько различных букв в нем.
'''

Text = str(input())

s = []

for i in Text:
    if (ord(i) > 64 and ord(i) < 91) or (ord(i) > 1039 and ord(i) < 1104) or (ord(i) > 96 and ord(i) < 123):
        if i not in s:
            s.append(i)

print(len(s))