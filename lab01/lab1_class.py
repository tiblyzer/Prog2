import datetime

class Student:
    def __init__(self):
        self.__neptunCode = "Akj5n3"
        self.name = "Nagy Aniko"
        self.department = "IK"
        self.birthDate = datetime.datetime(1995,5,20)
        self.currentlySemester = 3

    def printData(self):
        print(self.neptunCode)
        print(self.name)

person = Student()
person.printData()