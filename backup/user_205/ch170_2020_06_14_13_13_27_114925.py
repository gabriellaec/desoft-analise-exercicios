def apaga_repetidos(palavra):
    for letra in palavra:
        contador = palavra.count(letra)
        if contador > 1 : 
            nova_palavra = palavra.replace(letra,'*')
            corrigindo = nova_palavra.replace('*',letra,1)
    return corrigindo