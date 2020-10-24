def classifica_idade(age):
    if age<=11:
        return 'crianca'
    elif age>=12 and age<18:
        return 'adolescente'
    else:
        return 'adulto'