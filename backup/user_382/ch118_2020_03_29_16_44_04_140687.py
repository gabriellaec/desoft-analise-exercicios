import math as m 
def reflexao_total_interna(n1,n2,teta2):
    teta2 = teta2*(m.pi/180)
	senoteta1 =(n2 * m.sin(teta2))/n1	
    if senoteta1 > 1:
        return True
    else:
        return False
        