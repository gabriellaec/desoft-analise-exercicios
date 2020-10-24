import math

def snell_descartes(n1,n2,sint1):
    t2 = (n1/n2)*sint1
    resultado = (t2)**-1
    return resultado

n1 = 1
n2 = 2
t1 = 30
sint1 = math.sin(math.radians(t1)

print(snell_descartes(n1,n2,sint1))