def libras_para_kg(a):
    peso=a/2.2
    return peso

b=float(input("peso em libras:"))
print("{0:.6f}".format(libras_para_kg(b)))