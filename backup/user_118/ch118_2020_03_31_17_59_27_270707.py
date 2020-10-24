import math
def reflexao_total_interna(n1,n2,o2):
    o1=math.sin((n2*math.sin(math.radians(o2)))/n1)
    return (o1)
if reflexao_total_interna>1:
    print(verdadeiro)
else:
    print(falso)