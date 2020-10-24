def classifica_idade(idade):
    if idade<12:
        return("crianca")
    else:
        if idade>=12 and idade<18:
            return('adolescente')
        else:
            if idade>=18:
                return("adulto")