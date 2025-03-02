# let's try some basics from scratch


class Animal:
    def __init__(self, name="zero"):
        self.name=name
    
    #def speak(self):
    #    print("Hello")



class Cat(Animal):
    def speak(self):
        print("meow")
    

class Dog(Animal):
    def speak(self):
        print("whoof")


c1 = Cat("caramel")

c1.speak()

d1 = Dog("lilo")
d1.speak()



#polymorphism

class Shape:
    def area(self):
        pass

s = Shape()
print("s.area()")
print(s.area())
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width=width
        self.height=height
    
    def area(self):
        return self.width*self.height
    

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2


shapes = [Rectangle(4,5), Circle(9)]
for shape in shapes:
    print(shape.area())

# Import the abc module to define abstract classes and methods
from abc import ABC, abstractmethod

# Define an abstract class called Shape that has an abstract method called area
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
#t=Shape()
#print("t.aera()")
#print(t.area())
# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implement the area method for Rectangles
    def area(self):
        return self.width * self.height

# Define a Circle class that also inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implement the area method for Circles
    def area(self):
        return 3.14 * self.radius ** 2

# Create a list of shapes that includes both Rectangles and Circles
shapes = [Rectangle(4, 5), Circle(7)]

# Loop through each shape in the list and print its area
for shape in shapes:
    print(shape.area())

    
