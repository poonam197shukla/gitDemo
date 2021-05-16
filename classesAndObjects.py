#classes and objects

#let asssume below class as parent class
class calculator:
    num=100

    #default constructor

    def __init__(self,a,b):
        self.firstNumber=a
        self.secondNumber=b
        print("I am constructor")

    def addNewNumber(self):
        print("It is executing method inside class")

    def add(self):
        return self.firstNumber+self.secondNumber+calculator.num




#creation of object one
cal1=calculator(2,3)
cal1.addNewNumber()
print(cal1.add())
#print(cal1.num)

#creation of object two
cal2=calculator(4,5)
#cal2.addNewNumber()
#print(cal2.num)