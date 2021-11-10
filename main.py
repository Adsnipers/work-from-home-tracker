# Employee Work from home tracker - By Ashton Southall

def addEmployeeHours():
    print("Add Employee Hours")
    print("~~~~~~~~~~~~~~~~~~")
    print()

def showHoursWorkedReport():
    print("Hours Worked Report")
    print("~~~~~~~~~~~~~~~~~~~")
    employeeName = input("Full Name: ")
    employeeID = input("Employee Number: ")
    print("Please enter the whole number of hours you've worked for each of the following days")
    monHours = input("Enter the number of hours worked on Monday: ")
    tueHours = input("Enter the number of hours worked on Tuesday: ")
    wedHours = input("Enter the number of hours worked on Wednesday: ")
    thurHours = input("Enter the number of hours worked on Thursday:")
    friHours = input("Enter the number of hours worked on Friday:")


#Main Menu
#Show program title
print("---------------------------------------------")
print("    Welcome to the work from home tracker    ")
print("              DIAMOND REALTY                 ")
print("---------------------------------------------")
print("")

# Set menu option variable
choice = 1

while (choice !=3):
    # Display menu of options
    print("Please select one of the following options to continue")
    print("1. Enter hours")
    print("2. Produce Report")
    print("3. Exit")
    print()

    # Get option
    choice = int(input("Please enter selection: "))

    # Check user choice
    
    if (choice == 1):
        addEmployeeHours()
    elif (choice == 2):
        showHoursWorkedReport()
    else:
        print("Please input only one of the 3 options. (1, 2 or 3)")
    