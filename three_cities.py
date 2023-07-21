
first_user_input = str(input())
second_user_input = str(input())
third_user_input = str(input())
list = []
list.extend([first_user_input,second_user_input,third_user_input])
print(min(list,key=len))
print(max(list,key=len))