def encontra_cateto(cateto1, hipotenusa):
    cateto2 = (hipotenusa**2 - cateto1**2)**(1/2)
    print("O valor do outro cateto é: {0}".format(cateto2))
c1 = float(input("Infome o valor de um dos catetos: "))
h = float(input("Informe o valor da hipotenusa: "))
encontra_cateto(c1, h)
