valor = float(input('Valor da casa?: R$'))
salario = float(input('Quanto você ganha?: R$'))
tempo = int(input('Em quantos anos vai pagar?: R$'))
meses = tempo*12
emprestimo = valor/meses
if emprestimo > (salario*0.3):
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')