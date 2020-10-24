val= input("Qual o valor da conta? ")
val= float(val)
def conta(val):
    fin = 1.1*val
    return fin
print("Valor da conta com 10%: R${0:.2f}".format(conta(val)))