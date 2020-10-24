import math
def reflexao_total_interna(n1,n2,o2):
    o2=math.asin((math.sin(o1*math.pi/180)*n1)/n2)
    return o2
	if o2>=math.asin(1):
        reflexao_total_interna=False
    else:
        reflexao_total_interna=True