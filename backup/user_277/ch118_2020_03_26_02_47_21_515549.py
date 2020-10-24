import math
def reflexao_total_interna(n1,n2,o2):
    o2=math.asin((math.sin(o1*math.pi/180)*n1)/n2)
	if math.sin(o2)>=1:
        reflexao_total_interna=True
    else:
        reflexao_total_interna=False