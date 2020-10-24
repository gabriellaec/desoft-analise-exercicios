def nome_usuario(string):
    cont = 0
    if string[cont] == "@":
        return 0
    while string[cont] != "@":
        cont += 1
    return string[0:cont]