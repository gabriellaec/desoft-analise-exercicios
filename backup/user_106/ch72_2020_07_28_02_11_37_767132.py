def lista_caracteres(texto):
    nova = []
    for i in texto:
        if not i in nova:
            nova.append(i)
    return nova