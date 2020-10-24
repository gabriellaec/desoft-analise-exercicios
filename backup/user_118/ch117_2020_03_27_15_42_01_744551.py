import math
def snell_descartes(n1,n2,t1):
    t2=(n1*t1)/n2
    return t2
n1=float(input('Diga um valor para n1: '))
n2=float(input('Diga um valor para n2: '))  
t1=math.degrees(float(input('Diga um valor para t1: ')))
t2=math.degrees((n1*t1)/n2)
print (t2)