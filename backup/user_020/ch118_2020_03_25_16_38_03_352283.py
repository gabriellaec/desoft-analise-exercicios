import math
def reflexao_total_interna(n1,n2,teta2):
    x = n2*math.sin(math.radians(teta2))/n1
    y = math.sin(x)
    if y > 1:
        return True
    else:
        return False
print(reflexao_total_interna(1,2,-90))