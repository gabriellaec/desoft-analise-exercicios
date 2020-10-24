def emprestimo_bancario (valor, salario, ano):
    prestacao_mensal = valor / (ano * 12)
    if (prestacao_mensal > salario * 0.3):
        return("Empréstimo não aprovado")
    else: 
        return("Empréstimo aprovado")
valor = int(input("Valor da casa a compra "))
salario = int(input("valor do salario "))
ano = int(input("quantos anos? "))
print(emprestimo_bancario(valor, salario, ano))