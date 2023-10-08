n = int(input())
while n > 99:  # пока в числе есть цифры
    # last_digit = n % 10  # получить последнюю цифру
    n = n // 10
print(n%10)