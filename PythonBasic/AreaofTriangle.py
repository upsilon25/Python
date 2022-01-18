def area(a,b,c):
    s=(a+b+c)//2

    ar=(s*(s-a)*(s-b)*(s-c))

    return ar ** 0.5 

print(area(12,14,16))