def verifica_idade(x):
    if x<18:
        return "Não está liberado"
    elif x==18:
        return "Liberado BRASIL"
    elif x>18:
        return "Liberado EUA e BRASIL"
    
        