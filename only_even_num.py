numbers = 10
flag = True
for i in range(1,numbers+1):
    user_input = int(input())
    if user_input % 2 != 0:
        flag = False     
if flag:
    print("YES")
else:
    print("NO")     