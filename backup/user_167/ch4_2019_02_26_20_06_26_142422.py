def classifica_idade(a_idade):
    if a_idade <= 11:
        return "você é um crianca"
    if a_idade>11 and a_idade<=17:
        return "você é um adolescente"
    if a_idade>=1718:
        return "você é um adulto"
a= int(input("digite a sua idade : "))
print(classifica_idade(a))    



    


    