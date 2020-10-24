def lista_sufixos(n):
    i=0
    l=[]
    while i<len(n):
        l.append(n[i:])
        i+=1
    return l