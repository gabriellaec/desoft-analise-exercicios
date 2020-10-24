def calcula_media(lista):
    soma = 0 
    n = 0
    for i in range(0,len(lista)):
        for t,m in lista[i].items():
            soma +=m
            n+=1
    media = soma/n
    return media