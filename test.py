def main():
    print("""Добро пожаловать в игру нечетно или даже)))
Введите числа от 1 до 1000)""")
    user_input = int(input("Какой номер вы думаете?\n>"))
    if user_input%2==0:
        print("Ураа!!!Это четное число вы угадали!!!")
    else:
        print("Это нечетное число! У другого?")


main()
