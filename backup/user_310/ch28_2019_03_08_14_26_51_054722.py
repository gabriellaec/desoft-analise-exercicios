velocidade=int(input("Velocidade: "))
if velocidade >80:
    multa= (velocidade-80)*5
    print("Usuário multado, valor de {0:.2f}".format(multa))
else:
    print("Não foi multado")