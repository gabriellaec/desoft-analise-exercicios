def inverte_lista(lista):
    nova = []
    i = 0
    for a in range(len(lista),0,-1):
        nova[i] = lista[a]
        nova.append(nova[i])
        i += 1
    return nova
        
        
        
