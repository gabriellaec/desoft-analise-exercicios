def estritamente_crescente(lista):
    crescente = []
    for item in lista:
        if not item in crescente:
            crescente.append(item)

    esta_crescente = False
    i = 0
    proximo = False
    while not esta_crescente:
        for x in range(i,len(crescente)):
            if crescente[i] > crescente[x]:
                valor = crescente.pop(x)
                crescente.insert(i,valor)
                break
            if x == len(crescente)-1:
                proximo = True
        if i == len(crescente)-1:
            esta_crescente = True
        
        if proximo == True:
            i += 1
            
            proximo = False
        
    return crescente