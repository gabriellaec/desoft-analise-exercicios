def classifica_lista(lista_n):
    if len(lista_n)<2:
        return "nenhum"
    x=[]
    y=[]
    x.append(lista_n[0])
    y.append(lista_n[0])
    for k in range(len(lista_n)-1):
        while True:
            if lista_n[k+1]>x[k]:
                x.append(lista_n[k+1])
            elif lista_n[k+1]<y[k]:
                y.append(lista_n[k+1])
            break
    if x[-1]==lista_n[-1]:
        return "crescente"
    elif y[-1]==lista_n[-1]:
        return "decrescente"
    else:
        return "nenhum"