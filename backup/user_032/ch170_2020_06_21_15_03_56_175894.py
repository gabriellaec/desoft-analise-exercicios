def apaga_repetidos(frase):
    palavra = []
    for x in frase:
        if x not in palavra:
            palavra.append(x)
        else:
            palavra.append('*')
    string = ''.join(palavra)
    return string