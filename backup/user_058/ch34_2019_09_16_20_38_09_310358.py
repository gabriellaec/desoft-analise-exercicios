x=float(input("Qual o valor do deposito? "))
y=float(input("Qual a taxa de juros? "))
m=1
valor = x
while m<25:
    valor=valor*(1+y)
    print('{0:.2f}'.format(valor))
    m+=1
    
print('{0:.2f}'.format(valor - x))