# the program has a class named temperature and converts temp to either celsius or fahrenheit

class temperature: # creats a class called temperature

    def __init__(self, temp): # the init method or constructor 
        self.temp = temp

    def convertCelsius(self): # a method to convert temperature to celsius

        a = self.temp * 9/5 + 32 # formula to calculate temp into celsius
        return a # returns the answer after calculation using the formula
    

    def convertFahrenheit (self): # a method to convert temperature to fahrenheit 

        b = (self.temp - 32) * 5/9 # formula to calculate temp into Fahrenheit
        return b # returns the answer after calculation using the formula 
    
temp = temperature(7) # create an object for the class and a variable
print(temp.convertCelsius()) # prints the converted temp into celsius 
print(temp.convertFahrenheit())  # prints the converted temp into fahrenheit 
