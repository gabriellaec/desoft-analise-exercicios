anos = int(input("idade"))
def classifica_idade(anos):
    if anos <= 11:
        return str("crianca")
    elif anos >=12 and anos <= 17:
        return str("adolescente")
    else:
        return str("adulto")
