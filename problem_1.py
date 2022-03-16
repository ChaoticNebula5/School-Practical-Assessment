#Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on
number = int(input("Enter a number from 1 to 12: ").strip())

if number > 12:
    print("Please enter a number from 1 to 12")
if number < 0:
    print("Please enter a number from 1 to 12")  
    
if number == 1:
    print("The Month is January. January has 31 days")
if number == 2:
    print("The Month is February. February has 28 days but 29 days in a leap year.")
if number == 3:
    print("The Month is March. March has 31 days.")
if number == 4:
    print("The Month is April. April has 30 days.")
if number == 5:
    print("The Month is May. May has 31 days.")
if number == 6:
    print("The Month is June . June has 30 days.")
if number == 7:
    print("The Month is July. July has 31 days.")
if number == 8:
    print("The Month is August. August has 31 days")
if number == 9:
    print("The Month is September. September has 30 days")
if number == 10:
    print("The Month is October. October has 31 days")
if number == 11:
    print("The Month is November. November has 30 days")
if number == 12:
    print("The Month is December. December has 31 days")