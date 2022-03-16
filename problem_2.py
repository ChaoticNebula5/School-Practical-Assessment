#Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

number = int(input('Enter a number: ').strip())

if number % 2 == 0 and number % 3 == 0:
    print(f"The number {number} is divisible by 2 and 3 both")
else:
    print(f"The number {number} is not divisible by 2 and 3")