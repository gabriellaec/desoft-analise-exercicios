def verifica_idade(idade):
    if int(idade) >= 21:
        print("Liberado EUA e BRASIL")
    elif int(idade) >= 18:
        print("Liberado BRASIL")
    else:
        print("Não está liberado.")
   