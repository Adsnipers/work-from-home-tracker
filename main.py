# Employee Work from home tracker - By Ashton Southall

# Import CSV library
import csv

def addEmployeeHours():
    print("Add Employee Hours")
    print("~~~~~~~~~~~~~~~~~~")
    print()
    employeeName = input("Full Name: ")
    employeeID = input("Employee Number: ")
    workingWeek = input("Working week: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please enter the whole number of hours you've worked for each of the following days")
    print()
    monHours = input("Enter the number of hours worked on Monday: ")
    tueHours = input("Enter the number of hours worked on Tuesday: ")
    wedHours = input("Enter the number of hours worked on Wednesday: ")
    thurHours = input("Enter the number of hours worked on Thursday:")
    friHours = input("Enter the number of hours worked on Friday:")

    # Open CSV file to write/Append data
    with open("reports/" + employeeID + ".csv", "a") as data:
	    writer = csv.writer(data)
	    writer.writerow([workingWeek, employeeName, employeeID, monHours, tueHours, wedHours, thurHours, friHours])

def showHoursWorkedReport():
    print("Hours Worked Report")
    print("~~~~~~~~~~~~~~~~~~~")
    employeeID = input("Employee ID: ")
    weekReportToShow = input("Work week to display: ")
    with open("reports/" + employeeID + ".csv", "r") as data:
        reader = csv.reader(data)
        for row in reader:
            print()
            print("~~~~~~~~~~~~~~~~~~~")
            print()
            # Print correct row containg report info for the requested week



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
    print()

    # Check user choice
    
    if (choice == 1):
        addEmployeeHours()
    elif (choice == 2):
        showHoursWorkedReport()
    else:
        print("Please input only one of the 3 options. (1, 2 or 3)")
    