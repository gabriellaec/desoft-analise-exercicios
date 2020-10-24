import math
def reflexao_total_interna(n2, teta2, n1):
    if n1>0:
        teta1=math.sin((n2*math.sin(math.radians(teta2)))/n1)
        return teta1
        while n1>0 and n2>=0 and teta1>=0 and teta2>=0:
            if teta1>teta2:
                return True
            else:
                return False
    