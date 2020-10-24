from math import radians
def arcotangente(x,n):
    cont = 1
    for i in range(n-2):
        arcpos = (x**cont) / cont
        arcneg = (x**(cont+2)) / (cont+2)
        cont += 4
        arc = arcpos - arcneg    
    arc = radians(arc)
    return arc