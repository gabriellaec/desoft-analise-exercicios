v=int(input('Qual a sua velocidade? '))
if v>80:
   print ('{:.2f}'.format(v-80)*5)
else:
   print ('Não foi multado')