def verifica_idade (i):
    i = int(input('Escreve sua idade'))
    if i >= 21:
        print ('Liberado EUA')
    elif i < 18:
        print ('Não está liberado')
    else:
        print ('Liberado Brasil')