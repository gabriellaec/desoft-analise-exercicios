valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salario: '))
anos = int(input('Digite a quantidade de anos a pagar: '))

prestacao = valor / (anos * 12)
if prestacao > (0.3 * salario):
    print ('Emprestimo nao aprovado')
else:
    print ('Emprestimo aprovado')