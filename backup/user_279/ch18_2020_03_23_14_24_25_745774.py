def verifica_idade(idade):
    
    if idade >= 21:
        return("Liberado EUA e Brasil")
    elif 21 > idade >= 18:
        return("Liberado Brasil")
    elif 18 > idade:
        return("Não está liberado")