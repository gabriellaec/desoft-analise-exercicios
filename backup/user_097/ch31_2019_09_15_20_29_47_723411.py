v = input("Informe o valor da casa: ")
s = input("Informe o salário do comprador: ")
a = input("Informe a quantidade de anos a pagar: ")

ps = (0.3*s)
pm = (v/a*12)

if (pm<=ps):
    print("Empréstimo aprovado")
elif (pm>ps):
    print("Empréstimo não aprovado")