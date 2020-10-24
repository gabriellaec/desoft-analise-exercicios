pesol =float(input("Escreva o valor do peso em libras"))
def libras_para_kg (x):
    y = x/2.2046
    return y
funcao = libras_para_kg (pesol)
print ("{0} libras são {1:.6} quilogramas.".format (pesol,funcao))