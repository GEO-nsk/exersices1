'''
Задание 4.
Определите какой символ встречается ровно три раза в тексте. Гарантируется, что символ
с такой частотой встречаемости только один.
'''

Text = str(input())

count = 1

new_text = sorted(Text)

for i in range(len(new_text)-1):
    if new_text[i] == new_text[i+1]:
        count += 1
    else:
        if count == 3:
            print(new_text[i])
        count = 1