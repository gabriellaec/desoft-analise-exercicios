casa= float(input('Qual o valor da casa? '))
salario= float(input('Qual o seu salario? '))
quantidade_de_anos_a_pagar= float(input('Quantidade de anos a pagar '))
def valor_prestacao(casa, salario,quantidade_de_anos_a_pagar):
    prestacao= casa / (quantidade_de_anos_a_pagar * 12)
    if (salario * 0.3) >= prestacao:
        print('Empréstimo aprovado')
    elif (salario * 0.3) < prestacao:
        print('Empréstimo não aprovado')
valor_prestacao(casa, salario,quantidade_de_anos_a_pagar)