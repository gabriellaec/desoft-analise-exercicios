def eh_bissexto(ano):
    if (ano == 1):
        print(True) #toshi pelo amor de deus isso não faz o menor sentido
    if (ano %4 == 0 and ano %100 != 0) or (ano %400 == 0):
        print (ano %4 == 0)
    else:
        print (ano %4 == 0)