# Python program that uses a function to check if a given string is a palindrome
def is_palindrome(word):

    #converting the word to lowercase to make comparison become case sensitive
    word = word.lower()

    #check if the word is equal to its reverse
    return word == word[::-1]

#Prompt the user for any word/string
user_wrd = input("Enter a word:  ")

#Test the user input word/string using an if...else statement
if is_palindrome(user_wrd):
    print("THE WORD ENTERED IS A PALINDROME")
else: 
    print("THE WORD IS NOT A PALINDROME")

    