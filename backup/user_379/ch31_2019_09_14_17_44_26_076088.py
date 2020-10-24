emp=int(input("digite o valor do empréstimo"))
divida=int(input("digite em quantos anos pagará"))
salario=int(input("digite o salário"))

def funcao(emp,divida,salario):
    por_do_sal=(30/100*salario)
    emprestimo=(emp/divida)
    if emprestimo>por_do_sal:
        return "Empréstimo não aprovado"
    elif emprestimo<por_do_sal:
        return "Empréstimo aprovado"