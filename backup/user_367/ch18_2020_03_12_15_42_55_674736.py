x=int(input('Sua idade: '))
def verifica_idade(idade):
    if idade >= 21:
        return 'Maior nos Eua e no Brasil'
    elif idade >= 18:
        return "Maior no Brasil" 
    else:
        return "menor de idade"

print(verifica_idade(x))
