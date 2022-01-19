import re

str1="-x2-6x+8"
a=len(str1)
y=re.sub("-","#-",str1)
print(y)
sp=y.split("#")
print("spilting sp",sp)
newsa=re.split('\+',sp[0])
newsb=re.split('\+',sp[1])
newsc=re.split('\+',sp[2])
print(newsa)
print(newsb)
print(newsc)
print("separating negative")

newsC=newsc[0]
print(newsC)
newsint=re.split('x',newsC)
print(int(newsint[0])*3)

  
print("thiisi")         