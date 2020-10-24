def apaga_repetidos(palavra):
    for letra in palavra:
        contador = palavra.count(letra)
        if contador > 1:
            #Troca todas letras repetidas por * 
            palavra = palavra[::-1].replace(letra,'*', contador-1)
            
    return palavra[::-1]
