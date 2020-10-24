def nome_usuario(string):
    i = 0
    for e in string:
        if e == "@":
            return string[: i]
        i += 1