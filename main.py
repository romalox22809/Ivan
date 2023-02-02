n = input('Введите число: ')
summa = 0
while n>0:
    i = n%10
    n = n/10
    summa = summa + i
print 'Сумма чисел равна =', summa
