def classifica_lista(lista_n):
    if len(lista_n)<2:
        return "nenhum"
    x=lista_n[0]
    y=lista_n[0]
    for k in range(len(lista_n)-1):
        while True:
            if lista_n[k+1]>x:
                x=lista_n[k+1]
            elif lista_n[k+1]<x:
                menor=lista_n[k+1]
            break

    if x==lista_n[-1]:
        return "crescente"
    elif y==lista_n[-1]:
        return "decrescente"
    else:
        return "nenhum"
    