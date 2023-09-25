'''
Задание 6.
Дано предложение. Напечатать его в обратном порядке слов.
'''

ptr = str(input())

new_str = ''

for i in ptr.split():
    i = i[::-1]
    new_str = new_str + i
    new_str = new_str + ' '

new_str = new_str[0:-1]
print(new_str[::-1])