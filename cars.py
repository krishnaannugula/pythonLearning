#Access specifiers in python, like Java or C++ there are No specific Access specifiers in python but still can be used like below
#Public = variableName
#protected = _variableName (single underscore)
#private : __variableName (double underscore)


class Cars:
    numberOfWheels= 4
    _color = "red"
    __yearOfManifacturing = 2017 # if in case the private attribute has to be accessed out side the class then it should be called as _Cars__yearOfManifacturing (name mangling)

class Bmw(Cars):
    def __init__(self):
        print("protected attribute ",self._color)

car = Cars()
print("public attribute", car.numberOfWheels)
bmw = Bmw()

print("private attribute", car._Cars__yearOfManifacturing)