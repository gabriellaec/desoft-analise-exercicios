def verifica_idade (idade):
 if idade < 18:
  return "Não está liberado"
 elif 18 <= idade < 21:
  return "Liberado BRASIL"
 else:
  return "Liberado EUA e BRASIL"
x = int(input('Qual a sua idade: '))
print(verifica_idade(x))
