def classifica_idade(idade):
    if idade<=11:
        msg='crianca'
    elif idade>=12 and idade<=17:
        msg='adolescente'
    else:
        msg='adulto'
    return msg