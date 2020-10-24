def verifica_idade(x):
    if idade < 18:
        print("Não está liberado")
    elif idade < 21:
        print("Liberado BRASIL")
    else:
        print("Liberado EUA e BRASIL")

idade = int(input())

ver = verifica_idade(idade)

print(ver)