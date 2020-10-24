idade = int(input('quala a sua idade '))
def classifica_idade(idade):
    if idade<=11:
        return 'crianca'
    elif 11<idade<18:
        return 'adolescente'
    elif idade>=18:
        return 'adulto'
print(classifica_idade(idade))