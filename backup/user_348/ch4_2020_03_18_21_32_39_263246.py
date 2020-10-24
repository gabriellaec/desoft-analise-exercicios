def classifica_idade(idade):
    if idade <= 11:
       return 'crianca'
    else:
       if idade <= 17:
           return 'adolecente'
       else:
           return'adulto'