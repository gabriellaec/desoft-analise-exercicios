def calcula_tempo(dic):
    c={}
    for nome,acel in dic.items():
        c[nome]=(200/acel)**0.5
    return c

        
            