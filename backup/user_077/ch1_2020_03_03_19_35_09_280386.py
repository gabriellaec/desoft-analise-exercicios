#Considerando o montante inicial como 50 reais e os juros como de 5%, temos:
calcula_valor_devido=[0]*24
calcula_valor_devido[0]=50
i=1
while i<24:
   calcula_valor_devido[i]=calcula_valor_devido[i-1]*1.05
   i=i+1
print(calcula_valor_devido)
