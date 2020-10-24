def classifica_idade(jaca):
    if jaca<=11:
        return 'criança' 
    elif jaca>=12 and jaca<=17:
        return 'adolescente'
    else:
        return 'adulto'