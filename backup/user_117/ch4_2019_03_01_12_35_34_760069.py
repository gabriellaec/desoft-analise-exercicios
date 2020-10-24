def classifica_idade(idade):
    if int(idade)<=11:
        return 'crianca'
    elif int(idade)>=12 and int(idade)<=17:
        return 'adolescente'
    elif int(idade)>=18:
        return 'adulto'
        
