def conta_a(str):
    soma= 0
    i= 0
    lista_a= []
    while i < len(str):
        if str[i]== 'a':
            lista_a.append(str[i])
            i= i + 1
        else:
            i= i + 1
    return len(lista_a)