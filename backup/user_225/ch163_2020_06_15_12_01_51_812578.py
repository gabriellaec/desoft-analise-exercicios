def calcula_media(lista):
    soma = 0
    contador = 0
    for dic in lista:
        for i  in dic:
            soma+=dic[i]
            contador+=1
    media = soma/contador
    return media