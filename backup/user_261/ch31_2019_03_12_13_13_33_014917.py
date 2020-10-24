a=int(input("valor da casa:"))
b=int(input("salário:"))
c=int(input("quantos anos pra pagar:"))
p=a/(c*12)
n=0.3*b
if p>n:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")
          