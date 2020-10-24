def calcula_media (lista):
    soma = 0
    quant = 0

    for dic in lista:
        notas = dic.values()
        for grade in notas:
            soma += grade 
            quant +=1
        
    media = soma/quant 
    return media