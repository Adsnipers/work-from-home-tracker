# Employee Work from home tracker - By Ashton Southall

# Project Styling array, this is called by the script to generate titles and styling throughout the program (0 = program title, 1 = long divider, 2 = medium divider, 3 = short divider)
styleGuide = ["---------------------------------------------\nWelcome to the Work From Home Tracker\nDiamond Realty\n---------------------------------------------", "~~~~~~~~~~~~~~~~~~", "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", "~~~~"]

# Import CSV library
import csv

def addEmployeeHours():
    print("Add Employee Hours")
    print(styleGuide[2])
    print()
    employeeName = input("Full Name: ")
    employeeID = input("Employee Number: ")
    workingWeek = input("Working week: ")
    print(styleGuide[2])
    print("Please enter the whole number of hours you've worked for each of the following days")
    print()
    monHours = input("Enter the number of hours worked on Monday: ")
    tueHours = input("Enter the number of hours worked on Tuesday: ")
    wedHours = input("Enter the number of hours worked on Wednesday: ")
    thurHours = input("Enter the number of hours worked on Thursday:")
    friHours = input("Enter the number of hours worked on Friday:")
    with open("reports/" + employeeID + ".csv", "a") as data: # Open CSV file to write/Append data using employeeID as filename
	    writer = csv.writer(data)
	    writer.writerow([workingWeek, employeeName, employeeID, monHours, tueHours, wedHours, thurHours, friHours]) # Write data to CSV file

def showHoursWorkedReport():
    print("Hours Worked Report")
    print(styleGuide[1])
    # Gather Employee ID and week number to generate report from
    employeeID = input("Employee ID: ")
    weekReportToShow = input("Work week to display: ")
    hourList = []
    # Open CSV file in read mode
    with open("reports/" + employeeID + ".csv", "r") as data:
        reader = csv.reader(data)
        for row in reader:
            hourList.append(row)
            hourList.reverse()
            # Ask user for number of records to display
            recordCount = input("Enter the number of records to display: ")
            for i in range(0, int(recordCount)):
                record = hourList[i]
                print()
                print(styleGuide[2])
                print("Showing " + recordCount + " record(s) for working week " + record[0] + " from " + record[1])
                print(styleGuide[3])
                # Print correct row containg report info for the requested week
                print("Employee ID: " + record[2])
                print("Hours worked on Monday: " + record[3])
                print("Hours worked on Tuesday: " + record[4])
                print("Hours worked on Wednesday: " + record[5])
                print("Hours worked on Thursday: " + record[6])
                print("Hours worked on Friday: " + record[7])
                print()
                print(styleGuide[2])
                print()
            
#Main Menu
#Show program title
print(styleGuide[0])

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
