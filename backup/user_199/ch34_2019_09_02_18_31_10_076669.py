c=int(input("digite o deposito inicial:"))
j=int(input('digite a taxa de juros:'))

lista_montante=[]
t=0
while t<24:
    
    t+=1
    m=c+(c*(j/100)*t)
    lista_montante.append(m)
    print('O valor no {0}° mês foi {0:.2f}'.format(t,m))

s=[]
soma=0
for i in lista_montante:
    soma = soma + i
    s.append(soma)
    
print ('O valor total com os juros é: {0:.2f}'.format(s[-1]))
        
        
        
        
    