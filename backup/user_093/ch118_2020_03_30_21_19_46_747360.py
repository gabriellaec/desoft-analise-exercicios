import math

def reflexao_total_interna(n1,n2,x):
    y=(math.asin((n1/n2)*(math.sin(math.radians(x)))))
    z=math.degrees(y)
    r=z+x
    if r>1 :
        return True	
    else:
        return False

    

    