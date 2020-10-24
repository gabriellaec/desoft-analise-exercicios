valor= int(input("valor: "))
salario= int(input("salário: "))
anos= int(input("anos: "))
prestacao= valor/anos*12
if prestacao>=0.3*salario:
    "Empréstimo não aprovado"
else:
    "Empréstimo aprovado"