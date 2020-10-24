def remove_vogais(string):
    vogais = ['a','e', 'i', 'o', 'u']
    letras = []
    for i in string:
        if i not in vogais:
            letras.append(i)
    return ''.join(letras)

