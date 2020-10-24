def verifica_progressao(p):
    a = []
    cond = True
    for n in range(2,len(p)):
        if p[n]/p[n-1] == p[n-1]/p[n-2] and p[n]-p[n-1] == p[n-1]-p[n-2]:
            a.append("AG")
        elif p[n]/p[n-1] == p[n-1]/p[n-2] and p[n]-p[n-1] != p[n-1]-p[n-2]:
            a.append("PG")
        elif p[n]/p[n-1] != p[n-1]/p[n-2] and p[n]-p[n-1] == p[n-1]-p[n-2]:
            a.append("PA")

    c = a[0]

    for item in a:
        if item != c:
            cond = False
            break

    if cond == False:
        return("NA")
    else:
        return(c)
