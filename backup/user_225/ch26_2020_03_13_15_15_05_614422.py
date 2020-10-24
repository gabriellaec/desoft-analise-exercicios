valordacasa =int(input("Valor da casa: "))
salario = int(input("Salário: "))
anosapagar = int(input("Quantidade de anos a pagar: "))

prestacao = valordacasa/(anosapagar * 12)

if prestacao < ((3*salario)/10):
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")