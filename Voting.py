#program to test whether one is eligible to vote or not based on age and citizenship
#program also solves the syntax problem of uppercase and lowercase user inputs
age = int(input("Enter Age: "))
citizenship = input("Enter Citizenship: ")
if age >= 18 and citizenship.lower() in ["kenyan","tanazanian","ugandan"]:
    print("ELIGIBLE")
else: 
    print("NOT ELIGIBLE")

