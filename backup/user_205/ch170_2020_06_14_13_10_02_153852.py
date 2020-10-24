def apaga_repetidos(palavra):
    for letra in palavra:
        palavra2 = palavra.count(letra)
        print(palavra2)
        if palavra2 >= 1 : 
            nova_palavra = palavra.replace(letra,'*', palavra2)
            corrigindo = nova_palavra.replace('*',letra,1)
    return corrigindo