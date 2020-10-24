x = int(input( ))

def classifica_idade(x):
    if x <= 11:
        return("Voce é crianca")
    elif x >= 12 and idade <= 17:
        return("Voce é adolescente")
    elif x > 18:
        return("Voce é adulto")
print(classifica_idade(x))