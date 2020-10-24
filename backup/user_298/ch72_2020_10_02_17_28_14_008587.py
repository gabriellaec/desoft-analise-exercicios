def lista_caracteres(palavra):
    lista_letras = []
    t = 0
    while t < len(palavra):
        lista_letras.append(palavra[t])
        t += 1
    return lista_letras