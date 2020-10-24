def calcula_media(lista):
    soma = 0 
    num = 0 
    for i in lista:
        for t in i.values():
            soma += t 
            num += 1
    return soma/num 
   