def segundos_entre(h1, h2):
    d = h1[:2]
    d = int(d)
    a = h1[3:5]
    a = int(a)
    c = h1[6:8]
    c = int(c)
    l = h2[:2]
    l = int(l)
    k = h2[3:5]
    k = int(k)
    i = h2[6:8]
    i = int(i)
    segundos1 = (d*3600)+(a*60)+(c)
    segundos2 = (l*3600)+(k*60)+(i)
    segundos3 = segundos2 - segundos1
    segundos3 = int(segundos3)
    return segundos3