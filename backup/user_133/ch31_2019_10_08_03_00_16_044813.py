valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salario: '))
anos = int(input('Digite a quantidade de anos a pagar: '))

prestacao = (valor / anos) / 12
limite = 0.3 * salario

if prestacao > limite:
    print ('Emprestimo nao aprovado')
else:
    print ('Emprestimo aprovado')