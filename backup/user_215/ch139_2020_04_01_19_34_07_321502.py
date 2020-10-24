def arcotangente(x,n):
    cont = 1
    for i in range(n):
        arc_pos = (x**cont) / cont
        arc_neg = (x**(cont+2)) / (cont+2)
        cont += 2
        arc = arc_pos + arc_neg
    return arc