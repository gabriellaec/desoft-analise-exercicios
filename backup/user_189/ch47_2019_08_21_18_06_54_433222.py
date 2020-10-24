def mes_x(n):
    meses=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    return meses[n-1]

n=int(input("qual o numero do Mês?: "))
print(mes_x(n))