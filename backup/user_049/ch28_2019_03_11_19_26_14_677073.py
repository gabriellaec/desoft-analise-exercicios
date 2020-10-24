v=int(input('Qual a sua velocidade? '))
if v>80:
   v1=(v-80)*5
   print ('{0:.2f}'.format(v1))
else:
   print ('Não foi multado')