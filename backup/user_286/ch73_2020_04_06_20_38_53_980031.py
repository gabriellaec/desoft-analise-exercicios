def remove_vogais(frase):
    lista = []
    vogais = ['a', 'e', 'i', 'o', 'u']
    for letra in frase:
        if letra not in vogais and letra not in lista:
            lista.append(letra)

    return lista