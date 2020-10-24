def mais_populoso(brasil):
    lista_estados = []
    estados = []
    soma = 0 

    for i in brasil: 
        estados.append(i)       
        for j in brasil[i]:
            for k in brasil[i][j]:
                k = float(k)
                soma = soma + k
        lista_estados.append(soma)

    mais_pop = 0
    z = 0
    while z < len(lista_estados)-1:
        if lista_estados[z]>mais_pop:
            mais_pop = lista_estados[z]
    x = lista_estados.index(mais_pop)
    return estados[x]