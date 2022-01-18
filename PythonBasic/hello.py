3
4

def protien( num ):
    if (num <1): 
        return 1
    else:
        return num*protien(num-1)
    
i=1
while i < 6:
    print("the python")
    val=int(input("Enter the number"))
    print(protien(val))
    i=i+1
