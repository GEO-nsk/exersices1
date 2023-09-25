'''
Задание 20.
Дано натуральное число не превосходящее 900 000 000. Напишите программу, которая
выводит на экран это число русскими словами.
'''

number = str(input())

ptr = ''

first_number1 = number[0:1]
first_number2 = number[1:2]
first_number3 = number[2:3]
second_number1 = number[3:4]
second_number2 = number[4:5]
second_number3 = number[5:6]
third_number1 = number[6:7]
third_number2 = number[7:8]
third_number3 = number[8:9]


if len(number) == 1:
    if number == '1':
        print('один')
    if number == '2':
        print('два')
    if number == '3':
        print('три')
    if number == '4':
        print('четыре')
    if number == '5':
        print('пять')
    if number == '6':
        print('шесть')
    if number == '7':
        print('семь')
    if number == '8':
        print('восем')
    if number == '9':
        print('девять')

if len(str(number)) == 2:
    if number == '11':
        print('одиннадцать')
    if number == '12':
        print('двеннадцать')
    if number == '13':
        print('треннадцать')
    if number == '14':
        print('четырнадцать')
    if number == '15':
        print('пятнадцать')
    if number == '16':
        print('шестнадцать')
    if number == '17':
        print('семнадцать')
    if number == '18':
        print('восемнадцать')
    if number == '19':
        print('девятнадцать')

    if first_number1 == '2':
        ptr = 'двадцать'
        if first_number2 == '1':
            print(ptr,'один')
        if first_number2 == '2':
            print(ptr,'два')
        if first_number2 == '3':
            print(ptr,'три')
        if first_number2 == '4':
            print(ptr,'четыре')
        if first_number2 == '5':
            print(ptr,'пять')
        if first_number2 == '6':
            print(ptr,'шесть')
        if first_number2 == '7':
            print(ptr,'семь')
        if first_number2 == '8':
            print(ptr,'восемь')
        if first_number2 == '9':
            print(ptr,'девять')
    if first_number1 == '3':
        ptr = 'тридцать'
        if first_number2 == '1':
            print(ptr, 'один')
        if first_number2 == '2':
            print(ptr, 'два')
        if first_number2 == '3':
            print(ptr, 'три')
        if first_number2 == '4':
            print(ptr, 'четыре')
        if first_number2 == '5':
            print(ptr, 'пять')
        if first_number2 == '6':
            print(ptr, 'шесть')
        if first_number2 == '7':
            print(ptr, 'семь')
        if first_number2 == '8':
            print(ptr, 'восемь')
        if first_number2 == '9':
            print(ptr, 'девять')
    if first_number1 == '4':
        ptr = 'сорок'
        if first_number2 == '1':
            print(ptr, 'один')
        if first_number2 == '2':
            print(ptr, 'два')
        if first_number2 == '3':
            print(ptr, 'три')
        if first_number2 == '4':
            print(ptr, 'четыре')
        if first_number2 == '5':
            print(ptr, 'пять')
        if first_number2 == '6':
            print(ptr, 'шесть')
        if first_number2 == '7':
            print(ptr, 'семь')
        if first_number2 == '8':
            print(ptr, 'восемь')
        if first_number2 == '9':
            print(ptr, 'девять')
    if first_number1 == '5':
        ptr = 'пятьдесят'
        if first_number2 == '1':
            print(ptr, 'один')
        if first_number2 == '2':
            print(ptr, 'два')
        if first_number2 == '3':
            print(ptr, 'три')
        if first_number2 == '4':
            print(ptr, 'четыре')
        if first_number2 == '5':
            print(ptr, 'пять')
        if first_number2 == '6':
            print(ptr, 'шесть')
        if first_number2 == '7':
            print(ptr, 'семь')
        if first_number2 == '8':
            print(ptr, 'восемь')
        if first_number2 == '9':
            print(ptr, 'девять')
    if first_number1 == '6':
        ptr = 'шестьдесят'
        if first_number2 == '1':
            print(ptr, 'один')
        if first_number2 == '2':
            print(ptr, 'два')
        if first_number2 == '3':
            print(ptr, 'три')
        if first_number2 == '4':
            print(ptr, 'четыре')
        if first_number2 == '5':
            print(ptr, 'пять')
        if first_number2 == '6':
            print(ptr, 'шесть')
        if first_number2 == '7':
            print(ptr, 'семь')
        if first_number2 == '8':
            print(ptr, 'восемь')
        if first_number2 == '9':
            print(ptr, 'девять')
    if first_number1 == '7':
        ptr = 'семьдесят'
        if first_number2 == '1':
            print(ptr, 'один')
        if first_number2 == '2':
            print(ptr, 'два')
        if first_number2 == '3':
            print(ptr, 'три')
        if first_number2 == '4':
            print(ptr, 'четыре')
        if first_number2 == '5':
            print(ptr, 'пять')
        if first_number2 == '6':
            print(ptr, 'шесть')
        if first_number2 == '7':
            print(ptr, 'семь')
        if first_number2 == '8':
            print(ptr, 'восемь')
        if first_number2 == '9':
            print(ptr, 'девять')
    if first_number1 == '8':
        ptr = 'восемьдесят'
        if first_number2 == '1':
            print(ptr, 'один')
        if first_number2 == '2':
            print(ptr, 'два')
        if first_number2 == '3':
            print(ptr, 'три')
        if first_number2 == '4':
            print(ptr, 'четыре')
        if first_number2 == '5':
            print(ptr, 'пять')
        if first_number2 == '6':
            print(ptr, 'шесть')
        if first_number2 == '7':
            print(ptr, 'семь')
        if first_number2 == '8':
            print(ptr, 'восемь')
        if first_number2 == '9':
            print(ptr, 'девять')
    if first_number1 == '9':
        ptr = 'девяносто'
        if first_number2 == '1':
            print(ptr, 'один')
        if first_number2 == '2':
            print(ptr, 'два')
        if first_number2 == '3':
            print(ptr, 'три')
        if first_number2 == '4':
            print(ptr, 'четыре')
        if first_number2 == '5':
            print(ptr, 'пять')
        if first_number2 == '6':
            print(ptr, 'шесть')
        if first_number2 == '7':
            print(ptr, 'семь')
        if first_number2 == '8':
            print(ptr, 'восемь')
        if first_number2 == '9':
            print(ptr, 'девять')

if len(str(number)) == 3:
    if first_number1 == '1':
        if first_number2 == '2':
            ptr = 'двадцать'
            if first_number2 == '1':
                print(ptr, 'один')
            if first_number2 == '2':
                print(ptr, 'два')
            if first_number2 == '3':
                print(ptr, 'три')
            if first_number2 == '4':
                print(ptr, 'четыре')
            if first_number2 == '5':
                print(ptr, 'пять')
            if first_number2 == '6':
                print(ptr, 'шесть')
            if first_number2 == '7':
                print(ptr, 'семь')
            if first_number2 == '8':
                print(ptr, 'восемь')
            if first_number2 == '9':
                print(ptr, 'девять')
        if first_number2 == '2':
            ptr = 'двадцать'
            if first_number2 == '1':
                print(ptr, 'один')
            if first_number2 == '2':
                print(ptr, 'два')
            if first_number2 == '3':
                print(ptr, 'три')
            if first_number2 == '4':
                print(ptr, 'четыре')
            if first_number2 == '5':
                print(ptr, 'пять')
            if first_number2 == '6':
                print(ptr, 'шесть')
            if first_number2 == '7':
                print(ptr, 'семь')
            if first_number2 == '8':
                print(ptr, 'восемь')
            if first_number2 == '9':
                print(ptr, 'девять')
        if first_number2 == '3':
            ptr = 'тридцать'
            if first_number2 == '1':
                print(ptr, 'один')
            if first_number2 == '2':
                print(ptr, 'два')
            if first_number2 == '3':
                print(ptr, 'три')
            if first_number2 == '4':
                print(ptr, 'четыре')
            if first_number2 == '5':
                print(ptr, 'пять')
            if first_number2 == '6':
                print(ptr, 'шесть')
            if first_number2 == '7':
                print(ptr, 'семь')
            if first_number2 == '8':
                print(ptr, 'восемь')
            if first_number2 == '9':
                print(ptr, 'девять')
        if first_number2 == '4':
            ptr = 'сорок'
            if first_number2 == '1':
                print(ptr, 'один')
            if first_number2 == '2':
                print(ptr, 'два')
            if first_number2 == '3':
                print(ptr, 'три')
            if first_number2 == '4':
                print(ptr, 'четыре')
            if first_number2 == '5':
                print(ptr, 'пять')
            if first_number2 == '6':
                print(ptr, 'шесть')
            if first_number2 == '7':
                print(ptr, 'семь')
            if first_number2 == '8':
                print(ptr, 'восемь')
            if first_number2 == '9':
                print(ptr, 'девять')
        if first_number2 == '5':
            ptr = 'пятьдесят'
            if first_number2 == '1':
                print(ptr, 'один')
            if first_number2 == '2':
                print(ptr, 'два')
            if first_number2 == '3':
                print(ptr, 'три')
            if first_number2 == '4':
                print(ptr, 'четыре')
            if first_number2 == '5':
                print(ptr, 'пять')
            if first_number2 == '6':
                print(ptr, 'шесть')
            if first_number2 == '7':
                print(ptr, 'семь')
            if first_number2 == '8':
                print(ptr, 'восемь')
            if first_number2 == '9':
                print(ptr, 'девять')
        if first_number2 == '6':
            ptr = 'шестьдесят'
            if first_number2 == '1':
                print(ptr, 'один')
            if first_number2 == '2':
                print(ptr, 'два')
            if first_number2 == '3':
                print(ptr, 'три')
            if first_number2 == '4':
                print(ptr, 'четыре')
            if first_number2 == '5':
                print(ptr, 'пять')
            if first_number2 == '6':
                print(ptr, 'шесть')
            if first_number2 == '7':
                print(ptr, 'семь')
            if first_number2 == '8':
                print(ptr, 'восемь')
            if first_number2 == '9':
                print(ptr, 'девять')
        if first_number2 == '7':
            ptr = 'семьдесят'
            if first_number2 == '1':
                print(ptr, 'один')
            if first_number2 == '2':
                print(ptr, 'два')
            if first_number2 == '3':
                print(ptr, 'три')
            if first_number2 == '4':
                print(ptr, 'четыре')
            if first_number2 == '5':
                print(ptr, 'пять')
            if first_number2 == '6':
                print(ptr, 'шесть')
            if first_number2 == '7':
                print(ptr, 'семь')
            if first_number2 == '8':
                print(ptr, 'восемь')
            if first_number2 == '9':
                print(ptr, 'девять')
        if first_number2 == '8':
            ptr = 'восемьдесят'
            if first_number2 == '1':
                print(ptr, 'один')
            if first_number2 == '2':
                print(ptr, 'два')
            if first_number2 == '3':
                print(ptr, 'три')
            if first_number2 == '4':
                print(ptr, 'четыре')
            if first_number2 == '5':
                print(ptr, 'пять')
            if first_number2 == '6':
                print(ptr, 'шесть')
            if first_number2 == '7':
                print(ptr, 'семь')
            if first_number2 == '8':
                print(ptr, 'восемь')
            if first_number2 == '9':
                print(ptr, 'девять')
        if first_number2 == '9':
            ptr = 'девяносто'
            if first_number2 == '1':
                print(ptr, 'один')
            if first_number2 == '2':
                print(ptr, 'два')
            if first_number2 == '3':
                print(ptr, 'три')
            if first_number2 == '4':
                print(ptr, 'четыре')
            if first_number2 == '5':
                print(ptr, 'пять')
            if first_number2 == '6':
                print(ptr, 'шесть')
            if first_number2 == '7':
                print(ptr, 'семь')
            if first_number2 == '8':
                print(ptr, 'восемь')
            if first_number2 == '9':
                print(ptr, 'девять')
