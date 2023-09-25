'''
Задание 7.
Дано предложение. Найти длину его самого короткого слова.
'''

ptr = str(input())

cnt = 10000000

for i in ptr.split():
    if cnt > len(i):
        cnt = len(i)

