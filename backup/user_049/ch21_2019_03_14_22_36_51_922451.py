valor=int(input('Qual é o valor da conta? '))
def porcentagem(valor):
    y=valor*1.1
    return y
x=porcentagem(valor)
print ("Valor da conta com 10%: R$ {0:.2f}".format(x))