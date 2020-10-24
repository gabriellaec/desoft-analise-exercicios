x=int(input("Qual a velocidade do seu carro? "))
if  x>80:
    print("Voce recebeu uma multa no valor de R$:{0:.2f}".format(float((x-80)*5)))
else:
    print("Não foi multado")
   
    