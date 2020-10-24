valor_casa = float(input('Digite aqui o valor da casa: '))
salario = float(input('Digite aqui o valor do seu salário: '))
qtd_anos = int(input('Digite aqui a quantidade de anos que deseja pagar: '))

def emprestimo(x, y, z):
    if x / z >= 0.3 * y:
        resultado = 'Empréstimo não aprovado'
    else:
        resultado = 'Empréstimo aprovado'
    return resultado

print(emprestimo(valor_casa, salario, qtd_anos))