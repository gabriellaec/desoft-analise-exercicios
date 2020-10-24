valor_da_casa = int(input('Qual o valor da casa que deseja comprar? '))
salario = int(input('Qual seu salario? '))
tempo_para_pagar = int(input('Em quantos anos pretende pagar o emprestimo? '))
def emprestimo(valor_da_casa, salario, tempo_para_pagar):
    salario30 = salario*0.3
    prestacao_da_casa = valor_da_casa/(tempo_para_pagar*12)
    if prestacao_da_casa > salario30:
        print('Empréstimo não aprovado')
    else:
        print('Empréstimo aprovado')
    return "a"
emprestimo(valor_da_casa, salario, tempo_para_pagar)