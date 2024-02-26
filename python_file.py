# pay rate python program

user = print("How many employees to process:")
user = int(input())
counter = 1

# while loop
while counter <= user:
    # ask user for employee first name
    fname = print("Enter employee first name: ")
    fname = str(input())

    # ask user for employee last name
    lname = print("Enter employee last name: ")
    lname = str(input())

    # ask user for hours worked by employee
    hours_work = print("Enter the amount of hours", fname, lname , "worked: ")
    hours_work = float(input())

    # ask user employee pay rate
    pay_rate = print("Enter", fname, lname, "pay rate: ")
    pay_rate = float(input())
    
    # multiplies hours worked by pay rate to find employee salary
    pay = hours_work * pay_rate
    
    # prints everything out
    print(fname, lname, "worked", hours_work, "hours at a pay rate of $", pay_rate, "and made $", pay, "this week")
    counter += 1
    print("Program Completed")
