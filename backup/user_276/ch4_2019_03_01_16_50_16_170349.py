id = int(input("Qual é a sua idade?   "))
def classifica_idade(idade):
    if idade <= 11:
        return("Criança")
        if idade <= 17:
            return("adolescente")
        else:
            return("adulto")
a = classifica_idade(idade)
print(a)