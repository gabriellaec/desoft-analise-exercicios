def lista_sufixos(st):
    lista=[]
    a = len(st)
    for i in range(a):
        lista.append(st[i:])
        
    return lista