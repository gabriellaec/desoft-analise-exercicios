def verifica_idade(idade):
    if verifica_idade >= 21:
        print("Liberado EUA e Brasil")
    elif verifica_idade <18:
        print("Não está liberado")
    else:
        print("Liberado Brasil")