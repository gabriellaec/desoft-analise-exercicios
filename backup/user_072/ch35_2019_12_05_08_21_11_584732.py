deposito_inicial = float(input('Qual o seu deposito inicial '))
adição_mes_a_mes = float(input('qual a adiiçao por mes '))
taxa_juros = float(input('qual a taxa de juros ao mes '))

i = 0 

valor_total = deposito_inicial
while i < 24:
    
    valor_total *= (1 + taxa_juros)
    
    valor_total = valor_total + adição_mes_a_mes  
    print('{0:.2f}'.format(valor_total))
    i = i + 1
x = valor_total-(deposito_inicial+adição_mes_a_mes*24)

print('{0:.2f}'.format(x))
    