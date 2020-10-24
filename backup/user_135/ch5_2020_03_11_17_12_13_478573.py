def libras_para_kg (libras):
    quilogramas = libras*0.453592
    return quilogramas

lib = 7

funcao = libras_para_kg (lib)
print ('{:.6f}'.format(funcao))