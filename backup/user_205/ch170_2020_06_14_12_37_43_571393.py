def apaga_repetidos(palavra):
    for letra in palavra:
        palavra2 = palavra.count(letra)
        if palavra2 > 1 : 
            x = palavra.index(letra)
            nova_palavra = palavra[x+1:].replace(letra,'*', palavra2-1)
            adicionando = letra + nova_palavra
    return adicionando