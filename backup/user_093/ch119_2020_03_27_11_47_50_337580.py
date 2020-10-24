def factorial(z):
    elist=[]
    product=1
    while z>0:
        elist.append(z)
        z-=1
    for z in elist: 
        product *= z
    return product


z=0
list=[]
while z!=19:
    x=1/factorial(z)
    list.append(x)
    z+=1
    print("e = ",sum(list))
    print(z)
    