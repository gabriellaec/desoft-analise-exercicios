velocidade=(int(input("Qual a velocidade do seu carro?: ")))

if velocidade > 80:
    multa = (velocidade-80)*5
    print("Sua multa foi de {:12.2f}".format(multa))
else:
    print("Não foi multado")
    
    
    
