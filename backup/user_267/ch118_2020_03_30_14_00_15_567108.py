import math.sin
def reflexao_total_interna(n1,n2,teta2):
	sin_teta1=(sin(teta2)*n2)/n1
	if sin_teta1>1:
		return True
	else:
		return False
        