idade = int(input("coloque sua idade: "))

def classifica_idade(idade):
    if idade <= 11:
        return("crianca")
    if idade >= 18:
        return "adulto"
    else:
        return "adolescente"