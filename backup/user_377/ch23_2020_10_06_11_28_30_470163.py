vel=int(input("Qual a sua velocidade? "))
if vel > 80:
    print ("Foi multado")
    a = 5*(vel-80)
elif vel <= 80:
    print ("Não foi multado")
print("Multado em {0:.2f}".format(a)) 