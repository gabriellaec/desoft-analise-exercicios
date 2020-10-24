def subtracao_de_listas(lista1, lista2):
    resultado = []
    i = 0
    if lista1 == []:
        resultado=[]
    if lista2 == []:
        resultado=[]
    while i <= len(lista1):
        if i not in lista2:
            resultado.append(lista1[i])
    return resutado
        