def mais_populoso(dicio_estados):
    dicio_final={}
    for estado,outro_dicio in dicio_estados.items():
        soma = 0
        dicio_estados[estado] = outro_dicio
        for cidade, populacao in outro_dicio.items():
            outro_dicio[cidade]= populacao 
            soma+= populacao
            dicio_final[estado]= soma
    print(dicio_final)


