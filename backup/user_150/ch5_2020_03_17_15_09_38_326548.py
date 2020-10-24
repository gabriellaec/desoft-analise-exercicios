def libras_para_kg(libras):
    kilograma = libras / 2,2046
    return kilograma
libras = float (input('Digite o peso em libras: '))
print('O peso em kilogramas é: {0: .6f}'.format(libras))