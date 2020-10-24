def encontra_cateto(y,z):
    x = (y*y - z*z)**1/2
    return x
hipotenusa = int(input("coloque a hipootenusa "))
cateto = int(input("coloque o cateto "))
print(encontra_cateto(hipotenusa, cateto))