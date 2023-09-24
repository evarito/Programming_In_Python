#program to determine the amount of discount offered for goods sold above Ksh.1000

amount = int(input("Enter Amount:  "))
if amount >= 1000:
    Discount = 0.05 * amount
    print("The Discount is: ", Discount)
else: 
    print("NO DISCOUNT")