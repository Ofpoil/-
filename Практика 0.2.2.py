print('Вводите числа через enter. Как только надоест нажмите enter без ввода числа.')
a = list()
while True:
  b = str(input('Введите число: '))
  if b == "":
    break
  else:
    a.append(b)
pos = int(input('Введите N-ую позицию : '))
finished = ''.join(a)
i = len(finished)
print((int(finished) // (10 ** (i - pos))) % 10)
