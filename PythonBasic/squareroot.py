def square(x):
    i=1
    while (i<x):
        if(x/(i*i)==1):
            return  i
        i=i+1
        
    return -1 
 
for i in range (1,100):
        val= square(i)
        if(val!=-1):        
          print(val," ",i)