
idade = int(input('Insira sua idade '))
def classifica_idade(idade):
    if idade <= 11:
        print("crianca")
        return "a"
    elif idade <= 17:
        print("adolescente")
        return "a"
    else:
        print("adulto")
        return "a"
classifica_idade(idade) 