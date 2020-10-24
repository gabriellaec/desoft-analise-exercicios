x=int(input('Sua idade: '))
def classifica_idade(idade):
    if idade >= 18:
        return 'Adulto'
    elif idade >=12:
        return "Adolescente" 
    else:
        return "crianca"

print(classifica_idade(x))