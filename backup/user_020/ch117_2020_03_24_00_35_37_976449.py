import math
def snell_descartes(n1,n2,t1):
    x = (n1*math.sin(math.radians(t1)))/n2
    y = math.sin(x)
print(snell_descartes(10,20,30))
    