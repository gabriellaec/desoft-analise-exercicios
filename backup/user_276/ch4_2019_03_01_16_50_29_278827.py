id = int(input("Qual é a sua idade?   "))
def classifica_idade(id):
    if id <= 11:
        return("Criança")
        if id <= 17:
            return("adolescente")
        else:
            return("adulto")
a = classifica_idade(id)
print(a)