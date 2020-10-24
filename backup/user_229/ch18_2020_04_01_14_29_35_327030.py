def verifica_idade(idade):
    if int(idade) >= 21:
        print("Liberado EUA e Brasil")
    elif int(idade) < 18:
        print("Não está liberado")
    elif int(idade) in range(18,20):
        print("Liberado Brasil")