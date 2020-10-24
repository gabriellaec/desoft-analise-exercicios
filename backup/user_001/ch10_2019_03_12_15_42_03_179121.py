a = int(input("peso em libras:"))
def libras_para_kg(a):
    peso=a/2.2
    return peso
print("{0:.6f}".format(libras_para_kg(a)))