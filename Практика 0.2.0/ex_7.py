print('Введите номер нужной вам операции:')
number_operation = int(input('1 - "+", 2 - "-", 3 - "/", 4 - "*": '))
number_1 = float(input('Введите первое число: '))
number_2 = float(input('Введите второе число: '))
if number_operation == 1:
  res = number_1 + number_2
elif number_operation == 2:
  res = number_1 - number_2
elif number_operation == 3:
  res = number_1 / number_2
elif number_operation == 4:
  res = number_1 * number_2
print(res)
