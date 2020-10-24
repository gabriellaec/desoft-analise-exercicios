def verifica_idade(idade):
    if idade >= 21:
        print("Liberado EUA e BRASIL")
    elif idade >= 18:
        print("Liberado BRASIL")
    else:
        print("Não está liberado")


old = int(input("Qual sua idade? "))
print(verifica_idade(old))