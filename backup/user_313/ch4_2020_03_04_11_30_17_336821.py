def classifica_idade(x):

    if(x <=11):
        return("crianca")
    else:
        if(x>=12 and x<=17):
            return("adolescente")
    if(x>18):
        return("Adulto")

print(classifica_idade(50))