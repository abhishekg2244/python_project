class Calculator:
    def __init__(self,a,b):
        self.a1=a
        self.b1=b
        
    def  add(self):
      print(self.a1+self.b1)


    def  sub(self):
        print(self.a1-self.b1)

cal=Calculator(20,10)
cal.add()
cal.sub()