
def classifica_idade(idade):
    
    if idade <= 11:
        return("crianca")
        
    if 11 < idade < 18:
        return("adolescente")
    if idade >= 18:
        return("adulto")