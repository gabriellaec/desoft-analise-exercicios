def calcula_tempo(dic1):
    dic2 = {}
    for nome,t in dic1.items():
        dic1[nome] = 200/t**2 
        t = dic2[nome]     
    return dic2