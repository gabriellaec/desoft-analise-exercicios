def eh_crescente(a):
    s = 0
    for i in range(a[1], a[len(a)]):
        if i > a[s]:
            r = True
        else:
            r =  False
    return r