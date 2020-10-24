def verifica_idade (maioridade):
    if maioridade >= 18 and < 21:
        print ("Liberado BRASIL")
    elif maioridade >= 21:
        print ("Liberado EUA e BRASIL")
    else:
        print ("Não está liberado")
    