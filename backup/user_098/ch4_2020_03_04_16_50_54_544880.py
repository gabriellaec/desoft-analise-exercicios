def classifica_idade(idade):
    if idade <= 11:
        print("crianca")
        return "crianca"
    elif idade >= 12 and idade <= 17:
        print("adolescente")
        return "adolescente"
    else:
        print("adulto")
        return "adulto"