def emprestimo(valor, salario, anos):
    if (valor/(anos*12)) > (salario * 0.3):
        return ("Empréstimo não aprovado")
    else:
        return "Empréstimo aprovado"