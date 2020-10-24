from math import radians
def arcotangente(x,n):
    cont = 1
    for i in range(n-4):
        arc_pos = (x**cont) / cont
        arc_neg = (x**(cont+2)) / (cont+2)
        cont += 4
        arc = arc_pos - arc_neg
        arc = radians(arc)
    return arc