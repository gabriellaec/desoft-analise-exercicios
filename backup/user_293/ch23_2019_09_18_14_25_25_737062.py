def verifica_idade(idade):
    if idade < 18:
        return "Não está liberado"
    elif idade >= 18 or idade < 21:
        return "Liberado BRASIL"
    else:
        return "Não está liberado"
 
