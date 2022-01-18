def SqRootFloat(x):
    return  x ** 0.5

for i in range (int(input("Enter range start")),int(input("Enter range End"))):
                    va = SqRootFloat(i)
                    print(i," ",va)