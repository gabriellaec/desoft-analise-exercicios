conta=float(input("Quanto foi o valor da conta? "))

def dez(conta):
    com10 = conta*1.1
    return com10

print("Valor da conta com 10%: R${0}".format(round(dez(conta), 2)))