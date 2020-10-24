valor=float(input("Valor da casa: \n"))
salario=float(input("Salário: \n"))
tempo=float(input("Anos a pagar: \n"))

tempo=12*tempo #meses
p=valor/tempo

if(p<=0.3*salario):
    print("Empréstimo Aprovado")
else:
    print("Empréstimo não aprovado")