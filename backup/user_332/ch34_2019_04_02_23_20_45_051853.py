dep = float(input("deposito "))
juros = float(input("Juros "))
i = 1
soma = 0
while(i <= 24):
    soma = dep * (1+juros)**i
    i += 1
    print("Seu ganho foi {0:.2f}".format(soma))

ganho = soma - dep
print(ganho)