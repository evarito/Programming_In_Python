''''
The program is a banking app that a user can deposit, make widthrawals, and check balance.
It also prints out customer details. It displays options for a user to pick an option to either withdraw, 
check balance, make deposits and exits after a user is done.  
'''
import datetime

class Bank_Account: # this creates a class that will be important in creating objects with attributes and methods

    def __init__(self, account_number, customer_name): # this line defines constructor method for the bank account class. it initializes the objects attributes
  
        self.account_number = account_number # the value account_number is assigned to the account_number attribute of the object 

        self.customer_name = customer_name # the value customer_name is assigned to the customer_name attribute

        self.balance = 0 # the balance attribute is initialized with the object being 0 when a new Bank_Account object is created 
        self.date_of_opening = datetime.datetime.now()

        
    def depo(self, amount): # the method is used to deposit money into the account. 
        self.balance += amount # this line use the operator to increase the amount balance by the deposited amount
        return amount # the deposited amount is returned 
    
    def withdraw(self, amount):# a method to withdraw money from he account and the amount is the parameter rep. cash to be withdrawn 
        '''
        In this method the acconut balance is checked whether withdrawal can happen
        or there is insufficient balance. If the balance is insufficient it displays an insufficient message.
        If the balance can accept withdrawals, then the amount is subtarcted from the account. 
        '''
        if self.balance < amount:
            return "BALANCE IS NOT ENOUGH TO WITHDRAW!"
        else:
            self.balance -= amount # here is where the amount is decreased.
            return amount # the withdrawn amount is then returned 
        
        
    def view_balance(self):# method views the current balance by returning te value of self.balance
        return self.balance
    
    def cust_details(self):
        print("\nCustomer Name: {}".format(self.customer_name))
        print("Account Number: {}".format(self.account_number))
        print("Date of Account Opening: {}".format(self.date_of_opening.strftime("%Y-%m-%d"))) #the datetime function is called to get the current date and time when the account was created. The value is assigned to the date_of_opening attribute of the object. 
        print("Current Balance: Ksh.{}".format(self.balance))



# The next block of code is an interactive user input 
'''
- Here the user will be prompted to enter their name and account number. 
- Then have a list of choices on which task they want to perform.
- At the end of the list there is an option to exit the program/ transaction process.
'''
account_number = int(input("Enter your account number: "))#prompt user to enter their account number
customer_name = input("Enter your name: ").upper()#prompt user to enter their name. Then the .upper() method converts the string to uppercase

account = Bank_Account(account_number=account_number, customer_name=customer_name)
'''
The code on the line above creates an instance of the Bank_accaount class. it initislizes
the account variable as an object of the Bank_Account class, passing the user-input 
account number and the uppercase customer name as arguments. 
'''


while True:# the code starts a loop until it encouters a break statement inside the loop thus ending the program. 
        print("\n1. Make a Deposit")
        print("2. Make a withdrawal")
        print("3. Check Your Balance")
        print("4. Display customer Details")
        print("5. End Transaction")
# The print statements provide choies for a user to select 
        select = input("\nSelect an Option to Proceed:  ")# prompts a user to enter their choice then the user input is stored in the 'select' variable

        if select == "1":
            amount = int(input("Enter Amount You Wish to Deposit:  "))
            depo_amount = account.depo(amount)
            print(f"YOU HAVE DEPOSITED: Ksh.{depo_amount}") # f-strings have been used to simplify formating instead of using the inbuilt function .format()

        elif select == "2":
            amount = int(input("Enter Amount You Wish to Withdraw:  "))
            w_amount = account.withdraw(amount)
            if w_amount == "BALANCE IS NOT ENOUGH TO WITHDRAW!":
                print("CANNOT COMPLETE TRANSACTION: INSUFFICIENT BALANCE!")
            else:
                print(f"YOU HAVE WITHDRAWN: Ksh.{w_amount}")# f-strings have been used to simplify formating instead of using the inbuilt function .format()
        

        elif select == "3":
            print(f"YOUR CURRENT BALANCE IS: Ksh.{account.view_balance()}")# f-strings have been used to simplify formating instead of using the inbuilt function .format()

        
        elif select == "4":
            account.cust_details()# call the cust_details function/method to display customer details.
        
        
        elif select == "5":
            print("TRANSACTIONS COMPLETE.")
            break # the break statement ends the program when the 5 choice is selected. 

        else:
            print("INVALID CHOICE. PICK A VALID OPTION!")



