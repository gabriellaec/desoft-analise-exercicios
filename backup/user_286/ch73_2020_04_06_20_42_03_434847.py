def remove_vogais(frase):
    lista = []
    vogais = ['a', 'e', 'i', 'o', 'u']
    for letra in frase:
        if letra not in vogais:
            lista.append(letra)

    frase = ''.join(lista)

    return frase