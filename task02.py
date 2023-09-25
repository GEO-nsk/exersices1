'''
Задание 2.
Дан текст. Необходимо определить максимальное количество последовательных одинаковых символов в нём.
'''
Text = str(input())
count = 1
s = []
for i in range(len(Text)-1):
    if Text[i] == Text[i+1]:
        count += 1
    else:
        s.append(k)
        count = 1
s.append(count)
print(max(s))