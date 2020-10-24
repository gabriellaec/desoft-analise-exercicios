def monta_mala(lista1):
    lista2=[]
    total=0
    menor=True
    i=0
    while i<len(lista1) and menor:
        total= total+lista1[i]
        if total<=23:
            lista2.append(lista1[i])
            i=i+1
        else:
            menor=False
    return lista2   
      