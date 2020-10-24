def login_disponivel(string,lista):
    if string not in lista:
        return string
    else:
        v=1
    for string in lista:
        if string+f"{v}" not in lista:
            return string+f"{v}"
        else:
            v+=1