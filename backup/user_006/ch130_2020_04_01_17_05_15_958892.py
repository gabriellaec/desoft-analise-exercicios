def monta_mala(lista1):
    lista2=[]
    total=0
    menor=True
    i=0
    while i<len(lista1) and menor:
        total= total+lista[i]
        if total<=23:
            lista.append(lista[i])
            i=i+1
        else:
            menor=False
    return lista2   
      