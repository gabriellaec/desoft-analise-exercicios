def mais_populoso(dicio_estados):
    lista_num =[]
    soma = 0
    dicio_estados[estado] = outro_dicio
    for estado,outro_dicio in dicio_estados.items():
        for cidade, populacao in outro_dicio.items():
            outro_dicio[cidade]= populacao 
            soma+= populacao
        lista_num.append(soma)
        print(lista_num)

    #for j in range(len(lista_num)):
        #soma+= lista_num[j]
    #return soma/ len(lista_num)
