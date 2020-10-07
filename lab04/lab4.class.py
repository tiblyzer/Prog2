class Car:
    def __init__(self,engine,type):
        self.__engine = engine
        self.__type = type

    def getEngine(self):
        return self.__engine

    def getType(self):
        return self.__type

    def setEngine(self,engine):
        self.__engine = engine

    def setType(self,type):
        self.__type = type

    def __str__(self):
        return 'Properties: ' + self.getEngine() + ' ' + self.getType()

    def printLightType(self):
        print('white')


class Mercedes_X1(Car):
    def __init__(self):
        super().__init__("X 220d","Mercedes class X")

    def printLightType(self):
        print('neonblue')


class AUDI_A6(Car):
    def __init__(self):
        super().__init__("TDI 150 kW", "Audi A6 40")

    def printLightType(self):
        print('neonyellow')

    @staticmethod
    def printLogo():
        print('Audi-logo')

mercedes_X = Mercedes_X1()
audi_A6 = AUDI_A6()

print(mercedes_X)
print(audi_A6)

mercedes_X.printLightType()
audi_A6.printLightType()

AUDI_A6.printLogo()

print(Mercedes_X1.__bases__)
print(AUDI_A6.__bases__)
print(Car.__bases__)

print(Mercedes_X1.__class__)
print(isinstance(audi_A6,AUDI_A6))
