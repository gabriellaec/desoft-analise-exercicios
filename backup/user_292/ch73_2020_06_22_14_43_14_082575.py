def remove_vogais(palavras):
    lista = []
    for i in palavras:
        lista.append(i)
    for i in lista:
        if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            lista.remove(i)
    return lista