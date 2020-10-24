def verifica_idade(idade):
    if idade < 18:
       msg='Não está liberado'
    elif idade >= 18 and idade < 21:
       msg='Liberado BRASIL'
    else:
       msg='Liberado EUA e BRASIL'
    return msg
