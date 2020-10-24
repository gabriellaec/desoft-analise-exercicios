def pos_arroba(string):
    contador=0
    i=0
    if "@" in string:
        while contador<len(string):
            if string[i]!="@":
                contador+=1
                i+=1
            else:
                return contador
    else:
        return ("isso nao e um email")


def nome_usuario(x):
    z=pos_arroba(x)
    return x[:z]