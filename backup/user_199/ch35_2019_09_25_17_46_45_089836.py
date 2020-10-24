dm=float(input('digite seu deposito mensal:'))
di=float(input('digite seu deposito inicial:'))
i=float(input('digite sua taxa de juros:'))


lm=[]
t=0
while t<24:
    
    m=di+(dm*(i/100)*t)
    lm.append(m)
    t+=1
    print('O montante do mês é: {0:.2f}'.format(m))

soma=0    
for e in lm:
    soma=soma+e
print ('A soma de todos os montantes é: {0:.2f}'.format(soma))