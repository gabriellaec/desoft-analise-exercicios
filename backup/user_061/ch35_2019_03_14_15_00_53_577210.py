depósito_inicial = float(input('Depósito'))
depósito_mensal = float(input('Depósito mensal'))
taxa_de_juros = float(input('Taxa'))

t = 1
while t <= 24:
    M=(depósito_inicial + depósito_mensal*(t-1)) * (1 + taxa_de_juros)**(t)
    print("Valor do montante para o {0} mes é {1:.2f}".format(i,M))
    t += 1
J = M - depósito_inicial - 24*depósito_mensal
print('{0:.2f}'.format(J))
                    