def apaga_repetidos(palavra):
    letras_usadas=[]
    for i in range(len(palavra)):
        if palavra[i] not in letras_usadas:
            letras_usadas.append(lista_letras[i])
            print(letras_usadas)
        else:
            palavra[i]='*'
            
    saida = ''.join(lista_letras)
    print(saida)
    return saida