import function

list = [65, 75, 85, 95, 105]

number = int(input("please enter a number:"))

if function.check(number, list):
    print("in list")
else:
    print("not in list")
