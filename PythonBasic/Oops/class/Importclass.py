class Comp:
    n=""
    def __init__(self,name,age,salary):
         self.n=name
         self.a=age
         self.s=salary
    
    def printline(self):
        print("thisis america",self.n)
        return 1
    



def UsePrint(string):
     return f"this is the string printed by {string}"
        
if __name__ == "__main__":
      print(UsePrint("akshay kumar"))     
      print("name == ",__name__)
      co=Comp("vijay",23,45000)
      print(co.printline())
      print(co.__dict__)