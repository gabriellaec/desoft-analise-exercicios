import math
def snell_descartes(n1,n2,teta1):
    teta2=math.degrees(math.asin(n1*math.sin(teta1)/n2))
    return teta2

#math.degrees() # radianos em graus
#math.asin() # graus em radianos