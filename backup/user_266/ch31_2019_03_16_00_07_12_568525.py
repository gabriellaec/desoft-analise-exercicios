CASA=float(input('Valor da casa? '))
SALARIO=float(input('Qual é o seu salário? '))
ANOS=int(input('Quantos anos? '))
PRESTACAO = CASA / (ANOS * 12)
if PRESTACAO > 0.3 * SALARIO:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')