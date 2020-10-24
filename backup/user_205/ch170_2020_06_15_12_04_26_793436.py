def apaga_repetidos(palavra):
    for letra in palavra:
        contador = palavra.count(letra)
        if contador > 1:
            #Troca todas letras repetidas por * 
            palavra = palavra.replace(letra,'*')
            #Substitui apenas uma por *
            palavra = palavra.replace('*',letra,1)
    return palavra