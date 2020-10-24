def verifica_idade(idade):
    if idade >= 18 and idade < 21:
       return "Liberado BRASIL"
    if idade >= 21:
       return "Liberado EUA e BRASIL"
    if idade >= 1 and idade <= 17:
       return "Não está liberado"