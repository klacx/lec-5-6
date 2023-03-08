from function import*

runChoice = 0
function_choice = "xyz"
mark_list = []
master_list = []

while runChoice == 0:
    if type(function_choice) != int:
        function_choice = int(input("Your Options are:\n "
                                    "1.	Add new student detail.\n "
                                    "2.	View all student details.\n "
                                    "3.	Search Specific student detail."))

    if function_choice == 1:  #Add
        name = str(input("Please enter your name:"))
        tp_number = (input("Please enter your TP Number:"))
        amount = int(input("How many subject in semester:"))
        total = score(amount, mark_list)
        average = average(total, amount)
        grade = grade(average)
        dataRecord(name, tp_number, mark_list, total, average, grade, master_list)

    elif function_choice == 2:  #View
        pass


