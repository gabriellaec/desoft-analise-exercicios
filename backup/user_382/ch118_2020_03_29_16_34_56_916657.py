import math as m 
def reflexao_total_interna(n1,n2,teta2):
    teta2 = teta2*(m.pi/180)

    teta1 = m.asin((n1 * m.sin(teta2))/n2)

    
    if m.sin(teta1) > 1:
        return True
    else:
        return False
        