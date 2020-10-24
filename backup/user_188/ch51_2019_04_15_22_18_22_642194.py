def estritamente_crescente(lista):
    resultado = []
    resultado.append(lista[0])
    teste = lista[0]
    First = True
    
    for i in lista:
        if First:
            First = False
        elif i > teste:
            resultado.append(i)
            teste = i
    return resultado
           