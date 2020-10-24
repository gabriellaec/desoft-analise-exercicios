def remove_vogais(string):
    vogais = ['a','e', 'i', 'o', 'u']
    letras = list()
    for i in string:
        letras.append(i)
        for t in vogais:
            if i==t:
                letras.remove(i)
    return ("".joint(letras))
