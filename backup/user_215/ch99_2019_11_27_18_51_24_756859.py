def login_disponivel(string, lista):
    if string not in lista:
        return string
    if string in lista:
        repetido = lista.index(string)
        i = 1
        if len(lista[repetido]) == len(string) and string + "1" not in lista:
            return string + i
        if string + "1" in lista:
            i += 1
            i = str(i)
            return string + i