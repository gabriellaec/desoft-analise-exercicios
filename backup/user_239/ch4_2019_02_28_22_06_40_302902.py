def classifica_idade(x):
    if 0<=x<=11:
        return 'crianca'
    elif 12<=x<=17:
        return 'adolescente'
    else:
        return 'adulto'    
     
print (classifica_idade(x)) 