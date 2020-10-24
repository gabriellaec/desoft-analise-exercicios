def calcula_media(lista):
    num = 0
    tot = 0
    for dict in lista:
        for i in dict:
            num += 1
            tot += dict[i]
    return tot/num