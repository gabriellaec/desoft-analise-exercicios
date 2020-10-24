import math

def snell_descartes(n1,n2,t1):
    t2 = math.sin(math.radians((n1/n2)*t1))
    return t2

n1 = 2
n2 = 1
t1 = math.sin(math.radians(1))

snell_descartes(n1,n2,t1)