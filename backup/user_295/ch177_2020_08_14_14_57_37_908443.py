def numero_digitos (s):
    lista = list(s)
    lista_2 = []
    for i in lista:
        if i.isdigit():
            lista_2.append(i)
            
    return(lista_2)
