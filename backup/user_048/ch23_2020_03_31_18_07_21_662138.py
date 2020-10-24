d=input("Qua a velocidade do carro, em km/h")
if int(d)>80:
    x=int(d)-80
    y=x*5
    print("voce foi multado em RS", "%.2f" % y)
else:
    print("voce nao foi multado")