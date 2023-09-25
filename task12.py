'''
Задание 12.
Как известно, имя в языке Python может содержать только латинские символы, цифры
и знак подчеркивания "_". При этом, имя не может начинаться с цифры и не может быть
ключевым словом. Напишите программу, которая проверяет введенную строку, может ли
она быть именем в языке Python.
'''
import keyword

ptr = str(input())

cnt = 0
len_name = len(ptr)


for i in ptr:
    if (ord(i) > 64 and ord(i) < 91) or (ord(i) > 96 and ord(i) < 123) or (ord(i) > 47 and ord(i) < 58) or (ord(i) == 95):
        cnt += 1

if keyword.iskeyword(ptr) == 0:
    if cnt == len_name:
        print('может')
else:
    print('не может')
print(cnt)