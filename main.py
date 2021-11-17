# Employee Work from home tracker - By Ashton Southall
# Project Styling array, this is called by the script to generate titles and styling throughout the program (0 = program title, 1 = long divider, 2 = medium divider, 3 = short divider)
styleGuide = ["---------------------------------------------\nWelcome to the Work From Home Tracker\nDiamond Realty\n---------------------------------------------", "~~~~~~~~~~~~~~~~~~", "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", "~~~~"]
# Working hour guidelines, Contains mininum hours, maximum hours etc. used to compare worked hours with what the employee is supposed to work
lowest = 4 # Employee working less than 4 hours
high = 10 # Employee working more than 10 hours
higher = 20 # Employee working more than 20 hours
highest = 30 # Employee working more than 30 hours

# Import CSV library
import csv

def checkWorkedHours(monday, tuesday, wednesday, thursday, friday): # Gather inserted hours worked to be checked and display appropriate messages depending on whether the employee worked too many or not enough hours
    weekdays = [monday,tuesday,wednesday,thursday,friday]
    weekdayint = 5
    for i in weekdays:
        if weekdayint == 5:
            weekday = "Monday"
            weekdayint = weekdayint - 1
        elif weekdayint == 4:
            weekday = "Tuesday"
            weekdayint = weekdayint - 1
        elif weekdayint == 3:
            weekday = "Wednesday"
            weekdayint = weekdayint - 1
        elif weekdayint == 2:
            weekday = "Thursday"
            weekdayint = weekdayint - 1
        elif weekdayint == 1:
            weekday = "Friday"
            weekdayint = weekdayint - 1
        if int(i) >= highest:
            print ("WARNING: Employee worked equal to or more than " + str(highest) + " hours on " + weekday)
        elif int(i) >= higher:
            print ("WARNING: Employee worked equal to or more than " + str(higher) + " hours on " + weekday)
        elif int(i) >= high:
            print ("WARNING: Employee worked equal to or more than " + str(high) + " hours on " + weekday)
        elif int(i) <= lowest:
            print ("WARNING: Employee worked equal to or less than " + str(lowest) + " hours on " + weekday)
    print()
    print(styleGuide[1])
    print()

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
    thurHours = input("Enter the number of hours worked on Thursday: ")
    friHours = input("Enter the number of hours worked on Friday: ")
    with open("reports/" + employeeID + ".csv", "a") as data: # Open CSV file to write/Append data using employeeID as filename
	    writer = csv.writer(data)
	    writer.writerow([workingWeek, employeeName, employeeID, monHours, tueHours, wedHours, thurHours, friHours]) # Write data to CSV file
    checkWorkedHours(monHours,tueHours,wedHours,thurHours,friHours)

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
            recordCount = input("Enter the number of records to display or press enter to exit: ")
            if recordCount == "":
                return
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
                print(styleGuide[3])
                checkWorkedHours(record[3], record[4], record[5], record[6], record[7])
                print()
                print(styleGuide[2])
                print()
            
# Main Menu | Show program title
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