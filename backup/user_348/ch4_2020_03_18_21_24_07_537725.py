classifica_idade = int(input('Qual a sua idade'))
if classifica_idade <= 11:
   return 'crianca'
else:
   if classifica_idade <= 17:
      return 'adolecente'
   else:
      return 'adulto'