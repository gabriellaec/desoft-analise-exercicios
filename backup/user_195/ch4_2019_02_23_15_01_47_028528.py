def classifica_idade(idade):
    if idade<=11:
        print("crianca")
    elif idade>=12 and idade<=18:
        print("adolescente")
    elif idade>=18:
        print("adulto")
print(classifica_idade(19))