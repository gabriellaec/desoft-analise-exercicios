import math as m 
def reflexao_total_interna(n1,n2,teta1):
    teta1 = teta1*(m.pi/180)

    teta2 = m.asin((n1 * m.sin(teta1))/n2)

    
    if m.sin(teta2) > 1:
        return True
    else:
        return False
        