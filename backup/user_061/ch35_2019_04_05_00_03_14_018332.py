depósito_inicial = float(input('Depósito'))
depósito_mensal = float(input('Depósito mensal'))
taxa_de_juros = float(input('Taxa'))

M = depósito_inicial*(1+taxa_de_juros)
    
t = 1
while t <= 24:
    M=(depósito_inicial + depósito_mensal*t) * (1 + taxa_de_juros)**(t+1)
    print("Valor do montante para o {0} mes é {1:.2f}".format(t,M))
    t += 1
J = M - depósito_inicial - 24*depósito_mensal
print('{0:.2f}'.format(J))