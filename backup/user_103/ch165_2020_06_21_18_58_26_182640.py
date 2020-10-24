def mais_populoso(dicio_estados):
    lista_num =[]
    for estado,outro_dicio in dicio_estados.items():
            dicio_estados[estado] = outro_dicio
            soma = 0
            for cidade, populacao in outro_dicio.items():
                outro_dicio[cidade]= populacao 
                soma+= populacao
            lista_num.append(soma)
    print(lista_num)
