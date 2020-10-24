vel=int(input("Qual a sua velocidade? "))
if vel > 80:
    multa=5*(vel-80)
    print "Foi multado"
elif vel <= 80:
    print "Não foi multado"
print("Multado em {0:.2f}".format(multa))