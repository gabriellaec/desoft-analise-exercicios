def lista_caracteres(string)
d = {}
for letra in string:
    if letra in d:
        d[letra] = d[letra] + 1
    else:
        d[letra] = 1
    return d
   