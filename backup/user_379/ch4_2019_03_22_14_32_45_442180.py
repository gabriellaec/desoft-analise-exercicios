def classifica_idade(idade):
    if idade<=11:
        print("crianca")
    elif idade>11 and idade<=17:
        print('adolescente')
    else:
        print("adulto")
    return classifica_idade
print(classifica_idade(10))