idade=int(input('Qual a sua idade:'))
def classifica_idade(idade):
    if 0 <= idade <= 11:
        return 'crianca'
    elif 12 <= idade <=17:
        return 'idade'
    else:
        return 'adulto'