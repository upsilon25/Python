class Comp:
    n=""
    def __init__(self,name,age,salary):
         self.n=name
         self.a=age
         self.s=salary
    
    def printline(self):
        print("thisis america",self.n)
        return 1
        
      
co=Comp("vijay",23,45000)


print(co.printline())
print(co.__dict__)
        