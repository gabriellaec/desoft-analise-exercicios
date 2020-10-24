valor= float(input("valor: "))
salario= float(input("salário: "))
anos= float(input("anos: "))
prestacao= valor/anos
if prestacao>0.3*salario*12:
    "Empréstimo não aprovado"
else:
    "Empréstimo aprovado"
