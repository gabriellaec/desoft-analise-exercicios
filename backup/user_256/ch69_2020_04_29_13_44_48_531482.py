def junta_listas(listas):
    nova = []
    i = 0
    while i < len(listas):
        for numeros in listas[i]:
            nova.append(numeros)
        i+=1
    return nova
    
