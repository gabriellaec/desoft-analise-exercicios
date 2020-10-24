def apaga_repetidos(palavra):
    for letra in palavra:
        contador = palavra.count(letra)
        if contador > 1:
            palavra = palavra.replace(letra,'*')
            palavra = palavra.replace('*',letra, 1)
            
    return palavra
