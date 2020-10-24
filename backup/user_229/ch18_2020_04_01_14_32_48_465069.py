def verifica_idade(idade):
    if int(idade) >= 21:
        print("Liberado EUA e Brasil")
    elif int(idade) >= 18:
        print("Liberado Brasil")
    else:
        print("Não está liberado")
   