def verifica_idade(x):
    if x<18:
        return "Não está liberado"
    elif x==18 or x==19 or x==20:
        return "Liberado BRASIL"
    else:
        return "Liberado EUA e BRASIL"
    
        