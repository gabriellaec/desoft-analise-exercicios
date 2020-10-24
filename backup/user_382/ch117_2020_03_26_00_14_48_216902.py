import math as m 
def snell_descartes(n1,n2,teta1):
    teta1 = teta1*(m.pi/180)

    teta2 = m.asin((n1 * m.sin(teta1))/n2)

    teta2 = teta2*(180/m.pi)

    return teta2

print(snell_descartes(1,2,30))