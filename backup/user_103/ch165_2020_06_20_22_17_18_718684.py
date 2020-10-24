def mais_populoso(dicio_estados):
    lista_num =[]
    soma = 0
    for estado,outro_dicio in dicio_estados.items():
            dicio_estados[estado] = outro_dicio
            for cidade, populacao in outro_dicio.items():
                outro_dicio[cidade]= populacao 
                soma+= populacao
            lista_num.append(soma)
    for i in range(len(lista_num)):
        proximo_estado = lista_num[i+1] - lista_num[i]
        if proximo estado > lista_num[i]:
            return estado
    #for j in range(len(lista_num)):
        #soma+= lista_num[j]
    #return soma/ len(lista_num)
