def apaga_repetidos(palavra):
    lista_letras=palavra.split()
    letras_usadas=[]
    for i in lista_letras:
        if lista_letras[i] not in letras_usadas:
            letras_usadas.append(lista_letras[i])
        else:
            lista_letras[i]='*'
            
    saida = lista_letras.join()
    print(saida)
    return saida