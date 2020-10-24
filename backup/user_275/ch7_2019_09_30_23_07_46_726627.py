import math
def calcula_norma(v):
    calculo=0
    for i in range (len(v)):
        calculo+=(v[i]**2)
    final=math.sqrt(calculo)  
    return final    