valorCasa = int(input("Informe o valor da casa: "))
salario = int(input("Informe o salário do comprador "))
anosPagar = int(input("Informe a quantidade de anos a pagar: "))

prestacaoMensal = valorCasa/(anosPagar*12)
porcentagem = salario*0.3

if (prestacaoMensal>porcentagem):
    print("Empréstimo não aprovado")
elif (prestacaoMensal<=porcentagem):
    print("Empréstimo aprovado")