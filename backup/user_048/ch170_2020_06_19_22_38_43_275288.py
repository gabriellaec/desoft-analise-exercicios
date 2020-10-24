def apaga_repetidos(string):
    lista_todas=[]
    for letra in string:
        if letra.lower() in lista_todas or letra.upper() in lista_todas:
            lista_todas.append('*')
        else:
            lista_todas.append(letra)
    palavra=''
    for element in lista_todas:
        palavra+=element
    return palavra