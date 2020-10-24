def apaga_repetidos(texto):
    caracteres = []
    nova_palavra = ""
    for i in texto:
        if i not in caracteres:
            caracteres.append(i)
            nova_palavra = nova_palavra + i
        else:
            nova_palavra = nova_palavra + "*"
    return nova_palavra