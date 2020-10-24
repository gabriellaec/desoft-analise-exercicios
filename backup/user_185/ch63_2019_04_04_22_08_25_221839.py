def pos_arroba(string):
    contador = 0
    while contador < len(string):
        if string[contador] == "@":
            return string[contador]
        contador = contador + 1