def junta_nomes(h,m,s):
    nc=[]
    for i in h:
        for x in s:
            nc.append(i+" "+x)
    for y in m:
        for z in s:
            nc.append(y+" "+z)
    return nc