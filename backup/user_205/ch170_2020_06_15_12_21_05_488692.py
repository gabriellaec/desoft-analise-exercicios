def apaga_repetidos(palavra):
    for letra in palavra:
        contador = palavra.count(letra)
        espaco = palavra.count('')
        if contador > 1 or espaco > 1:
            #Troca todas letras repetidas por * 
            palavra = palavra[::-1].replace(letra,'*', contador-1)
            print(palavra)
    return palavra
