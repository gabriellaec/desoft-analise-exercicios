def emprestimo(casa, salario, anos):
    prestacao = casa/(anos*12)
    if (prestacao <= (salario*0.3)):
        return print ('Empréstimo aprovado')
    else:
        return print ('Empréstimo não aprovado')