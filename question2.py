def addition(no1, no2):
    total = no1 + no2
    print("addition is", total)


def subtraction(no1, no2):
    total = no1 - no2
    print("subtraction is", total)


def multiplication(no1, no2):
    total = no1 * no2
    print("multiplication is", total)


def division(no1, no2):
    total = no1 / no2
    print("division is", total)


n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))
option = int(input("select your option:(addition = 1, subtraction = 2, multiplication = 3, division = 4)"))

if option == 1:
    addition(n1, n2)
elif option == 2:
    subtraction(n1, n2)
elif option == 3:
    multiplication(n1, n2)
elif option == 4:
    division(n1, n2)
