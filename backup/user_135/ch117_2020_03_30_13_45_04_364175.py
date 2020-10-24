import math

def snell_descartes(n1,n2,t1):
    t2 = (n1/n2)*math.sin(math.radians(t1))
    resultado = (t2)**-1
    return resultado

n1 = 1
n2 = 2
t1 = 30

print(snell_descartes(n1,n2,t1))