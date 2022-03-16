#Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.

day = int(input("Enter day number : ").strip())

if day == 1 :
    print("Monday");

elif day == 2 :
    print("Tuesday")

elif day == 3 :
    print("Wednesday")

elif day == 4 :
    print("Thursday")

elif day == 5 :
    print("Friday")

elif day == 6 :
    print("Saturday")

elif day == 7 :
    print("Sunday")
