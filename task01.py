'''
Задание 1.
Дан текст. Необходимо определить максимальное количество последовательных пробельных символов  в нём.
'''
s = []
count = 0

Text = str(input())

for i in Text:
    if i == ' ' or i == '\t':
        count+=1
    else:
        s.append(count)
        k = 0

print(max(s))