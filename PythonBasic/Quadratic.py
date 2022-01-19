import re
# Only positive Quadratic equations are available
t= "x2+6x+8"
t_up= t.replace(' ','')
print(t_up)
list = re.split('-|\+',t_up)
print(list)
print(len(list))

a= list[0].split(' ')
if(a==['x2']):
    a=['1x2']
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
print(ax," ",bx," ",cx)
az=int(ax[0])
bz=int(bx[0])
cz=int(cx[0])

# if(re.findall("-",t).count>0):
print(re.findall("-",t).count)
print(az," ",bz," ",cz)

b24ac= ((bz**2)-(4*az*cz))**(0.5)
print(b24ac)
nom1=((-1*bz)+(b24ac))
nom2=((-1*bz)-b24ac)
print("root1 ",nom1/(2*az))
print("root2 ",nom2/(2*az))