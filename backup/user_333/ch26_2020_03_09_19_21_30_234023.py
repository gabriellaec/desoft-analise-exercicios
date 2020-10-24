valor_da_casa=float(input('Quanto custa a casa? '))
salario=float(input('Qual seu salário? '))
quantidade_anos=float(input('Em quanto tempo pagará o imposto? '))

def aprovacao_do_emprestimo(valor,salario,anos):
    prestacao_mensal=valor/(anos*12)
    if prestacao_mensal<=0.3*salario:
        resultado=str('Empréstimo aprovado')
    else:
        resultado=str('Empréstimo não aprovado')
    return resultado

print(aprovacao_do_emprestimo(valor_da_casa,salario,quantidade_anos))