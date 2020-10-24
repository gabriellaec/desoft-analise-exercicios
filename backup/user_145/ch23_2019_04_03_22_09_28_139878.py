def verifica_idade(idade):
    if 18 <= idade >= 21:
        return "Liberado EUA e BRASIL"

    if 18 <= idade < 21:
        return "Liberado BRASIL"
    else:
        return "Não está liberado"
        
      