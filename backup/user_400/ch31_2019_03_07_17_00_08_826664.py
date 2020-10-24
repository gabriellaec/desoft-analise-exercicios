valor = int(input())
salario = int(input())
anos = int(input())
meses = anos*12
prestação = valor/meses

if prestação > 0.3*salario:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")