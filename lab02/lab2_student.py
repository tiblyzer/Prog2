import datetime

class Student:
    def __init__(self):
        self.__neptunCode = "Akj5n3"
        self.name = "Nagy Aniko"
        self.department = "IK"
        self.birthDate = datetime.datetime(1995,5,20)
        self.currentlySemester = 3
    
    #-------Uj metodusok--------
    def getNeptunCode(self):
        return self.__neptunCode

    def setNeptunCode(self,newCode):
        self.__neptunCode = newCode
    def setNeptunCode(self,newCode,semester):
        if semester == 2:
            self.__neptunCode = newCode
        
    #-----------------------------
    
    def printData(self):
        print(self.neptunCode)
        print(self.name)

person = Student()

#-----------------------------

person.setNeptunCode("Akj5n6")
print(person.getNeptunCode())

#-----------------------------

print(person)