def apaga_repetidos(texto):
    lista=""
    for i in texto:
        if i in lista:
            lista+="*"
        else:
            lista+=i
    return lista
    