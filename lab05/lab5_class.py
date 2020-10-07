class A:
    def __init__(self):
        print('A.__init__(self) has been called.')
        self.__number = 5
    def get(self):
        return self.__number
    def __str__(self):
        return 'class A'
    def printName(self):
        print('A')

class B:
    def __init__(self):
        print('B.__init__(self) has been called.')
        self.__value = 9
    def get(self):
        return self.__value
    def __str__(self):
        return 'class B'
    def printName(self):
        print('B')

class C(A,B):
    def __init__(self):
        print('C.__init__(self) has been called.')
        super().__init__()
    def __str__(self):
        return 'class C'
    def printValue(self):
        print(str(self.get()))

class D(A,B):
    def __init__(self):
        print('D.__init__(self) has been called.')
        super().__init__()
        super(A,self).__init__()
    def __str__(self):
        return 'class C'
    def printValue(self):
        print(str(self.get()))

class E:
    def __init__(self):
        print('E.__init__(self) has been called.')
        self.__a = A()
        self.__b = B()
    def printValues(self):
        print(str(self.__a.get()) + ',' + str(self.__b.get()))

test = C()
test.printValue()

test2 = D()
test2.printValue()

test3 = E()
test3.printValues()