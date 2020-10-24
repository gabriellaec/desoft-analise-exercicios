def lista_caracteres(s):
    lista = list(s)
    lista_final = []
    for i in lista:
        if i in lista:
            lista_final=lista_final
        else:
            lista_final.append(i)
    return lista_final