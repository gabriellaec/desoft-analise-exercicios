def numero_digitos (senha):
    lista = list(senha)
    lista_2 = []
    for i in lista:
        if i.isdigit():
            lista_2.append(i)
            
    return(print(lista_2))
