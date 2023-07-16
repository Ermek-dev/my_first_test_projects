import math


a = float(input())
b = float(input())
average_arith_numbers = (a+b)/2
average_geometh_numbers = math.sqrt(a*b)
average_harmonious_numbers = (2*a*b)/(a+b)
average_quadratic_numbers = math.sqrt((a**2+b**2)/2)
print(average_arith_numbers)
print(average_geometh_numbers)
print(average_harmonious_numbers)
print(average_quadratic_numbers)
