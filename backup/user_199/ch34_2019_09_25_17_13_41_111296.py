c=int(input("digite o deposito inicial:"))
j=int(input('digite a taxa de juros:'))

lista_montante=[]
t=0
while t<24:
    
    
    m=c+(c*(j/100)*t)
    lista_montante.append(m)
    t+=1
    print('O valor no {0}° mês foi {0:.2f}'.format(t,m))

s=[]
soma=0
for i in lista_montante:
    
    s.append(soma)
    soma=soma+i
    
print ('O valor total com os juros é: {0:.2f}'.format(s[-1]))
        
        
        
        
    