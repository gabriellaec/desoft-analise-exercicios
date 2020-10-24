def junta_nomes(x,y,z):
    lista = []
    if len(x)!=0 and len(z)!=0:
        for i in x:
            for j in z:
                nova = i +' '+j
                lista.append(nova)
    if len(y)!=0 and len(z)!=0:
        for k in y:
            for l in z:
                nova1 = k +' '+l
                lista.append(nova1)
    return lista