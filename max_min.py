num = int(input())
maximum = 0
minimum = 10
while num>0:
    last_digit = num % 10
    if last_digit>maximum:
        maximum = last_digit
    if last_digit<= minimum:
        minimum = last_digit   
    num = num//10
print('Максимальная цифра равна',maximum)    
print('Минимальная цифра равна',minimum)  
