# Найдите сумму цифр трехзначного числа.
a = int(input("Введите трехзначное число: "))
b = a // 100
c = (a // 10) % 10
d = a % 10
print(b + c + d)