
class Car:
    def __init__(self, type="A", rendszam="AAA-000",evjarat="1990"):
        self.__type = str(type)
        self.__rendszam = str(rendszam)
        self.__evjarat = str(evjarat)

    def getType(self):
        return self.__type

    def getRendszam(self):
        return self.__rendszam

    def getEvjarat(self):
        return self.__evjarat

    def setType(self,type):
        self.__type = type

    def setEvjarat(self,evjarat):
        self.__evjarat = evjarat

    def setRendszam(self,rendszam):
        self.__rendszam = rendszam
