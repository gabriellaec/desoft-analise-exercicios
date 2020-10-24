idade = int(input( ))

def classifica_idade(idade):
    if idade <= 11:
        return("Voce é crianca")
    elif idade >= 12 and idade <= 17:
        return("Voce é adolescente")
    elif idade > 18:
        return("Voce é adulto")
print(classifica_idade(idade))