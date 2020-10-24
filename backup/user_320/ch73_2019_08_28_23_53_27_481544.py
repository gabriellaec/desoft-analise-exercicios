def remove_vogais(string):
    lista = []
    for letra in string:
        if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
            lista.append(letra)
    return ''.join(lista)