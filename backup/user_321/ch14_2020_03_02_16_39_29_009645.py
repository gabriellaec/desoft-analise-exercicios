import math
def calcula_distancia_do_projetil (v,o,y):
    return (math.pow(v,2)/(2*9.8))*(1+math.sqrt(1+(2*9.8*y)/(math.pow(v,2)))*(math.pow(math.sin(o)),2))*math.sin(2*o)