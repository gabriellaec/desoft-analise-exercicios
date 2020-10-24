def ver_emprestimo(valor_casa,salario,anos_pagar):
    valor_prestacao = ((valor_casa)/(anos_pagar*12))
    if (valor_prestacao > (0.3*salario)):
        return 'Empréstimo não aprovado'
    else:
        return 'Empréstimo aprovado'

valor_casa = float(input("Valor da Casa: "))

salario = float(input("Valor do Salário: "))

anos_pagar = float(input("Qte de Anos: "))

teste = ver_emprestimo(valor_casa,salario,anos_pagar)
print(teste)