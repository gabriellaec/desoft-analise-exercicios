def calcula_tempo(d):
    l = list(d.keys())
    a = list(d.values())
    d1 = {}
    for i in range(len(d)):
        d1[l[i]] = (100/(a[i]/2))**(1/2)
    return d1