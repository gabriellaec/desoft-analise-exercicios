n=int(input("Numero do mês: "))

meses=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

if(n<13):
    print(meses[n-1])
if(n<1):
    print("Mês inválido")