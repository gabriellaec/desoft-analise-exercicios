def libras_para_kg (libras):
    quilogramas = libras/2.2046
    return quilogramas

lib = 7

funcao = libras_para_kg (lib)
print ('{0:.6f}'.format(funcao))