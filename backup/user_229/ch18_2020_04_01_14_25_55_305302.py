def verifica_idade(idade):
    if idade >= 21:
        print("Liberado EUA e Brasil")
    elif idade <18:
        print("Não está liberado")
    else:
        print("Liberado Brasil")