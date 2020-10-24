def classifica_idade(x):
    if x>=0 and x<=11:
        return 'crianca'
    elif x>=12 and x<= 17:
        return 'adolescente'
    elif x>= 18:
        return 'adulto'
    else:
        return 'nao existe idade negativa'

idade= int(input('Insira sua idade: '))
print(classifica_idade(idade))