import function

run_choice = 0
master_list = []
temp_list = []

while run_choice == 0:
    function_choice = int(input("Your Options are:\n "
                                "1.	Add new student detail.\n "
                                "2.	View all student details.\n "
                                "3.	Search Specific student detail."))

    if function_choice == 1:
        mark_list = []
        name = str(input("Please enter your name:"))
        tp_number = (input("Please enter your TP Number:"))
        amount = int(input("How many subject in semester:"))

        total = function.score(amount, mark_list)
        average = function.average(total, amount)
        grade = function.grade(average)
        function.dataRecord(name, tp_number, mark_list, total, average, grade, master_list)

    elif function_choice == 2:
        for student in master_list:
            function.display(student)

    elif function_choice == 3:
        search = input("Enter a name to search specific detail")
        function.search(search, master_list)

    else:
        print("Invalid value, please try again. ")

    run_choice = int(input("Do you want to continue ‘0’ to Continue ‘-1’ to Terminate"))
    if run_choice == 0 or run_choice == -1:
        pass
    else:
        run_choice = int(input("Invalid value. Please try again! ‘0’ to Continue ‘-1’ to Terminate"))
