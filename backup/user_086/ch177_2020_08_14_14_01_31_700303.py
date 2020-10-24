def numero_digitos(s):
    lista_caracteres = list(s)
    lista_digitos = []
    n = 0
    while n < len(lista_caracteres):
        if lista_caracteres[n].isdigit() == True:
            lista_digitos.append(lista_caracteres[n])
        n+=1

    return len(lista_digitos)