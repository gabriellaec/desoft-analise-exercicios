def classifica_idade (Idade):
    if Idade <= 11:
        clase = "crianca" 
    elif Idade <= 17 and Idade >= 12:
        clase = "adolescente"
    else Idade >= 18 :
        clase = "adulto"
    return clase
print (classifica_idade (12))