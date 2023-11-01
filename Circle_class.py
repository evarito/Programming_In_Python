# python code with class Circle that has two methods that computes area and the perimeter of the circle

class Circle: # create a class called circle 

    def __init__(self, radius): # constructor 
        self.radius = radius

    def area(self):# method to calculate area 

        a = 3.142 * self.radius * self.radius # formula to calculate the area of a circle. Store it in a variable a
        return a # returns the answer of the calculation 
    
    def perimeter(self): # method to calculate the perimeter of a circle. 

        b = 2 * 3.142 * self.radius # formula to calculate the perimeter of a circle. Store it in a variable
        return b # returns the answer of the calculation

radius = Circle(7) #create an object for the class Circle 
print(radius.area()) #prints the answer of the area 
print(radius.perimeter())#prints the answer of the perimeter