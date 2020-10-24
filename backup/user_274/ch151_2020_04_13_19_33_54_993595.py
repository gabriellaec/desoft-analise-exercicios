def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    n = len(lista)
    i=1
    while i < n:
        if list[i-1] < list[i]:
            key = "c"
            i=i+1
        else:
            key = "n"
            break
    while i < n:
        if list[i-1] > list[i]:
            key = "i"
            i=i+1
        else:
            key = "n"
            break       
    if key == "c"
        return "crescente"
    elif key == "i":
        return "decrescente"
    else:
        return "nenhum"