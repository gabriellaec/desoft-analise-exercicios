def libras_para_kg(libras):
    k = libras/2.2
    return k

PESO = float(input("peso em libras:"))
print("{0:.6f}".format(libras_para_kg(PESO)))