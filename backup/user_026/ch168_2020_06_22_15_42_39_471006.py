def login_disponivel(s, lista):
    string = ""
    cont = 0
    if lista == []:
        return s
    for i in lista:
        if s in lista:
            if i == s + str(string) or i == s + str(cont):
                cont = cont + 1
        else:
            return s
    return s+ str(cont)