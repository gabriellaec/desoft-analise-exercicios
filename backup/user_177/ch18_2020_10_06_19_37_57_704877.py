def verifica_idade(idade):
     if idade >= 21:
         return 'Liberado EUA e BRASIL'
     else:
         if idade >= 18:
             return ' Liberado BRASIL'
         else:
             return 'Não está liberado'

print(verifica_idade(17))
print(verifica_idade(20))
print(verifica_idade(21))

        
