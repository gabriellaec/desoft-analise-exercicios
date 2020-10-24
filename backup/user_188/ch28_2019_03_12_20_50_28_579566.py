def multa_velocidade(v):
    if v > 80:
        multa = (v - 80) * 5
        print("{0:.2f}".format(multa))
    else:
        print("Não foi multado")

velocidade = float(input("Qual a sua velocidade? "))
multa_velocidade(velocidade)