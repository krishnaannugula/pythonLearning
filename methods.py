class Employee:
    def employeeDetails(self):
        self.name = "What"
        print("Get name",self.name)

    @staticmethod
    def welcomeMessage():
        print("Welcome to orgnization")



getEmployee = Employee()
getEmployee.employeeDetails()
getEmployee.name = "Eshan"

getEmployee.welcomeMessage()

