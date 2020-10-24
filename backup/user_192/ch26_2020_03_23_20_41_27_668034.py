valor = input('Qual é o valor da casa? ')
salario = input('Qual seu salario? ')
anos = input('Quantos anos a pagar? ')

def prestação(salario, anos):
    y = (int(valor/(anos/12))
    return y
if prestação(salario, anos) > (30/100)*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')