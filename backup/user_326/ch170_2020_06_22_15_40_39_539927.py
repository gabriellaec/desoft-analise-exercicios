def apaga_repetidos(string):
    lista_letras = {}
    for character in string:
        if character in lista_letras:
            lista_letras[character] += 1
        else: 
            lista_letras[character] = 1
    string = string[::-1]
    for key, value in lista_letras.items():
        string = string.replace(str(key), '*', value -1)
    return string[::-1]
