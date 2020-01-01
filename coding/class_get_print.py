"""program: get input using getString and display using printString in class"""

class GetPrintClass:
    def _init_(self):
        self.s=""
    def getString(self):
        self.s=input("enter a string ")
    def printString(self):
        self.s=self.s.upper()
        print(self.s)
obj=GetPrintClass()
obj.getString()
obj.printString()
