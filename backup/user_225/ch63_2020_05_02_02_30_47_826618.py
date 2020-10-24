def nome_usuario(string):
    i = 0
    for e in string:
        if e == "@":
            break
        i+=1
    a = string[:i:]
    return a