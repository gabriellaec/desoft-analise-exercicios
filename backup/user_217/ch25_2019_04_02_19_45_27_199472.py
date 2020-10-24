a=int(input('Qual a distancia percorida: '))
if a <= 200:
   preco_da_passagem= a * 0.5 
   print('Preço da passagem é {0:.2f}'.format(preco_da_passagem))
elif a > 200:
   preco_da_passagem= 100 + (a*0.5)
   print('Preço da passagem é {0:.2f}'.format(preco_da_passagem))
