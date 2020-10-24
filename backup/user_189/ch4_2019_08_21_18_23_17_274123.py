def classifica_idade(idade):
    if idade<0:
        return ("idade invalida")
    elif idade<=11:
        return ("crianca")
    elif idade<=17:
        return ("adolescente")
    else:
        return ("adulto")

idade=int(input("digite sua idade: "))
print(classifica_idade(idade))

