def classifica_lista(x):
    if len(x)<2:
        listacr = [x[0]]
        listadecr = [x[0]]
        maior = x[0]
        menor = x[0]
        
    for e in range (1, len(x)):
        if x[e]>maior:
            listacr.append(x[e])
            maior=x[e]
            
        if x[e]<menor:
            listadecr.append(x[e])
            menor=x[e]
            
        if listacr==x:
            return 'creceste'
        elif listadecr==x:
            return 'decrescente'
        else:
            return 'nenhum'
    else: return 'nenhuma'