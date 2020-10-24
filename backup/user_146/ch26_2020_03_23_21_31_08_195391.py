valor_casa = float(input('Qual o valor da casa? '))
valor_salario = float(input('Qual o valor do salario? '))
anos_a_pagar = int(input('Em quanto tempo vais pagar? '))
def prestacao(valor_casa,valor_salario,anos_a_pagar):
    if valor_casa/(anos_a_pagar*12) > 0.3*valor_salario:
        print('Empréstimono não aprovado')
    else:
        print('Empréstimo aprovado')