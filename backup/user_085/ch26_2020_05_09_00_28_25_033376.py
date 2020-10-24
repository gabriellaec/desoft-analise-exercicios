valor_da_casa = float(input('Valor da casa:'))
salario = float(input('Salário mensal: '))
q_anos = float(input('Anos: '))
q_meses = q_anos * 12
p_mensal = (valor_da_casa/q_meses)
if p_mensal > (salario * 0.3):
    print('Emprérstimo aprovado')
elif p_mensal < (salario * 0.3):
    print('Empréstimo não aprovado')