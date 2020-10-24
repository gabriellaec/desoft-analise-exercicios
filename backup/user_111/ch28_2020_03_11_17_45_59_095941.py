numero=1
limite=True
while limite:
    if numero==1/(2**99):
        limite=False
    numero=numero*(1/2)
    soma=(numero*((1/2)**100-1)/(-(1/2)))
    print("A soma é: ", soma)