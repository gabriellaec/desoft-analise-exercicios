import math

def snell_descartes(n1,n2,t1):
    t2 = math.sin(math.radians((n1/n2)*t1))
    return t2

n1 = 1
n2 = 2
t1 = math.sin(math.radians(30))

snell_descartes(n1,n2,t1)