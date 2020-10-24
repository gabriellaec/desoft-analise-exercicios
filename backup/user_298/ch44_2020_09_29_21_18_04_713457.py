meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

escolhido = input("Digite o mes: ")
numero = meses.index(escolhido) + 1
if escolhido in meses:
    print(numero)
else:
    print("Mes incorreto!")