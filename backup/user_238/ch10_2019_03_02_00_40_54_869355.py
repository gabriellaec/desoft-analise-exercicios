def libras_para_kg(libras):
    kilograma=libras/2.2046
    return kilograma
libras=int(input('seu peso em libras: '))
print('%.6f'%(libras_para_kg(libras)))
