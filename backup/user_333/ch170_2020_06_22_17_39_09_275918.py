def apaga_repetidos(palavra):
    letras_usadas=[]
    for i in range(len(palavra)):
        if palavra[i] not in letras_usadas:
            letras_usadas.append(palavra[i])
            print(letras_usadas)
        else:
            palavra[i]='*'
            
    saida = palavra
    print(saida)
    return saida