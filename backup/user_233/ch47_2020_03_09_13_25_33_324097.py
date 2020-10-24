def estritamente_crescente(lista):
    
    resultado = lista()
    resultado.append(lista[0])
    
    ultimo = lista[0]
    
    for i in lista:
        if i == lista[0]: continue
        if i > ultimo:
            resultado.append(i)
            ultimo = i
    
    return resultado