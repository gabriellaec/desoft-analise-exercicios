#Programa que classifica a idade
def classifica_idade(n):
    if n <= 11:
        return 'crianca'
    elif 11 < n < 17:
        return 'adolescente'
    else:
        return 'adulto'
