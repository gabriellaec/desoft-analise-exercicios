casa= float(input("valor casa:"))
sal=float(input("salário:"))
anos=int(input("prestação"))
def prestacao(casa,anos):
    x=casa/anos
if x > 1.3*sal:
    print('Emprestimo não aprovado)
else:
    print('Emprestimo aprovado')