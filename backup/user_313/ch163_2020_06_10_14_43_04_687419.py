def calcula_media (l1):
    soma = 0
    contador = 0
    for i in l1:
        for v in i.values():
           soma += v
           contador += 1
         
    return soma/contador