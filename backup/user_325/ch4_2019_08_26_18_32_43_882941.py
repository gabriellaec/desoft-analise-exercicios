def classifica_idade(anos):
    if anos <= 11:
        print ("crianca")
    elif anos >=12 and anos <= 17:
        print ("adolescente")
    else:
        return("adulto")
anos = int(input("idade"))