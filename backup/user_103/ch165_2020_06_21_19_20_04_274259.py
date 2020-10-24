def mais_populoso(dicio_estados):
    dicio_final={}
    for estado,outro_dicio in dicio_estados.items():
        dicio_estados[estado] = outro_dicio
        soma = 0
        for cidade, populacao in outro_dicio.items():
            outro_dicio[cidade]= populacao 
            soma+= populacao
            dicio_final[estado]= soma
    a=dicio_final[max(dicio_final, key=dicio_final.get)]
    return a


