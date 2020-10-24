def classifica_idade (Idade):
	if Idade < 12 :
        return('crianca')
    if 12 <= Idade <= 17 :
        return('adolescente')
    if Idade >= 18 :
        return('adulto')
    
   
 print(classifica_idade (12))