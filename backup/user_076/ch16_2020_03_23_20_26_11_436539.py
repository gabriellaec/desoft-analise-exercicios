valor=float(input("Digite o valor da sua conta:"))
def serviço(x):
    s  =x*1.1
    return s

print ("Valor da conta com 10%: R$" , "{0:.2f}".format(serviço(valor)))