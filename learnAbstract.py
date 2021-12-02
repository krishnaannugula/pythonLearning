from abc import ABCMeta, abstractmethod # abc is a AbstractBaseClass if this is inculded as a  @abstractmethod then it forcefull ask methods to implment 

class shape(metaclass = ABCMeta):
    @abstractmethod
    def size(self):
        return 0
    @abstractmethod
    def area(self):
        return 0

class Triangle(shape):
    b= 3
    h= 6
    def area (self):
        print("area of triangle is:", 0.5*self.b * self.h )
    def size(self) :
        print("size of triangle is:", (self.b * self.h ) / 3)

class Rectangle(shape):
    b=3
    h=6
    def area (self):
        print("area of rectangle is:", self.b * self.h )

    def size(self) :
        print("size of rectangle is:", (self.b * self.h ) / 2)
    


triangle= Triangle()
triangle.area()
triangle.size()

rectangle=Rectangle()
rectangle.area()
rectangle.size()
