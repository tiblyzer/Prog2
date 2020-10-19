import numpy
import math

class Car:
    def __init__(self,n_enginePower=0,n_vintage=0,
                 n_plateNumber='AAA-000',n_originPrice=0):
        self._enginePower=n_enginePower
        self._vintage = n_vintage
        self._plateNumber = n_plateNumber
        self._originPrice = n_originPrice

    def getEnginePower(self):
        return self._enginePower

    def getVintage(self):
        return self._vintage

    def getPlateNumber(self):
        return self._plateNumber

    def getOriginPrice(self):
        return self._originPrice

    def setEnginePower(self,n):
        if(type(n) == 'int'):
            self._enginePower = n

    def setVintage(self,n):
        if (type(n) == 'int'):
            self._vintage = n

    def setPlateNumber(self,n):
        if (type(n) == 'str'):
            self._plateNumber = n

    def setOriginPrice(self,n):
        if (type(n) == 'int'):
            self._originPrice = n

class Mercedes(Car):
    def __init__(self,parameterList):

        super().__init__(int(parameterList[1]),int(parameterList[2]),
                 parameterList[3],int(parameterList[4]))
        self.__type = parameterList[0]
        self.__topSpeed = int(parameterList[5])
    def getTopSpeed(self):
        return self.__topSpeed

    def __ge__(self,other):
        return self.__topSpeed >= other.getTopSpeed()

    def reducePrice(self):
        needReduction = numpy.random.rand()
        reduceFactor = numpy.random.rand()

        if (needReduction > 0.5):
            return self._originPrice *(1-reduceFactor)
        else:
            return self._originPrice

    def __str__(self):
        return 'Horsepower: ' + str(self._enginePower) + ',' + 'vintage: ' + str(self._vintage) + ','+ 'plateNumber: ' + str(self._plateNumber)

    def __add__(self, other):
        return self._originPrice + other.getOriginPrice()


class CarHandler:
    def __init__(self):
        self.carList = list()

    def readCarData(self):
        file = open('mercedes.txt')

        for line in file:
            splittedLine = line.split()
            print(splittedLine)
            vehicle = Mercedes(splittedLine)
            self.carList.insert(self.carList.__len__(), vehicle)
    def printContent(self):
        for element in self.carList:
            print(element)

    def calculateReducePrice(self):
        sum = 0
        for element in self.carList:
            sum += element.reducePrice()

        print(sum)


carHandler = CarHandler()
carHandler.readCarData()
carHandler.printContent()
carHandler.calculateReducePrice()

#carList = list()


#for element in carList:
#    print(element)

#sum = 0

#for element in carList:
#    sum += element.getOriginPrice()
#print(sum)


#print(sum)