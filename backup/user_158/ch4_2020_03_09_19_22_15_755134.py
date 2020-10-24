def classifica_idade (Idade):
	if idade <= 11 :
        return("crtianca")
    if 12 <= Idade <= 17 :
        return("adolescente")
    if Idade >= 18 :
        return("adulto")
    
   
print (classifica_idade (12))