def mais_populoso(dicio_estados):
    dicio_final={}
    for estado,outro_dicio in dicio_estados.items():
        dicio_estados[estado] = outro_dicio
        soma = 0
        for cidade, populacao in outro_dicio.items():
            outro_dicio[cidade]= populacao 
            soma+= populacao
            dicio_final[estado]= soma
    maior= max(dicio_final, key= lambda chave:(dicio_final[chave]))
    print(dicio_final)
    #return maior



