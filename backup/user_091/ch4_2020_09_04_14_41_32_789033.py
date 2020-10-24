def classifica_idade(idade):
   if idade <= 11:
    return ('crianca')
   if 12<=idade<=17:
    return('adolescente')
   if 18<=idade:
    return('adulto')
    
a= 13
b=classifica_idade(a)
print(b)