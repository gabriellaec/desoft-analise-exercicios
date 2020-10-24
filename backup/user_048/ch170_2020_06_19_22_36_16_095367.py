def apaga_repetidos(string):
    lista_todas=[]
    string=string.lower()
    for letra in string:
        if letra in lista_todas:
            lista_todas.append('*')
        else:
            lista_todas.append(letra)
    palavra=''
    for element in lista_todas:
        palavra+=element
    return palavra