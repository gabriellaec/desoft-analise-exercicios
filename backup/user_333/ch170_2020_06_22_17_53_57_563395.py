def apaga_repetidos(palavra):
    lista_letras = [char for char in palavra]
    letras_usadas=[]
    for i in range(len(lista_letras)):
        if lista_letras[i] not in letras_usadas:
            letras_usadas.append(lista_letras[i])
            print(letras_usadas)
        else:
            palavra[i]='*'
            
    saida = ''.join(lista_letras)
    print(saida)
    return saida