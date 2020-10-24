def remove_vogais(n):
    lista = []
    vogais = ["a", "e", "i", "o", "u"]
    for i in n:
        if i not in vogais:
            lista.append(i)
    lista = "".join(lista)
    return lista    