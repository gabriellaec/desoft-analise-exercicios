import math
def calcula_elongacao(a,to,m,t):
    x=a*math.cos((math.radians(to))+math.radians(m)*t)
    return(x)