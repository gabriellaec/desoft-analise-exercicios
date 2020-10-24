def aprova_emprestimo(casa,anos,salario):
    prestacao=casa/(anos*12)
    if prestacao > 0.3*salario:
        return "Empréstimo não aprovado"
    else:
        return "Empréstimo aprovado"
casa=int(input("qual o valor da casa: "))
anos=int(input("quantos anos: "))
salario=int(input("qual seu salário: "))
print(aprova_emprestimo(casa,anos,salario))
