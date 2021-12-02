class Employee:
    name = "Krishna"
    department = "IT"
    monthlyTargetAchived = 2

    def isMonthlytargetAchived(self):
        if self.monthlyTargetAchived >= 5:
            print("Employee" ,self.name, "achived monthly traget")
        else:
            print("Employee" ,self.name, "not achived monthly traget")


employeeOne = Employee()
print(employeeOne.name)

employeeOne.name = "Om Eshan"
employeeOne.monthlyTargetAchived = 6
employeeOne.isMonthlytargetAchived()
