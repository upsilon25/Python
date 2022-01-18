import re

t= "1  his  12 + 5is+ 6r  aining"
t_up= t.replace(' ','')
list = t_up.split('+')
print(list)
print(len(list))

a= list[0].split(' ')
b= list[1].split(' ')
c= list[2].split(' ')
print(a," ",b," ",c)

ay=a[0]
by=b[0]
cy=c[0]

print(ay,' ',by,' ',cy)

ax= (re.findall("([0-9]+)",ay))
bx= (re.findall("([0-9]+)",by))
cx= (re.findall("([0-9]+)",cy))

az=int(ax[0])
bz=int(bx[0])
cz=int(cx[0])
print(ax," ",bx," ",cx)
print(az," ",bz," ",cz)

b24ac= ((bz**2)-4*az*cz)**(0.5)
print(b24ac)
nom1=((-1*bz)+(b24ac))
nom2=((-1*bz)-b24ac)
print(nom1//(2*az))
print(nom2//(2*az))