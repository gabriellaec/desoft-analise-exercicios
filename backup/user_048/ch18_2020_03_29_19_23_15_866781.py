def verifica_idade(x):
    b=18
    e=21
    if x>=b and x>=e:
        print("Liberado EUA e BRASIL")
    elif x>=b and x<e:
        print("Liberado BRASIL")
    else:
        print("Não está liberado")
x=10
print(verifica_idade(x))
    