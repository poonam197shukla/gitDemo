#inheritance

#let assume below class as child class
from classesAndObjects import calculator

class childImp(calculator):
    numChild=200

    def __init__(self):
        calculator.__init__(self,2,20)

    def getCompleteData(self):
        return self.numChild+self.num+self.add()


child=childImp()
child.getCompleteData()
