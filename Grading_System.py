#Progam that calculates the grade of a student

subject1 = int(input("Enter Score for Subject 1: "))
subject2 = int(input("Enter Score for Subject 2: "))
subject3 = int(input("Enter Score for Subject 3: "))

total = subject1 + subject2 + subject3
average = total/3


if average >= 70 and average <= 100:
    print("YOUR GRADE IS A")

elif average >= 60 and average < 69:
    print("YOUR GRADE IS B")

elif average >= 50 and average < 59:
    print("YOUR GRADE IS C")

elif average >= 40 and average < 49:
    print("YOUR GRADE IS D")

else:
    print("YOU HAVE A FAIL!!!")
