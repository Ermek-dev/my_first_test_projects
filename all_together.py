num = int(input())
first_digit = num%10
kol = 0
maximum = 0
minimum = 10
proiz = 1
summa_chisel = 0
while (num)>0:
    last_digit = num % 10
    kol = kol+1
    summa_chisel = summa_chisel+last_digit
    proiz = proiz * last_digit
    if last_digit>maximum:
        maximum = last_digit
    if last_digit<= minimum:
        minimum = last_digit   
    num = num//10
    
print(summa_chisel)
print(kol)
print(proiz)
print(summa_chisel/kol)
print(last_digit)
print(first_digit+last_digit)
