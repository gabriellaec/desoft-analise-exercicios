valor=input("qual o valor da conta?")
def serviço(valor):
    valor_com_serviço= valor*1.1
    return "valor da conta com 10%: R${0:.2f}".format(valor_com_serviço)
