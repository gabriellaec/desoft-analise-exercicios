def calcula_tempo(dic1):
    dic={}
    for i,u in dic1.items():
        t=(200/u)**0.5
        dic[i]=t
        return dic