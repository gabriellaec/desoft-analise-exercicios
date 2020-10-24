def apaga_repetidos(palavra):
    lista_letras=palavra.split()
    letras_usadas=[]
    for i in range(len(lista_letras)):
        if lista_letras[i] not in letras_usadas:
            letras_usadas.append(lista_letras[i])
        else:
            lista_letras[i]='*'
            
    saida = ''.join(lista_letras)
    print(saida)
    return saida