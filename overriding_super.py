class Employee:
    def setNumberOfWokringhours(self):
        self.numberOfWokringhours = 40
    
    def displayNumberOfWokringhours(self):
        print(self.numberOfWokringhours)


class Trainee(Employee):
    def setNumberOfWokringhours(self): # here the method setNumberOfWokringhours is overrinding the base class 
        self.numberOfWokringhours = 45 

    def resetNumberOfWokringhours(self):
        super().setNumberOfWokringhours()    # here the method is reset by super() function in base class 



employee = Employee()
employee.setNumberOfWokringhours()

print("Number Of Wokring hours of a Employee: ", end = ' ')
employee.displayNumberOfWokringhours()

trainee= Trainee()
trainee.setNumberOfWokringhours()
print("Number Of Wokring hours of a trainee: ", end = ' ')
trainee.displayNumberOfWokringhours()


trainee.resetNumberOfWokringhours()
print("Number Of Wokring hours of a trainee after reset: ", end = ' ')
trainee.displayNumberOfWokringhours()