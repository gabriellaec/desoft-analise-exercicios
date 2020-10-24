def verifica_idade(x):
   if  verifica_idade >= 21:
        return ('Liberado EUA e BRASIL')
   elif verifica_idade >= 18 and verifica_idade < 21:
        return('Liberado BRASIL')
   else:
        return ('Não está liberado')
