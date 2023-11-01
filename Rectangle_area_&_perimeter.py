
class Rectangle: # create a class called rectangle

    def __init__(self, length, width): # constructor 
        
        self.length = length #instance variable 
        self.width = width #instance variable 

    def area(self):# method to calculate area 

        a = self.length * self.width # formula to calculate the area of a rectangle. Store it in a variable a
        return a # returns the answer of the calculation 
    
    def perimeter(self): # method to calculate the perimeter of a rectangle. 

        b = 2(self.length + self.width) # formula to calculate the perimeter of a rectangle. Store it in a variable
        return b # returns the answer of the calculation

calc = Rectangle(7,14) #create an object for the class Rectangle 
print(Rectangle.area()) #prints the answer of the area 
print(Rectangle.perimeter())#prints the answer of the perimeter