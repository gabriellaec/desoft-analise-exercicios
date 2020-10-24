cas =int(input("Qual o valor da casa ? "))
sal =int(input("Qual o seu salário ? "))
ano =int(input("Você pagará em quantos anos ? "))
val_pres = cas/(ano/12)
if val_pres > 0.3*sal:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")