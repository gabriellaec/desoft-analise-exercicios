def classifica_lista(lista_n):
    if len(lista_n)<2:
        return "nenhum"
    maior=lista_n[0]
    menor=lista_n[0]
    for k in range(len(lista_n)-1):
        while True:
            if lista_n[k+1]>maior:
                maior=lista_n[k+1]
            elif lista_n[k+1]<menor:
                menor=lista_n[k+1]
            break

    if maior==lista_n[-1]:
        return "crescente"
    elif menor==lista_n[-1]:
        return "decrescente"
    else:
        return "nenhum"