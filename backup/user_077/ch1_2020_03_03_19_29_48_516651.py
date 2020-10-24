#Considerando o montante inicial como 50 reais e os juros como de 5%, temos:
M=[0]*24
M[0]=50
i=1
while i<24:
   M[i]=M[i-1]*1.05
   i=i+1
print(M)