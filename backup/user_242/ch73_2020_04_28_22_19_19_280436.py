def remove_vogais(string):
    vogais = ['a','e', 'i', 'o', 'u']
    letras = []
    for i in string:
        if i in vogais:
            continue
        else:
            letras.append(i)
    return ''.join(letras)

