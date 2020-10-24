def libras_para_kg(a):
    peso=a/2.2
    return peso
a=float(input("peso em libras:"))
b=libras_para_kg(a)
print("{0:.6f}".format(b))