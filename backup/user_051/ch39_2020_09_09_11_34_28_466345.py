def f(x):
    lista=[x]
    while x > 1:
        if x%2==0:
            x=x/2
        else:
            x=3*x+1
        lista.append(x)
    return lista
i=1
am=0
b=0
while i<=1000:
    f(i)
    lista=f(i)
    a=len(lista)
    if a > am:
        am=a
        b=i
    i+=1
print(am)
print(b)
print (f(b))