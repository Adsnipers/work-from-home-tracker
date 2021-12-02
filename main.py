# Employee Work from home tracker - By Ashton Southall
# Project Styling array, this is called by the script to generate titles and styling throughout the program (0 = program title, 1 = long divider, 2 = medium divider, 3 = short divider)
styleGuide = ["---------------------------------------------\n    Welcome to the Work From Home Tracker\n              Diamond Realty\n---------------------------------------------", "~~~~~~~~~~~~~~~~~~", "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", "~~~~"]
# Working hour guidelines, Contains mininum hours, maximum hours etc. used to compare worked hours with what the employee is supposed to work
lowest = 4 # Employee working less than 4 hours
high = 10 # Employee working more than 10 hours
higher = 20 # Employee working more than 20 hours
highest = 30 # Employee working more than 30 hours

# Import CSV library
import csv

# Gather inserted hours worked to be checked and display appropriate messages depending on whether the employee worked too many or not enough hours
def checkWorkedHours(monday, tuesday, wednesday, thursday, friday, employeeName): 
    weekdays = [monday,tuesday,wednesday,thursday,friday]
    weekdayint = 5 # Start week at 5 (Friday)
    # Run for every day of the week, remove 1 from weekdayint every time to calculate the day of the week for output to the user
     # Calculate total hours worked in the working week
    totalHours = int(monday) + int(tuesday) + int(wednesday) + int(thursday) + int(friday)
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
        # If the employee worked more or less than the number of hours specified, display appropriate messages. values for lowest, high, higher and highest are retrived from the beginning of the script
        if int(i) >= highest:
            print ("WARNING: Employee worked equal to or more than " + str(highest) + " hours on " + weekday)
        elif int(i) >= higher:
            print ("WARNING: Employee worked equal to or more than " + str(higher) + " hours on " + weekday)
        elif int(i) >= high:
            print ("WARNING: Employee worked equal to or more than " + str(high) + " hours on " + weekday)
        elif int(i) <= lowest:
            print ("WARNING: Employee worked equal to or less than " + str(lowest) + " hours on " + weekday)
    print()
    print("Total hours worked this working week: " + str(totalHours))
    with open("reports/totalHours.csv", "a") as data: # Write total hours to CSV file
        writer = csv.writer(data) # Declare writer object
        writer.writerow([employeeName, totalHours])
    print(styleGuide[1])
    print()

def addEmployeeHours():
    print("Add Employee Hours")
    print(styleGuide[2])
    print("Hint: Leave any input fiend blank to cancel creating and return to the main menu")
    print()
    # Retrive employee information including Full name, Employee ID/Number and the working week to add. 
    employeeName = input("Full Name: ") 
    if employeeName == "":
        return
    employeeID = input("Employee Number: ")
    if employeeID == "":
        return
    workingWeek = input("Working week: ")
    if workingWeek == "":
        return
    print(styleGuide[2])
    print("Please enter the whole number of hours you've worked for each of the following days")
    print()
    # Get user input for the number of hours worked on each of the corresponding days, checking that the values do not exceed 24 hours worked per day.
    monHours = input("Enter the number of hours worked on Monday: ")
    if monHours == "":
        return
    if int(monHours) > 24:
        print("Cannot enter more than 24 hours in one day")
        monHours = 0
    tueHours = input("Enter the number of hours worked on Tuesday: ")
    if tueHours == "":
        tueHours = 0
    if int(tueHours) > 24:
        print("Cannot enter more than 24 hours in one day")
        return
    wedHours = input("Enter the number of hours worked on Wednesday: ")
    if wedHours == "":
        wedHours = 0
    if int(wedHours) > 24:
        print("Cannot enter more than 24 hours in one day")
        return
    thurHours = input("Enter the number of hours worked on Thursday: ")
    if thurHours == "":
        thurHours = 0
    if int(thurHours) > 24:
        print("Cannot enter more than 24 hours in one day")
        return
    friHours = input("Enter the number of hours worked on Friday: ")
    if friHours == "":
        friHours = 0
    if int(friHours) > 24:
        print("Cannot enter more than 24 hours in one day")
        return
    # Open CSV file to write/Append data using employeeID as filename
    with open("reports/" + employeeID + ".csv", "a") as data: 
	    writer = csv.writer(data) # Declare writer object
	    writer.writerow([workingWeek, employeeID, employeeName, monHours, tueHours, wedHours, thurHours, friHours]) # Write data to CSV file
    print()
    print(styleGuide[3])
     # Check worked hours with lowest, high, higher and highest values, this will display a report to the user
    checkWorkedHours(monHours,tueHours,wedHours,thurHours,friHours,employeeName)

def showHoursWorkedReport():
    print("Hours Worked Report")
    print(styleGuide[1])
    # Gather Employee ID and week number to generate report from
    employeeID = input("Employee ID: ")
    if employeeID == "":
        return
    weekReportToShow = input("Work week to display: ")
    if weekReportToShow == "":
        return
    hourList = []
    # Open CSV file in read mode
    with open("reports/" + employeeID + ".csv", "r") as data:
        reader = csv.reader(data)
        for row in reader:
            hourList.append(row)
            hourList.reverse()
            # Ask user for number of records to display
            recordCount = 1 # I tried to get rid of this but deleting it broke everything, just hardcoding the variable so the end user has no idea this is a thing
            for i in range(0, int(recordCount)):
                record = hourList[i]
                print()
                print(styleGuide[2])
                print("Showing record for working week " + str(record[0]) + " from " + str(record[2]))
                print(styleGuide[3])
                # Print correct row containg report info for the requested week
                print("Employee ID: " + record[1])
                print("Hours worked on Monday: " + record[3])
                print("Hours worked on Tuesday: " + record[4])
                print("Hours worked on Wednesday: " + record[5])
                print("Hours worked on Thursday: " + record[6])
                print("Hours worked on Friday: " + record[7])
                print(styleGuide[3])
                checkWorkedHours(record[3], record[4], record[5], record[6], record[7], record[2])
                print()
                print(styleGuide[2])
                print()
            
def reportAll():
    dataList = []
    print()
    print(styleGuide[1])
    print("Displaying full report containing all employee worked hours")
    print(styleGuide[3])
    print()
    with open("reports/totalHours.csv", "r") as report:
        reader = csv.reader(report)
        for row in reader:
            if len(row) > 0:
                print(styleGuide[3])
                print(row[0] + ": " + row[1] + " Hours")
                if (int(row[1]) > 41):
                    print("Employee worked more than 40 hours")

# Main Menu
print(styleGuide[0]) # Show program title
choice = 1 # Set menu option variable
while (choice !=3): # Display menu of options
    print(styleGuide[1])
    print()
    print("Please select one of the following options to continue")
    print("1. Enter hours")
    print("2. Produce Report")
    print("3. Exit")
    print()
    choice = int(input("Please enter selection: ")) # Get option
    print()
    if (choice == 1): # Check user choice
        try:
            addEmployeeHours()
        except:
            print("An error occurred. Please try again")
    elif (choice == 2):
        subChoice = int(input("Please select one of the following options to continue\n1. Generate report for single employee\n2. Generate report for all employees\n"))
        if subChoice == 1: # Generate report for single employee:
            showHoursWorkedReport()
        elif subChoice == 2: # Generate report for all employees
            reportAll()
    elif (choice == 3): # Exit program
        print("Exiting program")
    else:
        print("Please input only one of the 3 options. (1, 2 or 3)")