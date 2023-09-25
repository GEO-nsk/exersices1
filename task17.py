'''
Задание 17.
Строка содержит арифметическое выражение, в котором используются круглые скобки,
в том числе вложенные. Напишите программу, которая вычисляет значение этого выражения.
Функцию eval() не использовать.
'''

ptr = str(input())

cnt_left = 0
cnt_right = 0
comma = 0
new_ptr = ''
flag = False

for i in ptr:
    new_ptr += i
    if i == '(':
        cnt_left += 1
        flag = True
    if i == ')':
        cnt_right += 1
    if flag:
        if cnt_left == cnt_right:
            flag = False
            while cnt_left != 0:
                for x in new_ptr:
                    if x == '(':
                        comma += 1

                cnt_left -= 1
            new_ptr = ''
