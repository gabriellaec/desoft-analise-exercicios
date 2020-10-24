def encontra_cateto(y,z):
    x**2 = y**2 - z**2
    return z
hipotenusa = int(input("coloque a hipootenusa"))
cateto = int(input("coloque o cateto"))
print(encontra_cateto(hipotenusa, cateto))