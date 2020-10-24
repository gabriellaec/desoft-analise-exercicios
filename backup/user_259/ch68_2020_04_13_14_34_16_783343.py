def separa_trios(lista):
    lista_grupos = []
    grupo = []
    i = 0
    while i<len(lista):
        grupo.append[i]
        if len(grupo) == 3:
            lista_grupos.append(grupo)
            grupos = []
            i+=1
        elif grupo[len(grupo)-1] == lista[len(lista)]:
            lista_grupos.append(grupo)
            return lista_grupos
        i+=1
    return lista_grupos
            