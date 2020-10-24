casa = float(input("valor da casa?"))
salario = float(input("Qual o salario?"))
anos = int(input("quantos anos?"))
parcela=casa/anos/12

if parcela <=0.3*salario:
    print ("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")

