def pali(x):
    sum=0
    while(x>0):
        rem=x%10
        sum=sum*10+rem
        x=x//10 
    return sum    


choose= 'y'
while(choose!=1):
   x=int(input("enter x"))
   val= pali(x)
   if(val==x):
       print("pali")
   else:
       print("not pali") 
   choose=(input("enter choose"))      
       