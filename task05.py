'''
Задание 5.
Даны три строки. Выведите на экран только те символы, которые есть лишь в одной из этих трёх строк.
'''

str1 = str(input())
str2 = str(input())
str3 = str(input())

for i in str1:
    if i not in str2 and i not in str3:
        print(i)

for i in str2:
    if i not in str1 and i not in str3:
        print(i)

for i in str3:
    if i not in str2 and i not in str1:
        print(i)