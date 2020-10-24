def lista_sufixos(stg):
    ls=[]
    i=0
    while len(stg)!=len(ls):
        ls.append(stg[i:])
        i+=1
    return ls