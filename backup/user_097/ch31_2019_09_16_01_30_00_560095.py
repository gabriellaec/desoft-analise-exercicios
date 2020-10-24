v = int(input("Informe o valor da casa: "))
s = int(input("Informe o salário do comprador: "))
a = int(input("Informe a quantidade de anos a pagar: "))

porcentagemSalario = (0.3*s)
prestacaoMensal = (v/a*12)

if (prestacaoMensal<=porcentagemSalario):
    print("Empréstimo aprovado")
elif (prestacaoMensal>porcentagemSalario):
    print("Empréstimo não aprovado")
