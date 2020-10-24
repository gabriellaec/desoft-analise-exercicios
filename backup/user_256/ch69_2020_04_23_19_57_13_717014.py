def junta_listas(listas):
    nova = []
    i = 0
    while i < len(listas[i]):
        for numeros in listas[i]:
            if not numeros in nova:
                nova.append(numeros)
            i+=1
    return nova
    
