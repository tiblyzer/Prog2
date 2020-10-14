class Clock:
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.__minutes = minutes
        self.__hours = hours
        self.__seconds = seconds
    def set(self,hours,minutes,seconds=0):
        self.__minutes = minutes
        self.__hours = hours
        self.__seconds = seconds
    def tick(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__minutes += 1
            self.__seconds = 0
        if (self.__minutes == 60):
            self.__hours += 1
            self.__minutes = 0
        if (self.__hours == 24):
            self.__hours = 0
    def display(self):
        print('Aktualis ido: ' + str(self.__hours) + ':' + str(self.__minutes) + ":" +str(self.__seconds))
    def __str__(self):
        return str(self.__hours) + ':' + str(self.__minutes) + ":" +str(self.__seconds)

timePoint = Clock()
print(timePoint)
timePoint.display()

for i in range(0,100):
    timePoint.tick()
    print(timePoint)