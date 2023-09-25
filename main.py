number = 123456789

first_number1 = number // 100000000
first_number2 = number // 10000000 % 10
first_number3 = number // 1000000 % 10
second_number1 = number // 100000 % 10
second_number2 = number // 10000 % 10
second_number3 = number // 1000 % 10
third_number1 = number // 100 % 10
third_number2 = number // 10 % 10
third_number3 = number % 10

print(first_number1)
print(first_number2)
print(first_number3)
print(second_number1)
print(second_number2)
print(second_number3)
print(third_number1)
print(third_number2)
print(third_number3)

