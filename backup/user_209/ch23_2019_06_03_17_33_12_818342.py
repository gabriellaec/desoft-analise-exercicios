def verifica_idade (maioridade):
    if maioridade >= 18 and maioridade < 21:
        print ("Liberado BRASIL")
    elif maioridade >= 21:
        print ("Liberado EUA e BRASIL")
    elif maioridade < 18 and maioridade > 0:
        print ("Não está liberado")
    