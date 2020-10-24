def calcula_media(lista):
    soma = 0
    cont = 0
    for sala in lista:
        for aluno in sala:
            soma += sala[aluno]
            cont += 1
    media = soma/cont
    return media