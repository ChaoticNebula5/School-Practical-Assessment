#Write a program to accept percentage from the user and display the grade according to the following criteria

marks = int(input("Please enter your marks: ").strip())

if marks > 90:
    print("WOW! Good Job! You got A grade")
elif ((marks <= 90) and (marks > 80)):
    print("Keep up the good work! You got B Grade")
elif ((marks >= 60) and (marks <=80)):
    print("You can do better! You got C Grade")
elif marks < 60:
    print("Start studying. You got D Grade")
