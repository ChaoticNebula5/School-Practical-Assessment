#Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria

cost = int(input("What was the cost of your bike?: ").strip())

if cost > 100000:
    tax = 15/100 * cost
    total = cost + tax
    print(f"You will have to pay {tax} as tax. So your total cost will be {total}")
elif ((cost > 50000) and (cost <= 100000)):
    tax = 10/100 * cost
    total = cost + tax
    print(f"You will have to pay {tax} as tax. So your total cost will be {total}")
elif cost <= 50000:
    tax = 5/100 * cost
    total = cost + tax
    print(f"You will have to pay {tax} as tax. So your total cost will be {total}")