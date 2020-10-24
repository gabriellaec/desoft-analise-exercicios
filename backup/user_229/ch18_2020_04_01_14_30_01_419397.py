def verifica_idade(idade):
    if int(idade) >= 21:
        print("Liberado EUA e Brasil")
    elif int(idade) in range(18,20):
        print("Liberado Brasil")
    else:
        print("Não está liberado")
   