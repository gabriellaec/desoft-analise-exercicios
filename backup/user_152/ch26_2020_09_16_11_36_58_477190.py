def emprestimo (valor, salario, anos):
    parcela = valor/(anos*12)
    if (parcela>(salario*0.3)):
       print("Empréstimo não aprovado")
    elif (parcela<=(salario*0.3)):
       print("Empréstimo aprovado")

v = float(input("Entre com o valor da casa a comprar: "))
s = float(input("Entre com o valor do salário: "))
a = float(input("Entre com a quantidade de anos a pagar: "))
emprestimo(v, s, a)