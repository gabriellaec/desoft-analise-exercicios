def prestacao(valor, anos):
    y = valor/(12*anos)
    return y
valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario? '))
anos = float(input('Quantos anos? '))
if (valor, anos) > 0.3*(salario):
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')