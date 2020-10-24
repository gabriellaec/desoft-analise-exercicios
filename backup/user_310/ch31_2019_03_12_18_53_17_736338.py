valor_casa= float(input("valor da casa: "))
salario= float(input("salario: "))
anos= float(input("anos: "))

prestacao= valor_casa/anos*12

if prestacao>salario*0.3:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")