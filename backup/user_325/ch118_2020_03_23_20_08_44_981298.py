import math
def reflexao_total_interna(n1,n2,o1):
    a = math.radians(o1)
    b = math.sin(a)
    c = (n2/n1)* b
	if c > 1:
        return True
    else:
        return False
        