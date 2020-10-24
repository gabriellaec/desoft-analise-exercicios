valor_casa = int(input('Qual o valor da casa? '))
valor_salario = float(input('Qual o valor do salario? '))
anos_a_pagar = int(input('Em quanto tempo vais pagar? '))
def prestacao(valor_casa,valor_salario,anos_a_pagar):
    anos_meses = anos_a_pagar*12
    valor_prestacao = valor_casa/anos_meses
    if valor_prestacao > valor_salario * 0.3:
        return prestacao
        print('Empréstimo não aprovado')
    else:
        print('Empréstimo aprovado')