def remove_vogais(palavras):
    lista = []
    for i in palavras:
        lista.append(i)
    for i in lista:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            lista.remove(i)
    return "".join(lista)