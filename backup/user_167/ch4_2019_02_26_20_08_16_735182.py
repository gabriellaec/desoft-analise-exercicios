def classifica_idade(a_idade):
    if a_idade <= 11:
        return "você é um crianca"
    elif a_idade>11 and a_idade<=17:
        return "você é um adolescente"
    else: 
        return "você é um adulto"
a= int(input("digite a sua idade : "))
print(classifica_idade(a))    



    


    