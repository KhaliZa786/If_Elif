a = int(input("Введите число "))
b = int(input("Введите число "))
c = int(input("введите число "))
d = int(input("Выберите действие 1.Сумма чисел 2. Произведение чисел "))
if d == 1:
    x = a+b+c
    print(x, "сумма чисел")
elif d == 2:
    x = a*b*c
    print(x, "произведение чисел")

a = int(input("Введите число "))
b = int(input("Введите число "))
c = int(input("введите число "))
d = int(input("Выберите действие 1.Максимум 2. Минимум 3.Среднеарифмитическое "))
if d == 1:
  x = max(a,b,c)
  print (x, "максимум")
if d == 2:
    x = min(a,b,c)
    print(x,"минимум")
elif d ==3:
    x = (a+b+c) //2
    print(x, "среднеарифметическое")

a = int(input("Введите число"))
print("a", 100)
b = int(input("Выберите действие 1.Мили 2. Дюймы 3. Ярды"))
if b == 1:
    x = a * 1069
    print(x, "мили")
if b == 2:
    x = a * 39.37
    print(x, "дюймы")
elif b == 3:
    x = a * 1.09
    print(x, "ярды")

number = int(input("Введите число "))
if number > 0:
    print("number is pozitive")
elif number < 0:
    print("number is negative")
else:
    print("number is equal to zero")

a = int(input("a: "))
b = int(input("b: "))
if a > b:
   print(b)
   print(a)
elif a < b:
   print(a)


