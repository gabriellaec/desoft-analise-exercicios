valor_da_casa = int(input('Qual o valor da casa?'))
salario = int(input('Qual o seu salario?'))
quantidade_de_anos = int(input('qual o numero de anos a pagar?'))

def valor_da_prestacao_mensal(a,b):
    y = a/(b*12)
    return y

valor_da_prestacao_mensal_do_usuario = valor_da_prestacao_mensal(valor_da_casa,quantidade_de_anos)

if valor_da_prestacao_mensal_do_usuario > 0.3*salario :
    print('Empréstimo não aprovado')
else :
    print('Empréstimo aprovado')