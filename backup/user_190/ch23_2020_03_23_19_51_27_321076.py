v=float(input("velocidade?: "))
if v>80:
    multa=5*(v-80)
    print('Multado em R${0:.2f}.format(multa))
else:
    print ("Não foi multado")
    