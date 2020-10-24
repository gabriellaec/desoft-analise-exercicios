valor = float(input('Digite o valor do emprestimo:'))
meses = int(input('Digite em quantos meses deseja pagar o emprestimo:'))
taxa = float(input('Digite o valor da taxa de juros:'))

def calcula_valor_devido(valor, meses, taxa):
    montante = valor*((1+taxa)**meses)
    return montante
