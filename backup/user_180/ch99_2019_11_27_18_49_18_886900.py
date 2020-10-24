def login_disponivel(string, lista_string):
    if string not in lista_string:
        return string
    else:
        contador = 1
        contador_string = []
        while string not in lista_string:
            contador_string.append(lista_string.count(string+str(contador)))

        if len(contador_string) == 1:
            return string + str(contador_string)
        else:
            return string + str(contador_string+1)