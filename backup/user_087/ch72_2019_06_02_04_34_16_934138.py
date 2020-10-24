def lista_caracteres(palavra):
    lista_letras = []
    for letra in palavra:
        lista_letras.append(letra)
    lista_letras1 = list(set(lista_letras))
    return lista_letras1