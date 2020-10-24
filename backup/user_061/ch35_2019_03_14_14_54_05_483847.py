depósito_inicial = int(input('Depósito'))
depósito_mensal = int(input('Depósito mensal'))
taxa_de_juros = int(input('Taxa'))

t = 0
while t <= 24:
    M=(depósito_inicial + depósito_mensal*t) * (1 + taxa_de_juros)**(t+1)
                    