# put your python code here
num = int(input())
while num != 0:  # пока в числе есть цифры
    last_digit = num % 10  # получить последнюю цифру
    # код обработки последней цифры
    print(last_digit,end='')
    num = num // 10  # удалить последнюю цифру из числа