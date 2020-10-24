import math as m 
def snell_descartes(n1,n2,teta1):
    teta1 = teta1*(m.pi/180)

    teta2 = m.asin((n1 * m.sin(teta1))/n2)

    return teta2

def reflexao_total_interna(teta2):
    if m.sin(snell_descartes(teta2)) > 1:
        return True
    else:
        return False
        