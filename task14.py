'''
Задание 14.
В телевизионной игре "Поле чудес", игрок отгадывает слово. Напишите программу, которая спрашивает
у ведущего подсказку и загаданное слово. Далее, программа удаляет информацию с экрана, выполняя
вывод 25 пустых строк. После этого, выводится подсказка и слово, где вместо букв, выводятся
символы "*". Игрок должен с десяти попыток отгадать слово по буквам. После каждого хода выводится
слово, где неназванные буквы закрыты символом "*".  Отгаданные буквы выводятся на тех местах, где
они расположены. Каждый ход сопровождается вопросом "Буква или слово (0 - буква, 1 - слово)?".
В случае если слово отгадано верно, выводится сообщение "Победа!". Если слово названо неверно,
или закончились попытки, выводится сообщение "Проигрыш!".

Пример работы программы:
Ведущий вводит две строки: подсказку и загаданное слово.
Дикое животное.
тигр
Программа выводит 25 пустых строк и таким образом "скрывает" то, что написал ведущий.
Игрок пытается отгадать слово:
Дикое животное.
****
Буква или слово (0 - буква, 1 - слово)?0
a
****
Буква или слово (0 - буква, 1 - слово)?0
р
***р
Буква или слово (0 - буква, 1 - слово)?0
и
*и*р
Буква или слово (0 - буква, 1 - слово)?1
тигр
Победа!
'''


prompt = str(input())
word = str(input())
print('\n'*25)
print(prompt)
print(len(word)*'*')

new_word = '*' * len(word)
flag = True

for i in range(1,11):
    answer = int(input('Буква или слово (0 - буква, 1 - слово)?'))
    if answer == 1:
        answer_word = str(input())
        if answer_word == word:
            print('Победа!')
            flag = False
            break
        else:
            print('Проигрыш!')
            flag = False
            break
    else:
        answer_letter = str(input())
        for i in range(len(word)):
            if word[i] == answer_letter:
                new_word = new_word[:i] + answer_letter + new_word[i+1:]
        print(new_word)
        if new_word == word:
            print('Победа!')
            flag = False
            break

if flag:
    print('Проигрыш!')