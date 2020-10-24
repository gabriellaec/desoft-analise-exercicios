def classifica_idade(idade_do_usuario):
    if idade_do_usuario >= 18:
        return 'adulto'
    elif idade_do_usuario >=12:
        return 'adolescente'
    else:
        return 'crianca'