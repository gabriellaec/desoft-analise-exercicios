def lista_caracteres(palavra):
    letras = list()
    for i in palavra:
        if i not in letras:
            letras.append(i)
    return letras