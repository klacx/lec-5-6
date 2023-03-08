def check(number, number_list):
    for no in number_list:
        if number == no:
            return True


def display(mlist):
    count = 1
    print("Student name:", mlist[0])
    print(mlist[0], "'s", "TP Number:", mlist[1])
    for mark in mlist[2]:
        print("subject", count, "'s marks:", mark)
        count += 1
    print("Total of all subjects:", mlist[3])
    print("Average of Semester:", mlist[4])
    print("Grade of Semester:", mlist[5])


def score(amount, mark_list):
    total = 0
    for count in range(1, amount + 1, 1):
        mark = int(input("please enter your subject " + str(count) + "'s marks:"))
        mark_list.append(mark)
        total = total + mark
    return total


def average(total, amount):
    average_mark = total / amount
    return average_mark


def grade(average_mark):
    if average_mark >= 80:
        return "A+"
    elif average_mark >= 75:
        return "A"
    elif average_mark >= 70:
        return "B+"
    elif average_mark >= 65:
        return "B"
    elif average_mark >= 60:
        return "C+"
    elif average_mark >= 55:
        return "C"
    elif average_mark >= 50:
        return "C-"
    else:
        return "D/Fail"


def dataRecord(name, tp_number, mark_list, total, average_mark, grade_mark, master_list):
    temp_list = [name, tp_number, mark_list, total, average_mark, grade_mark]
    master_list.append(temp_list)
    #record = open("record.txt", "w")
    #temp = ",".join(map(str, temp_list))
    #record.writelines(temp + "\n")


def search(search, master_list):
    for detail in master_list:
        if search in detail:
            display(detail)


def view():
    record = open("record.txt", "r")
    for data in record.readlines():
        temp = data.rstrip().split(",")
        display(temp)





