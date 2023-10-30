a,b,c = len(input()),len(input()),len(input())
summa_numbers = a+b+c
maximum_of_num = max(a,b,c)
minimum_of_num = min(a,b,c)
average_of_num = summa_numbers-maximum_of_num-minimum_of_num
if maximum_of_num-average_of_num == average_of_num-minimum_of_num:
    print("YES")
else:
    print("NO")
