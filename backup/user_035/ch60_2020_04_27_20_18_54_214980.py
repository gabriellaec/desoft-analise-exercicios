def eh_palindromo(string):
    contador = True
    e = 0
    while contador:
        if string[e]==len(string)-e:
            contador = True
            e =+ 1
        else:
            contador = False
    return contador