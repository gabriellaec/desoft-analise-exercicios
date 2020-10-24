b=0
p=0

def calcula_prestacao(v,a):
    p = v/a
    b = salario*0.30
    if p > b:
        return 'Empréstimo não aprovado'
    else:
        return 'Empréstimo aprovado'
    
valor_casa = int(input('Qual o valor da casa a comprar?'))
salario = int(input('Qual seu salário?'))
anos = int(input('Qual a quantidade de anos a pagar?'))


print (calcula_prestacao(valor_casa, anos))
