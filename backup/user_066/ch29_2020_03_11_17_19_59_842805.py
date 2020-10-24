deposito_inicial= int(input('Qual o deposito inicial? '))
taxa_de_juros = 0.01*int(input('Qual a taxa de juros? '))
mes = 0
while mes <24:
    mes += 1
    valor_atual = deposito_inicial*(1+taxa_de_juros)**mes
    ganho_do_mes= valor_atual-deposito_inicial*(1+taxa_de_juros)**(mes-1)
    print(ganho_do_mes) 
print(valor_atual)