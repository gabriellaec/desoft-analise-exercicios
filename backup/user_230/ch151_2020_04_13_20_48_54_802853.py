def classifica_lista(lista_n):
    if len(lista_n)<2:
        return "nenhum"
    a=[0]*len(lista_n)
    b=[0]*len(lista_n)
    a[0]=lista_n[0]
    b[0]=lista_n[0]
    for k in range(len(lista_n)-1):
        for k in range(len(a)):
            for k in range(len(b)):
                while True:
                    if lista_n[k+1]>a[k]:
                        a.append(lista_n[k+1])
                    elif lista_n[k+1]<b[k]:
                        b.append(lista_n[k+1])
                    break
    if a[-1]==lista_n[-1]:
        return "crescente"
    elif b[-1]==lista_n[-1]:
        return "decrescente"
    else:
        return "nenhum"