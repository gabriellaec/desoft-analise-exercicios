def calcula_tempo(dic1):
    dic2={}
    for i in dic1:
        dic2[i]=((100/dic1[i])**(1/2))
    return dic2
    