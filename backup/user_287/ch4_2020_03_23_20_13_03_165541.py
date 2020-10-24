def classifica_idade(x):
    x = int(input('Digite uma idade'))
    if x<11:
        return "crianca"
    elif 12<x<17:
        return "Adolescente"
    else:
        return "Adulto"
        