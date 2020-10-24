import math
z=True
def reflexao_total_interna(n1,n2,x):
    y=math.asin((n1/n2)*(math.sin(math.radians(x))))
    z=math.degrees(y)
    if z>90:
        return True	
    else:
        return False

    return z

	
    
