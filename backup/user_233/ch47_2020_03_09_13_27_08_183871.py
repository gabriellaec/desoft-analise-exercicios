def estritamente_crescente(lista):
    
    if len(lista) == 0: return []
    
    resultado = [lista[0]]
    
    ultimo = lista[0]
    
    for i in lista:
        if i == lista[0]: continue
        if i > ultimo:
            resultado.append(i)
            ultimo = i
    
    return resultado